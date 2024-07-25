def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    letter_counter = 0 
    word_counter = 0
    shortest_word = 1000000
    word = None
    for elem in strs:
        if len(elem) < shortest_word:
            shortest_word = len(elem)
            word = elem
    for elem in strs[0]:
        while letter_counter < shortest_word:
            while word_counter < len(strs):            
                if elem == strs[word_counter][letter_counter]:
                    pass
                else:
                    if letter_counter == 0:
                        return ""
                    else:
                        return prefix
                word_counter += 1
            prefix = prefix + elem
            letter_counter += 1
    return prefix
       
print(longestCommonPrefix(["flower","flow","flight"]))  
    

"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""