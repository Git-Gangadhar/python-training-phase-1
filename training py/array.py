arr=[[1,3,2],
     [4,5,6],
     [7,8,9]
     ]
print(arr[0])#access row 1
print(arr[1][1])#access particular element

#create an array
row=3
col=4
for i in range(row):
    temp=[]
    a=input('enter elements: ').split(' ')
b=list(map(int,a))#convert of datatype
temp.append((b))#store this data in temp
print(temp)
