import struct
from datetime import datetime, timezone
from typing import Dict, Any

def make_key(data: list[int], i: int) -> tuple[str, int]:
    i += 1
    list_for_key = []
    while  i < len(data) and data[i] != 0:
        list_for_key.append(data[i])
        i += 1
    i += 1
    return bytes(list_for_key).decode(), i

def Binary(elem: bytes) -> bytes:
    return Int32(elem[:-1]) + bytes([0]) + elem

def Int32(elem: Any) -> bytes:
    return struct.pack('i', len(elem) + 1)

def Document(e_list: bytes) -> bytes:
    return struct.pack('i', len(e_list) + 5) + e_list + bytes([0])

def E_list(data: Dict[Any, Any]) -> bytes:
    e_list = b''
    for key in data:
        elem = data[key]
        e_list += Element(key, elem)
    return e_list

def UnE_list(data: list[int], new_data: Dict[Any, Any]) -> None:
    i = 0
    while i < len(data):
        bt = data[i]
        if bt == 2:
            key, i = make_key(data, i)
            #print(i)
            let_amount = data[i]
            i += 4
            list_for_value = []
            while let_amount > 1:
                list_for_value.append(data[i])
                let_amount -= 1
                i += 1
            value = bytes(list_for_value).decode()
            new_data[key] = value
            i += 1

        elif bt == 1:
            key, i = make_key(data, i)
            list_for_value = []
            for j in range(8):
                list_for_value.append(data[i])
                i += 1
            value = struct.unpack('d', bytes(list_for_value))[0]
            new_data[key] = value

        elif bt == 8:
            key, i = make_key(data, i)
            if data[i] == 0:
                value = False
            else:
                value = True
            new_data[key] = value
            i += 1
        #binary data
        elif bt == 5:
            key, i = make_key(data, i)
            num_of_bytes = struct.unpack('i', bytes(data[i:i+4]))[0]
            i += 5
            value = bytes(data[i:i+num_of_bytes])
            i += num_of_bytes
            new_data[key] = value

        elif bt == 9:
            key, i = make_key(data, i)
            dt = data[i]
            value = datetime(1970, 1, 1, 0, 0, 0, dt*1000, tzinfo=timezone.utc)
            new_data[key] = value
            i += 8

        elif bt == 3:
            key, i = make_key(data, i)
            amount_of_bytes_in_doc = data[i]
            value = unmarshal(bytes(data[i:i+amount_of_bytes_in_doc]))
            i += amount_of_bytes_in_doc
            new_data[key] = value

        elif bt == 4:
            key, i = make_key(data, i)
            amount_of_bytes_in_doc = struct.unpack('i', bytes(data[i:i+4]))[0]
            value = unmarshal(bytes(data[i:i+amount_of_bytes_in_doc]))
            i += amount_of_bytes_in_doc
            list_from_dict = []
            for k in value:
                list_from_dict.append(value[k])
            new_data[key] = list_from_dict

        elif bt == 16:
            key, i = make_key(data, i)
            value = struct.unpack('i', bytes(data[i : i + 4]))[0]
            new_data[key] = value
            i += 4

        elif bt == 18:
            key, i = make_key(data, i)
            value = struct.unpack('q', bytes(data[i : i + 8]))[0]
            new_data[key] = value
            i += 8

        elif bt == 6:
            key, i = make_key(data, i)
            value = None
            new_data[key] = value


def Element(key: str, elem: Any) -> bytes:
    e_name = Cstring(key)
    if isinstance(elem, str):
        return bytes([2]) + e_name + String(elem)
    if isinstance(elem, float):
        return bytes([1]) + e_name + struct.pack("d", elem)
    if isinstance(elem, bool):
        return bytes([8]) + e_name + bytes([elem])
    if isinstance(elem, bytes):
        return bytes([5]) + e_name + Binary(elem)
    if isinstance(elem, bytearray):
        return bytes([5]) + e_name + Binary(elem)
    if isinstance(elem, datetime):
        delta_time = int((elem.timestamp() - datetime(1970, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc).timestamp())*1000)
        return bytes([9]) + e_name + bytes([delta_time]) + bytes([0, 0, 0, 0, 0, 0, 0])
    if isinstance(elem, dict):
        return bytes([3]) + e_name + marshal(elem)
    if isinstance(elem, list) or isinstance(elem, tuple):
        new_data = dict()
        for i in range(len(elem)):
            new_data[str(i)] = elem[i]
        return bytes([4]) + e_name + marshal(new_data)
    if isinstance(elem, int):
        if -2147483648 <= elem <= 2147483647:
            return bytes([16]) + e_name + struct.pack('i', elem)
        else:
            return bytes([18]) + e_name + struct.pack('q', elem)
    if elem is None:
        return bytes([6]) + e_name


def String(elem: str) -> bytes:
    return Int32(elem) + elem.encode() + bytes([0])


def Cstring(elem: str) -> bytes:
    return elem.encode() + bytes([0])


def marshal(data: Dict[Any, Any]) -> bytes:
    # Сортируем data по ключам и присваиваем к data
    lst = []
    new_data = {}
    for key in data:
        lst.append(key)
    flag = False
    for elem in lst:
        if not elem.isdigit():
            flag = True
    if flag:
        lst.sort()
    for elem in lst:
        new_data[elem] = data[elem]
    data = new_data
    e_list = E_list(data)
    return Document(e_list)


def unmarshal(data: bytes) -> Dict[Any, Any]:
    data = list(data)
    new_data = {}
    UnE_list(data[4:-1], new_data)
    return new_data

'''
#print(struct.unpack('=B', b'1'))
g = {"вася": float('0.0'),
    "vasya": float('-0.0'),
    "12345": float('inf'),
    "": float('-inf'),
    "\t": float('nan'),}
d = marshal(g)
print(list(d))
#print(list(b'' + b'34' + b'1'))
print(datetime(1970, 1, 1, tzinfo=timezone.utc))
#print(bytes([3, 87]))
print(unmarshal(d))
#print(f.marshal(d))'''