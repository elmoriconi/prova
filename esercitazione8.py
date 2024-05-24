class LinkedList:
    def __init__(self):
        self.head: list[Node] = []
        
    def append(self, value):
        self.head.append(Node(value))
        
    def get_node(self, value):
        x = self.head[value]
        return x
        
        
class Node:
    def __init__(self, value):
        self.nodo = value
        if type(self) == list:
            return True
        else:
            self.next = None

    def __str__(self) -> str:
        return f"{self.nodo} {self.next}"
        
def has_cycle(head) -> bool:
    flag = False
    lista = []
    for elem in range(len(head)):
        pos = head[elem].nodo
        next = head[elem].next
        if next == pos:
            return True
        if next not in lista:
            lista.append(head[elem])
        else:
            flag = True
    return flag

ll4 = LinkedList()
ll4.append(1)
node = ll4.head #!!!!!!!!!!!!!!!!!!!!!!!!!! PROBLEMA
node.next = node  # Creating a cycle

print(has_cycle(ll4.head))


