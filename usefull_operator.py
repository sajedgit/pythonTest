a=list(range(0,11,3))
print(a)


mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

aaa=list(zip(mylist1,mylist2))
print(aaa)

for a,b in aaa:
    print("first item is {} and second item is {} ".format(a,b))


ttt=[2,3,5,3,2]
print(ttt)
from random import shuffle
shuffle(ttt)
print(ttt)

# from random import randint
# c=int(input("enter the min no:\n"))
# d=int(input("enter the max no:\n"))
# k=randint(c,d)
# print(k)

word="Print only the words that start with s in this sentence"
lst = word.split(" ")
print(lst)

for var in lst:
    if var[0]=='s':
        print(var)

print(list(range(0,11,2)))

lc=[x for x in range(1,51) if x%3==0]
print(lc)
