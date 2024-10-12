import typing as tp
import heapq


def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    s: tp.List[int] = []
    heapq.heapify(s)

    for i in range(len(input_streams)):
        d = input_streams[i].readline()
        while d != b"":
            each_byte = int(d.decode())
            heapq.heappush(s, each_byte)
            d = input_streams[i].readline()

    while len(s) > 0:
        ans = heapq.heappop(s)
        output_stream.write((str(ans) + '\n').encode('utf-8'))
