def binary_search(array: list[int], x: int) -> int:
    low = 0
    high = len(array)
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        else:
            if x > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return None


#in python array.index() fa in automatico la binary search se l'array è ordinato, altrimenti fa il for


#maniera ricorsiva, visita in ordine

def visit_tree(tree: dict[int, list[int]], node: int):
    print(node)
    left_child, right_child = tree.get(node, [None, None])
    if left_child: #is not none
        visit_tree(tree, left_child)
    if right_child:
        visit_tree(tree, right_child)

tree = {4: [3, 5], 3: [2, None], 2: [None, None], 5: [4.5, 6], 4.5: [None, None], 6: [None, None]}
visit_tree(tree, 4)

#in maniera iterativa, depth first search

def visit_tree_iterative(tree:  dict[int, list[int]], root: int):
    stack: list[int] = [root] #LIFO
    while stack: #len > 0
        curr_node = stack.pop()
        print(curr_node)
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append(right_child)
        if left_child:
            stack.append(left_child)

tree = {4: [3, 5], 3: [2, None], 2: [None, None], 5: [4.5, 6], 4.5: [None, None], 6: [None, None]}
visit_tree_iterative(tree, 4)


#BFS

"""def visit_tree_iterative(tree:  dict[int, list[int]], root: int):
    stack: list[int] = [root] #FIFO
    while stack: #len > 0
        curr_node = stack.pop(0)
        print(curr_node)
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append(right_child)
        if left_child:
            stack.append(left_child)
"""

#es: visita in ampiezza calcolando la media per livelli. dizionario con chiave: livello, valore: media

def visit_tree_iterative2(tree:  dict[int, list[int]], root: int) -> dict:
    stack: list[int] = [root] 
    dizionario: dict = {"0": root}
    level: int = 0
    while stack: #len > 0
        curr_node = stack.pop(0)
        #print(curr_node)
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append(right_child)
        if left_child:
            stack.append(left_child)
            level += 1
            if level == 1 and len(stack) == 2:
                dizionario.update({level: sum(stack)/len(stack)})
            if level == 3 and len(stack) == 3:
                dizionario.update({level: sum(stack)/len(stack)})
    print(dizionario)

tree = {4: [3, 5], 3: [2, None], 2: [None, None], 5: [4.5, 6], 4.5: [None, None], 6: [None, None]}
visit_tree_iterative2(tree, 4)
