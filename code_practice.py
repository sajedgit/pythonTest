num_list=list(range(1,101))

for num in num_list:
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%5==0:
        print("Fizz")
    elif num%3==0:
        print("Buzz")
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
st=st.split()
a=[word[0] for word in st]
print(a)