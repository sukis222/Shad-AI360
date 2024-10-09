def normalize_path(path: str) -> str:
    """
    :param path: unix path to normalize
    :return: normalized path
    """
    sec_path = []
    sec_path_str = ''

    if path == '.' or path == '':
        return '.'

    if len(path) > 0 and path[0] == '/':
        root = True
    else:
        root = False

    '''for i in range(len(path)-1):
        if path[i] == '/' and path[i+1] != '/':
            sec_path.append('/')
            sec_path_str += '/'
        elif path[i] != '/':
            sec_path.append(path[i])
            sec_path_str += path[i]
            
    sec_path_str += path[-1]'''
    blocks = path.split('/')

    ans_blocks = []
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
