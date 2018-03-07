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
#myname=input("What is your name?")
#print (myname)  ## execute this statement by python3 filename 

myvar='test'
print (myvar)

#conditional execution  execute by python3 file name
#if(myname=="james"):
 #           print("james is in form")
#else :
 #    print ("no one is great")           


if(myvar=='test'):
    print ("test condition")

else :
    print ("no test")  

#mathmatic in python
x, y, z = 3, -4, 0
x = -x
y = -y
z = -z
print(x, y, z) #(-3,4,0) output


x = 4
y = 10.2
sum = x + y
print (sum)   #14.2 output


print(-3 + 2)  # -1 output
print(-(3 + 2)) # -5 output


# run these by python3
seconds= eval(input('enter the second'))  # example  :: input second :  60  
hours=seconds/3600  ## 3600 seconds = 1 hours
# Compute the remaining seconds after the hours are accounted for
seconds=seconds%3600
# Next, compute the number of minutes in the remaining number of seconds
minutes= seconds// 60 ## 60 seconds = 1 minute
#Compute the remaining seconds after the minutes are accounted for
seconds=seconds % 60

#output of hrs
print (hours,"hr",minutes,"min",seconds,"s")  #output 0.016666666666666666 hr 1 min 0 s

#arthematic operator
m=+ 5 #would assign +5 to n instead of increasing n by five.
n=-5  #would assign −5 to n instead of decreasing n by five.
print(m)  # 5 output
print(n)  # -5 output 


degreesF, degreesC = 0, 0  #Establish some variables
degreesC = 5/9*(degreesF - 32)  #formula to find the celcius
degreesF = eval(input('Enter the temperature in degrees F: ')) # Prompt user for degrees F ,example -2
print(degreesF, "degrees F =", degreesC, 'degrees C') #outupt  2 degrees F = -17.77777777777778 degrees C

print(4/2) # output is 2

# Get two numbers from the user
n1, n2 = eval(input()) # 1
# Compute sum of the two numbers
print(n1 + n2) # 2
# Compute average of the two numbers
print(n1+n2/2) # 3
# Assign some variables
d1 = d2 = 0 # 4
# Compute a quotient
 #print(n1/d1) # 5      # gives an error of ZeroDivisionError: division by zero
# Compute a product
d1=n1*n2    # 6
# Print result
print(d1)