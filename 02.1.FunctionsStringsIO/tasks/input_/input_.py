import sys
import typing as tp


def input_(prompt: str | None = None,
           inp: tp.IO[str] | None = None,
           out: tp.IO[str] | None = None) -> str | None:
    """Read a string from `inp` stream. The trailing newline is stripped.

    The `prompt` string, if given, is printed to `out` stream without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), return None.

    `inp` and `out` arguments are optional and should default to `sys.stdin`
    and `sys.stdout` respectively.
    """
    if out is None:
        out = sys.stdout
    if prompt is not None:
        out.write(prompt)
        out.flush()
    if inp is not None:
        ans = inp.readline()
        return ans[:-1] if ans != '' else None
    else:
        inp = sys.stdin
        return inp.readline()[:-1]
