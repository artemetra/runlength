from typing import List, TypeVar, Union, Any

T = TypeVar('T')
class ElemCount:
    def __init__(self, element: T, number: int) -> None:
        if not isinstance(number, int):
            raise ValueError("Number times to repeat an element is not an int")
        
        self.element = element
        self.number = number
    
    def __repr__(self):
        return f'{self.element}[{self.number}]' if self.number != 1 else f'{self.element}'

RLEncoded = List[ElemCount]
def encode(elem_list: List[T]) -> RLEncoded:
    result_list: RLEncoded = [ElemCount(elem_list[0], 1)]
    idx = 0
    for elem in elem_list[1:]:
        current = result_list[idx]
        if current.element == elem:
            current.number += 1
        else:
            result_list.append(ElemCount(elem, 1))
            idx += 1
    return result_list

def decode(to_decode: RLEncoded) -> List[T]:
    return [ec.element for ec in to_decode for _ in range(ec.number)]

def main(to_encode):
    encoded = encode(to_encode)
    print(f"encoded: {''.join(str(i) for i in encoded)}")
    print(f"decoded: {decode(encoded)}")

if __name__ == '__main__':
    t = input("run length encode: ")
    main(t)