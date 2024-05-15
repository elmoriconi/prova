#bubble sort

def bubble_sort(x: list[int]):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j] > x[j+1]:
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp