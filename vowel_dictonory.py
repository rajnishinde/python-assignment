import numpy as np
# dict = {1: "aeiou", 2: "apple", 3: "grape", 4: "umbrella", 5:"mango"}
# v_list = ["a","e","i","o","u"]
# vowel_list = []
# concenet_list = []
#
# # length = len(dict)
# # middle = length // 2
#
# for (key,value) in dict.items():
#     print(value)
#     length = len(value);
#     middle = int(np.ceil(length/2))
#     print(middle)
#     if middle in v_list:
#        vowel_list.append(value)
#     else:
#         concenet_list.append(value)

dict = {1:"apple",2:"mango",3:"banana",4:"grapes"}
vowels = ["a","e","i","o","u"]
vowelsList = []
consonantList = []

for i in dict.values():
    if(len (i) % 2 == 0):
        midLetter = len(i) // 2-1

        print(i,midLetter)

    else:
        midLetter = len(i) // 2

    if(i[midLetter] in vowels):
        vowelsList.append(i)

        print(i[midLetter])

    else:
        consonantList.append(i)


print("NEW LIST OF FRUITS WITH MIDDLE LETTER VOWEL: ")
print(vowelsList)
print("NEW LIST OF FRUITS WITH MIDDLE LETTER CONSONANT: ")
print(consonantList)
