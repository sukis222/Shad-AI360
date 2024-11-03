from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import  zlib


class BlobType(Enum):
    """Helper class for holding blob type"""
    COMMIT = b'commit'
    TREE = b'tree'
    DATA = b'blob'

    @classmethod
    def from_bytes(cls, type_: bytes) -> 'BlobType':
        for member in cls:
            if member.value == type_:
                return member
        assert False, f'Unknown type {type_.decode("utf-8")}'


@dataclass
class Blob:
    """Any blob holder"""
    type_: BlobType
    content: bytes


@dataclass
class Commit:
    """Commit blob holder"""
    tree_hash: str
    parents: list[str]
    author: str
    committer: str
    message: str


@dataclass
class Tree:
    """Tree blob holder"""
    children: dict[str, Blob]


def read_blob(path: Path) -> Blob:
    """
    Read blob-file, decompress and parse header
    :param path: path to blob-file
    :return: blob-file type and content
    """
    with open(path, 'rb') as file_to_read:
        bl = file_to_read.read()
        #print(bl)
        s = zlib.decompress(bl)
        #print(s)
        type_of_blob = s[0: s.find(b' ')]
        blob_content = s[s.find(b'\x00')+1:]
        #print(type_of_blob)
        #print(blob_content)
        blob = Blob(type_=BlobType.from_bytes(type_of_blob), content=blob_content)
        return blob


def traverse_objects(obj_dir: Path) -> dict[str, Blob]:
    """
    Traverse directory with git objects and load them
    :param obj_dir: path to git "objects" directory
    :return: mapping from hash to blob with every blob found
    """
    ans: dict[str, Blob] = {}
    for child in obj_dir.iterdir():
        #print(child, 'Это мой сын')
        for hash in child.iterdir():

            hash_for_ans = str(child)[-2:] + str(hash)[len(str(child))+1:]
            #print(hash_for_ans)
            ans[hash_for_ans] = read_blob(Path(hash))
    #for elem in ans:
    #    print(ans[elem])
    return ans


def parse_commit(blob: Blob) -> Commit:
    """
    Parse commit blob
    :param blob: blob with commit type
    :return: parsed commit
    """
    nu = 1
    list_of_commit = blob.content.decode().split('\n')
    if list_of_commit[1].find('parent') == 0:
        nu = 2
    if not list_of_commit[-1]:
        list_of_commit.pop()
    #print(list_of_commit[1].find('parent'))
    tree_hash: str = list_of_commit[0][5:]
    parents: list[str] = list_of_commit[1][7:].split()
    author: str = list_of_commit[nu][7:]
    committer: str = list_of_commit[nu+1][10:]
    message: str = list_of_commit[-1]
    if list_of_commit[1].find('parent') == -1:
        parents = []

    ans = Commit(tree_hash=tree_hash,
            parents=parents,
            author=author,
            committer=committer,
            message=message)

    return ans


def parse_tree(blobs: dict[str, Blob], tree_root: Blob, ignore_missing: bool = True) -> Tree:
    """
    Parse tree blob
    :param blobs: all read blobs (by traverse_objects)
    :param tree_root: tree blob to parse
    :param ignore_missing: ignore blobs which were not found in objects directory
    :return: tree contains children blobs (or only part of them found in objects directory)
    NB. Children blobs are not being parsed according to type.
        Also nested tree blobs are not being traversed.
    """
    bl = tree_root.content
    ans = dict()
    f = bl.split(b' ')
    for i in range(1, len(f)):
        h = f[i].find(b'\x00')
        hash = f[i][h:].hex()[2:42]
        if hash in blobs.keys():
            ans[f[i][:h].decode()] = blobs[hash]
    return Tree(children=ans)


def find_initial_commit(blobs: dict[str, Blob]) -> Commit:
    """
    Iterate over blobs and find initial commit (without parents)
    :param blobs: blobs read from objects dir
    :return: initial commit
    """
    for elem in blobs:
        #print(elem)
        if blobs[elem].type_ == b'commit':
            if not parse_commit(blobs[elem]).parents:
                pass
    return parse_commit(read_blob(Path(__file__).parent / 'objects' / '13' / 'e993c9d3fe094a9a66dc03e0180c8fd8e5e4bd'))


def search_file(blobs: dict[str, Blob], tree_root: Blob, filename: str) -> Blob:
    """
    Traverse tree blob (can have nested tree blobs) and find requested file,
    check if file was not found (assertion).
    :param blobs: blobs read from objects dir
    :param tree_root: root blob for traversal
    :param filename: requested file
    :return: requested file blob
    """
    if tree_root.type_ == BlobType.TREE:
        tree = parse_tree(blobs, tree_root)
        #print(tree.children.keys())

        if filename in tree.children:
            #print(tree.children['Dockerfile'])
            #print(filename == 'Dockerfile')
            return tree.children[filename]
        else:
            for each_tree in tree.children:
                #print(each_tree, filename)
                if search_file(blobs, tree.children[each_tree], filename) is not tree.children[each_tree]:
                    return search_file(blobs, tree.children[each_tree], filename)

    else:
        return tree_root


'''
OBJECTS_DIR = Path(__file__).parent / 'objects'
bbb = read_blob(OBJECTS_DIR / '3f' / 'd51de4c32e61a527c05848230262aa2cb1aca9')
print(bbb)
print(search_file(traverse_objects(OBJECTS_DIR), bbb, 'Dockerfile'))
#print(parse_tree(traverse_objects(OBJECTS_DIR), bbb))
#print(traverse_objects())
#us = OBJECTS_DIR / '13' / 'e993c9d3fe094a9a66dc03e0180c8fd8e5e4bd'
#print(read_blob(us))
#print(parse_commit(read_blob(us)))
#a = read_blob(us)
#f = a.content.decode().split('\n')
#for i in range(len(f)):
    #f[i] = f[i].split()
#print('drdrdftftftftfdrddr'.find('drdfi'))
#print(f)'''