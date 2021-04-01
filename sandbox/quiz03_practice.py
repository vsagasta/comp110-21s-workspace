def dict_trans(data: list[dict[int, str]]) -> list[dict[int, str]]:
    """Fun."""
    for num in range(0, len(data), 2):
        for key in data[num]:
            word: str = data[num][key]
            last: int = len(data[num][key]) - 1
            if key % 2 == 0:
                data[num][key] = word[last]
            else:
                data[num][key] = word[0]
    return data

print(dict_trans([ { 3:"roy" , 2:"unc" } , { 1:"kris" } , { 9:"hello", 11:"there", 2:"!!" } ]))

def list_trans(data: dict[int, list[int]]) -> dict[int, list[int]]:
    """."""
    for row in data:
        i: int = 0
        for num in data[row]:
            data[row][i] = row * num
            i += 1

    return data

print(list_trans({ 2:[1, 2] , 5:[3, 4] }))