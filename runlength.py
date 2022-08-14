from typing import List, Any

class ElemCount:

    def __init__(self: 'ElemCount', element: Any, repeats: int) -> None:
        if not isinstance(repeats, int):
            raise ValueError("Number times to repeat an element is not an int")
        
        self.element = element
        self.repeats = repeats

    def increase_repeats(self):
        self.repeats += 1
    
    def __str__(self):
        return f'{self.element}{self.repeats}'

RLEncoded = List[ElemCount]

def encode(elem_list: str) -> RLEncoded:
    result_list: RLEncoded = [ElemCount(elem_list[0], 1)]
    idx: int = 0
    for elem in elem_list[1:]:
        current: ElemCount = result_list[idx]
        if current.element == elem:
            current.increase_repeats()
        else:
            result_list.append(ElemCount(elem, 1))
            idx += 1
    return result_list

def decode(to_decode: RLEncoded) -> str:
    return ''.join([ec.element for ec in to_decode for _ in range(ec.repeats)])

def main(to_encode):
    encoded = encode(to_encode)
    print(f"encoded: {''.join(str(i) for i in encoded)}")
    print(f"decoded: {decode(encoded)}")

if __name__ == '__main__':
    t = input("run length encode: ")
    main(t)