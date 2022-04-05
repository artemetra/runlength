from typing import List, TypeVar, Union

class ByteCount:
    def __init__(self, byte: bytes, number: int) -> None:
        if not isinstance(number, int) and len(byte) != 1:
            raise ValueError("The ByteCount constructor should only get one byte as a parameter")
        if not isinstance(number, int):
            raise ValueError("Number times to repeat a byte is not an int")
        
        self.byte = byte
        self.number = number
    
    def __repr__(self):
        return f'{self.byte}[{self.number}]' if self.number != 1 else f'{self.byte}'

RLEncoded = List[ByteCount]

def encode(bytes: Union[bytes, bytearray, str]) -> RLEncoded:
    result_list: RLEncoded = [ByteCount(b'\0',0)]
    idx = 0
    for b in bytes:
        current = result_list[idx]
        if current.byte == b:
            current.number += 1
        else:
            result_list.append(ByteCount(b, 1))
            idx += 1
    return result_list[1:]

def decode(to_decode: RLEncoded) -> Union[bytes, str]:
    try:
        return ''.join(t.byte*t.number for t in to_decode)
    except TypeError:
        return b''.join(t.byte*t.number for t in to_decode)

def main(to_encode):
    encoded = encode(to_encode)
    print("encoded: " + ''.join(str(i) for i in encoded))
    print("decoded: " + decode(encoded))

if __name__ == '__main__':
    t = input("run length encode: ")
    main(t)