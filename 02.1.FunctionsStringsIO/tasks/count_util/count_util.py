def count_util(text: str, flags: str | None = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """
    answer = {'chars' : 0, 'lines' : 0, 'words' : 0, 'longest_line' : 0}

    for elem in text:
        if elem.isalpha() or elem == ' ':
            answer['chars'] += 1

    answer['lines'] = text.count('\n')
    answer['chars'] += answer['lines']
    split_text = text.split('\n')
    sch = 0
    for elem in split_text:
        f = False
        for j in range(len(elem)):
            if elem[j] != ' ' and not f:
                sch += 1
                f = True
            elif elem[j] == ' ':
                f = False

    max_len = 0
    al_len = 0
    for elem in split_text:
        al_len += len(elem)
        if len(elem) > max_len:
            max_len = len(elem)

    answer['longest_line'] = max_len
    answer['words'] = sch - repr(text).count(r'\t')
    ans = dict()
    if flags is not None and flags != '':
         for j in flags:
             if j == 'm':
                 ans['chars'] = answer['chars']
             if j == 'l':
                 ans['lines'] = answer['lines']
             if j == 'L':
                 ans['longest_line'] = answer['longest_line']
             if j == 'w':
                 ans['words'] = answer['words']
    elif flags == '' or flags is None:
        ans = answer
    return ans
