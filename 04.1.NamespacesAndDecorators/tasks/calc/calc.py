import sys
import math
from typing import Any

PROMPT = '>>> '


def run_calc(context: dict[str, Any] | None = None) -> None:
    """Run interactive calculator session in specified namespace"""
    sys.stdout.write(PROMPT)
    s = sys.stdin.readline()
    if s:
        sys.stdout.write(str(eval(s, {"__builtins__" : {}}, context)) + '\n')
    else:
        sys.stdout.write('\n')
    while s:
        sys.stdout.write(f'{PROMPT}')
        s = sys.stdin.readline()
        if s:
            sys.stdout.write(str(eval(s, {"__builtins__" : {}}, context)) + '\n')
        else:
            sys.stdout.write('\n')


if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)
