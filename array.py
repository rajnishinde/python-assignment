import numpy as np

# list = [[3,6,1,66,90,0], [3,6,1,66,90,0]]
#arr1 = ["rrr","ggg","ffff","hhh"]

# arr1.sort()
#print (arr1)

# for i in range(0,len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i]>arr[j]):
#             temp = arr[i];
#             arr[i] = arr[j];
#             arr[j] = temp;
#
# print();
#
# for i in range(0,len(arr)):
#     print(arr[i],end=" ");



list_1 =[[3,4,3,5,6],[3,4,3,7,6]]
arr_1 = np.array(list_1)
arr_2 = arr_1.dot(arr_1)
print(arr_2),