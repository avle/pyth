#first test, hello world

import ClassOne


def main():
    print("Hello, World!")

    person = input('Enter your name: ')
    print('Hello, {}!'.format(person))

    '''Error in addition from input.'''

    x = input("Enter a number: ")
    y = input("Enter a second number: ")
    #print(type(x))
    print('The sum of ', x, ' and ', y, ' is ', int(x)+int(y), '.', sep='') #error

#main()
'''
try:
    file = open("text.txt","r")
except:
    print("file did not open")
    exit()

print("file opened successfully")

lineList = []
for line in file:
    lineList.append(line)
file.close()    
for line in lineList:
    print(line, end='')
'''

'''
import ClassOne #get classes from ClassOne file
myBuddy = ClassOne.Calculator() # make myBuddy into a Calculator object
myBuddy.add(2) #use myBuddy's new add method derived from the Calculator class
print(myBuddy.getCurrent()) #print myBuddy's current instance variable 

'''
import fibo
fib=fibo.fib
fib(500)

