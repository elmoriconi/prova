def subtract_all(x: list[float], y: float) -> list[float]:
    result: list[float] = []
    for i in x:
        z: float = i - y
        result.append(z)
    return result

x: list[float] = [1,2,3,4,5]
y: float = 5
result: list = subtract_all(x, y)
print(result)