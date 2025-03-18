import array as arr


Arr = arr.array('i',[1,2,3])
for i in range(len(Arr)):
    print(Arr[i] , end=" ")


Arr.insert(1,4)


print("\n")
for i in range(len(Arr)):
    print(Arr[i] , end=" ")

Arr.append(5)

print("\n")
for i in range(len(Arr)):
    print(Arr[i] , end=" ")


Arr.pop(1)
print("\n")
for i in range(len(Arr)):
    print(Arr[i] , end=" ")


Arr.remove(2)


print("\n")
for i in range(len(Arr)):
    print(Arr[i] , end=" ")