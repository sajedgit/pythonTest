# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    if num  % 2 ==0:
        print("%d is even"%num)
    else:
          print("%d is odd"%num)


list2={'key1':'one','key2':'two'}

for val in list2:
    print(list2[val])

print(list2.items())

for a,b in list2.items():
    print(a)
    print(b)



x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    
else:
    print('All Done!')

