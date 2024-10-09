from typing import List


def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """

    if path == '.' or path == '':
        return '.'

    if len(path) > 0 and path[0] == '/':
        root = True
    else:
        root = False

    blocks = path.split('/')

    ans_blocks: List[str] = []
    for i in range(len(blocks)):
        if blocks[i] == '..':
            if len(ans_blocks) > 0 and ans_blocks[-1] != '..':
                ans_blocks.pop()
            elif not root:
                ans_blocks.append('..')
        elif blocks[i] != '..' and blocks[i] != '.' and blocks[i] != '':
            ans_blocks.append(blocks[i])

    if root:
        return '/' + '/'.join(ans_blocks)
    else:
        if len(ans_blocks) > 0:
            return '/'.join(ans_blocks)
        else:
            return '.'
