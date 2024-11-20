from queue import Queue
from abc import ABC, abstractmethod
from typing import Generator, Any


class SystemCall(ABC):
    """SystemCall yielded by Task to handle with Scheduler"""

    @abstractmethod
    def handle(self, scheduler: 'Scheduler', task: 'Task') -> bool:
        """
        :param scheduler: link to scheduler to manipulate with active tasks
        :param task: task which requested the system call
        :return: an indication that the task must be scheduled again
        """


Coroutine = Generator[SystemCall | None, Any, None]


class Task:
    def __init__(self, task_id: int, target: Coroutine) -> None:
        """
        :param task_id: id of the task
        :param target: coroutine to run. Coroutine can produce system calls.
        System calls are being executed by scheduler and the result sends back to coroutine.
        """
        self.target = target
        self.task_id = task_id
        self.ans = None
        self.wait = False
        self.result = None


    def set_syscall_result(self, result: Any) -> None:
        """
        Saves result of the last system call
        """
        self.result = result

    def step(self) -> SystemCall | None:
        """
        Performs one step of coroutine, i.e. sends result of last system call
        to coroutine (generator), gets yielded value and returns it.
        """

        self.ans = self.target.send(self.result)
        return self.ans


class Scheduler:
    """Scheduler to manipulate with tasks"""

    def __init__(self) -> None:
        self.flag = None
        self.task_id = 0
        self.task_queue: Queue[Task] = Queue()
        self.task_map: dict[int, Task] = {}  # task_id -> task
        self.wait_map: dict[int, list[Task]] = {}  # task_id -> list of waiting tasks
        self.idi = 0
        self.search = None
        self.i = None

    def _schedule_task(self, task: Task) -> None:
        """
        Add task into task queue
        :param task: task to schedule for execution
        """
        self.task_queue.put(task)

    def new(self, target: Coroutine) -> int:
        """
        Create and schedule new task
        :param target: coroutine to wrap in task
        :return: id of newly created task
        """
        self.task_id += 1
        self.task_queue.put(Task(self.task_id, target))
        self.task_map[self.task_id] = Task(self.task_id, target)
        return self.task_id

    def exit_task(self, task_id: int) -> bool:
        """
        PRIVATE API: can be used only from scheduler itself or system calls
        Hint: do not forget to reschedule waiting tasks
        :param task_id: task to remove from scheduler
        :return: true if task id is valid
        """
        self.task_map.pop(task_id)
        return True


    def wait_task(self, task_id: int,  wait_id: int) -> bool:
        """
        PRIVATE API: can be used only from scheduler itself or system calls
        :param task_id: task to hold on until another task is finished
        :param wait_id: id of the other task to wait for
        :return: true if task and wait ids are valid task ids
        """
        while True:
            taska = self.task_queue.get()
            if taska.task_id == wait_id:
                try:
                    taska.step()
                except StopIteration:
                    break
            self.task_queue.put(taska)
        return True


    def run(self, ticks: int | None = None) -> None:
        """
        Executes tasks consequently, gets yielded system calls,
        handles them and reschedules task if needed
        :param ticks: number of iterations (task steps), infinite if not passed
        """
        self.flag = False
        self.ticks = ticks

        if ticks is None:
            self.flag = True
            self.ticks = 0

        i = 0
        while (self.flag or ticks > i) and self.task_queue and self.task_map:
            task_to_execute = self.task_queue.get()
            #print(self.task_map)
            if task_to_execute.task_id in self.task_map:
                if self.wait_map and task_to_execute.task_id in self.wait_map or not self.wait_map:
                    try:
                        #print(self.task_map, 'kiki')
                        yielded_call = task_to_execute.step()
                        if isinstance(yielded_call, GetTid):
                            task_to_execute.result = task_to_execute.task_id
                        elif isinstance(yielded_call, NewTask):
                            self.new(yielded_call.target)
                            task_to_execute.result = self.task_id
                        elif isinstance(yielded_call, KillTask):
                            #print(self.task_queue, self.task_map, yielded_call.tas_id)
                            if yielded_call.tas_id not in self.task_map:
                                task_to_execute.result = False
                            else:
                                self.exit_task(yielded_call.tas_id)

                        elif isinstance(yielded_call, WaitTask):
                            if yielded_call.task_id not in self.task_map:
                                task_to_execute.result = False
                            else:
                                self.wait_map[yielded_call.task_id] = []

                        self.task_queue.put(task_to_execute)

                    except StopIteration:
                        self.task_map.pop(task_to_execute.task_id)
                        if self.wait_map:
                            self.wait_map.pop(task_to_execute.task_id)

                else:
                    self.task_queue.put(task_to_execute)


            else:
                task_to_execute.target.close()
            i += 1



    def empty(self) -> bool:
        """Checks if there are some scheduled tasks"""

        return not bool(self.task_map)


class GetTid(SystemCall):
    """System call to get current task id"""

    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        #task.set_syscall_result = task.id
        return True



class NewTask(SystemCall):
    """System call to create new task from target coroutine"""

    def __init__(self, target: Coroutine) -> None:
        self.target = target

    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        return True


class KillTask(SystemCall):
    """System call to kill task with particular task id"""

    def __init__(self, task_id: int) -> None:
        self.tas_id = task_id


    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        return True


class WaitTask(SystemCall):
    """System call to wait task with particular task id"""

    def __init__(self, task_id: int) -> None:
        self.task_id = task_id

    def handle(self, scheduler: Scheduler, task: Task) -> bool:
        # Note: One shouldn't reschedule task which is waiting for another one.
        # But one must reschedule task if task id to wait for is invalid.
        return True



# def generator_function():
#     i = 12
#     print(i)
#     while True:
#         i += 1
#         print(i)
#         value = yield i**2
#         print(i,  'after')
#         print("Received value:", value)
#
# # Создание генератора
# generator = generator_function()
# print()
# print(generator.__next__())
# print()
# print(generator.send('sex'))
# print()
# print(generator.send('ded'))
# print()
# print(generator.send('dad'))
#
# def infinite_ping() -> Coroutine:
#     while True:
#         print('ping!')
#         yield None
#
# s = infinite_ping()
# next(s)
# s.send(StopIteration)
# next(s)