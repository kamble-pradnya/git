#..REMOVE DUPLICATE ELEMENTS IN AN ARRAY..#


arr=[1,3,5,6,3,5,6,1]
print("original array:"+ str(arr))

res=[]
for i in arr:
    if i not in res:
        res.append(i)
print("after removing duplicate elements:" + str(res))

