#with open("file_di_prova.txt") as file:
#    pass

#file = open("file_di_prova.txt")
#try:
#   pass
#finally:
#    file.close()

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

reader = open("file_di_prova.txt")
#print(reader)
#reader.close()

try:
    reader.readline()
    print("Sono nella try")
    raise Exception("Eccezione!")

except Exception:
    print("Sono nella except")

finally:
    print(reader)
    reader.close()
    print("Sono nella finally")


"""with open("file_di_prova.txt") as reader:           #come leggere il file line by line
    
    line = reader.readline()

    while line != "":
        print(line)
        line = reader.readline()"""

with open("file_di_prova.txt") as reader:         
    
    line = reader.readline()

    while line != "":
        print(line)
        line = reader.readline()
