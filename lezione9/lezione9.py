#bubble sort => 64 iterazioni = n**2

def bubble_sort(x: list[int]):
    for _ in range(len(x)):      # _ si usa quando una variabile non è utilizzata
        for j in range(len(x) - 1):
            if x[j] > x[j+1]:
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp

l: list[int] = [235, 53, 5, 43, 567]
bubble_sort(l)
print(l)

#improved bubble sort => 36 iterazioni 

def bubble_sort2(x: list[int]):
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp