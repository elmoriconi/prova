def fibonacci4(n: int) -> int:
    a: int = 1
    b: int = 1
    c: int = 0
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return b

import time

a = time.time()
print(fibonacci4(52))
print(f"tempo_impiegato: {time.time() - a}")