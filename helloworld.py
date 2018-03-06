from datetime   import   datetime

message="hello world"
print (message)

# add the two number 
a=10
b=10
c=a+b
print (c)

#add the first name and last name 
firstname="test"
lastname="jaes"
fullName=firstname+lastname
print(fullName)

#print date time 
print (datetime.now())

#Tested the String 
s = 'hi'
print (s[1])          ## i
print (len(s))        ## 2
print (s + ' there')  ## hi there

pi = 3.14
##text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is '  + str(pi)  ## yes

print (text)  #The value of pi is 3.14

# get input from  user 
myname=input("What is your name?")
#print (myname)  ## execute this statement by python3 filename 

myvar='test'
print (myvar)

#conditional execution  execute by python3 file name
if(myname=="james"):
            print("james is in form")
else :
     print ("no one is great")           


if(myvar=='test'):
    print ("test")

else :
    print ("no test")  


