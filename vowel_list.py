list = ["apple","grape","mango","orange","i"]
vowel_list = ["a","e","i","o","u"]
final_vowel_list =[]
concenet_list = []


for i in list:
    # my_list[i]
    # print(i[0])
    if i[0] in vowel_list:
        final_vowel_list.append(i)
    else:
        concenet_list.append(i)
print(final_vowel_list)
print(concenet_list)


# print(set('Mississippi'))
# print("Hello World"[8])
# print("tinker"[1:4])
# print("Hello world"["Hello world".find("r")])
# print("Answer for Question-2:","tinker"["tinker".find("i"):"tinker".find("e")],"\n")