import heapq

from mypy.checkexpr import defaultdict


def normalize(
        text: str
        ) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """
    ans = ''
    for elem in text:
        if elem.isalpha() or elem.isspace():
            ans = ans + elem
    return ans.lower()


def get_words(
        query: str
        ) -> list[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """
    sch = 0
    ans: list[str] = []
    str_for_work = normalize(query)
    for i in range(len(str_for_work)):
        if str_for_work[i] == ' ':
            if sch > 3:
                ans.append(str_for_work[i-sch:i])
            sch = 0
        else:
            sch += 1

    return ans


def build_index(
        banners: list[str]
        ) -> dict[str, list[int]]:
    """
    Create index from words to banners ids with preserving order and without repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """
    ans = defaultdict(list)
    for num in range(len(banners)):
        mini_list = get_words(normalize(banners[num]))
        for elem in mini_list:
            if len(ans[elem]) > 0 and ans[elem][-1] != num or len(ans[elem]) == 0:
                ans[elem].append(num)
    return dict(ans)


def get_banner_indices_by_query(
        query: str,
        index: dict[str, list[int]]
        ) -> list[int]:
    """
    Extract banners indices from index, if all words from query contains in indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """
    a = []
    heapq.heapify(a)
    norm_str = get_words(normalize(query))
    ans: list[int] = []
    for elem in norm_str:
        if elem in index:
            for sss in index[elem]:
                heapq.heappush(a, sss)
    a.sort()
    sch = 1
    if len(norm_str) == 1:
        return a
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            sch += 1
        else:
            if sch == len(norm_str):
                ans.append(a[i-1])
            sch = 1

    if sch == len(norm_str):
        ans.append(a[-1])

    return ans


#########################
# Don't change this code
#########################

def get_banners(
        query: str,
        index: dict[str, list[int]],
        banners: list[str]
        ) -> list[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################


