with open("file_di_prova.txt") as file:
    pass

file = open("file_di_prova.txt")
try:
    pass
finally:
    file.close()

"""
#context manager

class ContextManager:           #open() funziona in modo simile a questo context manager, con un enter ed un exit

    def __enter__(self):
        print("Risorsa acquisita!")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            pass
        print("Risorsa rilasciata!")
        return False
    
with ContextManager() as manager:

    print("Sono dentro with")
"""