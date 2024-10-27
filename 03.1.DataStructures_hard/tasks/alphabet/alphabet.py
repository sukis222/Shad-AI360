import enum
from sys import setrecursionlimit


setrecursionlimit(1000000)


class Status(enum.Enum):
    NEW = 0
    EXTRACTED = 1
    FINISHED = 2


def extract_alphabet(
        graph: dict[str, set[str]]
        ) -> list[str]:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """
    done = set()
    ans = []


    def dfs(ver):
        for elems in graph[ver]:
            if elems not in done:
                dfs(elems)
        done.add(ver)
        ans.append(ver)


    for elem in graph:
        if elem not in done:
            dfs(elem)

    return ans[::-1]

'''d_f.append(elem)
            first_elem = elem
            while len(d_f) != 0:
                for new_elem in graph[first_elem]:
                    d_f.append(new_elem)
                if graph[first_elem] == {}:
                    done.add(first_elem)
                done.add(first_elem)
                first_elem = d_f.popleft()
                ans.append(first_elem)
'''


def build_graph(
        words: list[str]
        ) -> dict[str, set[str]]:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """
    graph = {}
    for elem in words[0]:
        graph.setdefault(elem, set())
    for i in range(1, len(words)):
        j = 0
        f = True
        while j < len(words[i]):
            graph.setdefault(words[i][j], set())
            if j < len(words[i-1]) and words[i][j] != words[i-1][j] and f:
                graph[words[i-1][j]].add(words[i][j])
                f = False
            else:
                j += 1

    return graph


#########################
# Don't change this code
#########################

def get_alphabet(
        words: list[str]
        ) -> list[str]:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)

#########################


