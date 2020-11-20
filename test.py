import sys
# first_name = "Rajni"
# last_name ="Shinde"
# name = first_name + ' ' + last_name
# print(name)

# first_num = int(input("enter first name"))
# last_num = int(input("enter last name"))
# name = first_num +last_num
# print(name)
'''
print(sys.argv[0])
first_num = int(sys.argv[1])
last_num =int(sys.argv[2])
result = first_num+last_num
print(result)'''

#first_name ="rajni"
# # print(first_name[-5])
#print(first_name[0:4])
#print(first_name[::2])
#print(first_name[:2:-1])
#print(first_name[1::2])

# mylist_1= ["rajni",4,4.1,['kumar',6,['sai',7,2.2]]]
# first_name= mylist_1[2]
# # print(first_name)
# last_nm=mylist_1[3][2][2]
# print(last_nm + first_name)

# dict_1 = { 1:"Rajni", 'fruit':['apple','mango',1], 1.2:{1:['shinde',3]}}
# print(dict_1)
# key_list = dict_1.keys()
# print(key_list)
# value_list = dict_1.values()
# print((value_list))
# first_num = dict_1['fruit'][2]
# print(first_num)
# sec_num = dict_1[1.2][1][1]
# print(sec_num + first_num)

# list = ['r,','a,','j,','n,','i,']
# name = ''
# for l in list:
#     name = name + l
# name=name.replace(',','')
# print(name)

dict_1 = {1:[1,2,3], 2:[1,2,4], 3:[1,2,5], 4:[1,2,6], 5:[1,2,7], 6:[1,2,"rajni"]}
last_value =[]
for key in dict_1:
    last_value.append(dict_1[key][2])
print(last_value)
