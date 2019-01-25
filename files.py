myfile = open('whoops.txt','a+')
myfile.write('\nThis is a new line')
myfile.seek(0)
print(myfile.read())

    
