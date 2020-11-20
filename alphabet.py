
item_list = ['apple', 'ant', 'mobile', 'phone', 'mango', 'raj', 'rose']
Dic = {}

for word in item_list:
    if word[0] not in Dic.keys():
        Dic[word[0]] = []
        Dic[word[0]].append(word)
        # print(word[0])
    else:
        if word not in Dic[word[0]]:
            Dic[word[0]].append(word)
            # Dic = sorted(Dic.values())
            print(word)

for k,v in Dic.items():
    print(k, ":", v)

sorted(Dic.values())
print(Dic)








