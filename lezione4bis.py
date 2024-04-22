def subtract_all(x: list[float], y: float) -> list[float]:
    result: list[float] = []
    for elem in x:
        z: float = elem - y
        result.append(z)
    return result

x: list[float] = [1,2,3,4,5]
y: float = 5
result: list[float] = subtract_all(x, y)
print(result)

def suBtract_all2(x: list[float], y: float) -> list[float]:
    result: list[float] = []
    for i in range(len(x)):
        z: float = x[i] - y[i]
        result.append(z)
    return result

a: list[float] = [1,2,3,4,5]
b: list[float] = [2,3,4,5,6]
result2: list[float] = suBtract_all2(a, b)
print(result2)