#first test, hello world

import ClassOne

#def getNumber

'''
def main():
    print("Hello, World!")

    person = input('Enter your name: ')
    print('Hello, {}!'.format(person))

    #Error in addition from input.

    x = input("Enter a number: ")
    y = input("Enter a second number: ")
    #print(type(x))
    print('The sum of ', x, ' and ', y, ' is ', int(x)+int(y), '.', sep='')
'''


def main():
    '''
    import socket
    print( socket.gethostname() )

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('www.py4inf.com', 80))
    mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

    while True:
        data = mysock.recv(512)
        if ( len(data) < 1 ) :
            break
        print('-'*10)
        print(data.decode("utf-8"))

    mysock.close()
    '''
    import sqlite3

    conn = sqlite3.connect('music.sqlite3')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Tracks ')
    cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

    cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', 
        ( 'Thunderstruck', 20 ) )
    cur.execute('INSERT INTO Tracks (title, plays) VALUES ( ?, ? )', 
        ( 'My Way', 15 ) )
    conn.commit()
    print('Tracks:')
    cur.execute('SELECT title, plays FROM Tracks')
    for row in cur :
        print(row)
    conn.close()

'''
    word = 'brontosaurus'
    d = dict()
    for c in word:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    #print(d.items())
    for i in d.items():
        print(i)
'''

if __name__ == "__main__":
    main()


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

'''
import fibo
fib=fibo.fib
fib(500)
'''
