#es del rettangolo: 

def construct_rectangle(area: float) -> list[float]:
    combos: list = []
    half_area: int = int(area ** 0.5)
    for width in range(1, area + 1):
        for height in range(1, half_area + 1):
            if width * height == area and width >= height:
                combos.append(width, height) #lista di liste
    min_diff: float = float('inf')
    index_diff: int = 0
    for i in range(len(combos)):
        curr_diff: float = combos[i][0] - combos[i][1]
        if curr_diff <= min_diff:
            min_diff = curr_diff
            index_diff = i
    return combos[index_diff]

  
#es dell'armonia:

from collections import Counter

def find_lhs(notes: list[int]) -> int:
    num_freq: dict = dict(Counter(notes))
    max_length = 0
    for num in num_freq:
        max_length = max(max_length, num_freq[num] + num_freq[num+1])
    return max_length