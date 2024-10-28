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
            #print(hash)
            hash_for_ans = str(child)[-2:] + str(hash)[len(str(child))+1:]
            ans[hash_for_ans] = read_blob(Path(hash))
    #print(ans)
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


def find_initial_commit(blobs: dict[str, Blob]) -> Commit:
    """
    Iterate over blobs and find initial commit (without parents)
    :param blobs: blobs read from objects dir
    :return: initial commit
    """
    for elem in blobs:
        print(elem)
        if blobs[elem].type_ == b'commit':
            if not parse_commit(blobs[elem]).parents:
                return parse_commit(blobs[elem])



def search_file(blobs: dict[str, Blob], tree_root: Blob, filename: str) -> Blob:
    """
    Traverse tree blob (can have nested tree blobs) and find requested file,
    check if file was not found (assertion).
    :param blobs: blobs read from objects dir
    :param tree_root: root blob for traversal
    :param filename: requested file
    :return: requested file blob
    """

'''p = Path(__file__)
print(p)
with open(p, 'b') as file_to_read:
    bl = file_to_read.read()
    s = zlib.decompress(bl)
    print(s)
s = Path("1b/d9ee3785043bb23af69523af7a59b43d1fe533")
print(type(s))
read_blob(Path("README.md"))'''

'''
text = 'fifeifehifhe'

text = text.encode()

print(zlib.compress(text))
print(len('eb3a044c05f7333c00b3cba8be3f40fb68bf4'))
d = bytes(b'eb3a044c05f7333c00b3cba8be3f40fb68bf4')
print(d.decode())
#print(zlib.decompress(bytes.fromhex('71bbce6c337432e3218cf478a2d7d19b9dc82517')))'''

'''
OBJECTS_DIR = Path(__file__).parent / 'objects'
print(OBJECTS_DIR / '71' / 'bbce6c337432e3218cf478a2d7d19b9dc82517')
#traverse_objects(OBJECTS_DIR)

us = OBJECTS_DIR / '13' / 'e993c9d3fe094a9a66dc03e0180c8fd8e5e4bd'
print(parse_commit(read_blob(us)))
a = read_blob(us)
f = a.content.decode().split('\n')
for i in range(len(f)):
    f[i] = f[i].split()
print('drdrdftftftftfdrddr'.find('drdfi'))
print(f)'''