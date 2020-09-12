#..DISPLAY GIVEN ARRAY IN REVERSE ORDER..#


arr=[10,20,30,40,50]
print("original array:")
for i in range(0,len(arr)):
    print(arr[i])
print("array in reverse order:")
for i in range(len(arr)-1,-1,-1):
    print(arr[i])
