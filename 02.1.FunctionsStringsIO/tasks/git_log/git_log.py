import typing as tp


def reformat_git_log(inp: tp.IO[str], out: tp.IO[str]) -> None:
    """Reads git log from `inp` stream, reformats it and prints to `out` stream

    Expected input format: `<sha-1>\t<date>\t<author>\t<email>\t<message>`
    Output format: `<first 7 symbols of sha-1>.....<message>`
    """
    lin = inp.read()

    each_line = lin.split('\n')
    each_line.pop()
    for line in each_line:
        begin = line[0:7]
        underline = line.split('\t')
        end = underline[-1]
        k = '.' * (80 - len(begin) - len(end))
        out.write(begin + k + end + '\n')
