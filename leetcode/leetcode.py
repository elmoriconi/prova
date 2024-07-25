def minDistance(word1: str, word2: str) -> int:
    operations = 0
    word1 = list(word1)
    word3 = list(word2)
    word2 = list(word2)
    for elem in word1:
        if elem not in word2:
            word1.remove(elem)
            operations += 1
        else: 
            word2.remove(elem)
            operations += 1
    print(word1, word2)
    for elem in word2:
        if elem not in word1:
            word1.append(elem)
            word2.remove(elem)
            operations += 1
    print(word1, word2)
    for i in range(len(word3)):
        if word3[i] != word1[i]:
            var = word1[i]
            word1[i] = word3[i]
            word1.append(var)
            operations += 1
    return operations, word1

print(minDistance("intention", "execution"))
print(minDistance("horse", "ros"))

"""Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""        