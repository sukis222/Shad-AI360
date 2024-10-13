import typing as tp
from io import SEEK_END
from io import BytesIO
from pathlib import Path
import sys


def tail(filename: Path, lines_amount: int = 10, output: tp.IO[bytes] | None = None) -> None:
    """
    :param filename: file to read lines from (the file can be very large)
    :param lines_amount: number of lines to read
    :param output: stream to write requested amount of last lines from file
                   (if nothing specified stdout will be used)
    """
    ch = -1
    with open(filename, 'rb') as file:

        file.seek(-1, SEEK_END)
        while file.tell() > 0 and file.read().count(b'\n') <= lines_amount:
            ch -= 1
            file.seek(ch, SEEK_END)
        if file.tell() == 0:
            file.seek(0)
        else:
            file.seek(ch, SEEK_END)

        ans = file.read()
        s = ans.count(b'\n')
        for i in range(s):
            ans.replace(b'\n', b'')
        if output is None:
            output = BytesIO()
        output.write(ans[(ans.find(b'\n'))+1:-2])

        print(output.getvalue().decode())

        #file.seek(ch, SEEK_END)
        #sys.stdout.write(file.read().decode())



tail(filename='access.log', lines_amount=10)

