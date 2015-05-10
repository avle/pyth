#test_sqlite3.py
import sqlite3
DATABASE_FILE_NAME = 'sqlite3test.db'

def main():
    conn=sqlite3.connect(DATABASE_FILE_NAME)
    c = conn.cursor()

    #creat table
    c.execute('DROP TABLE IF EXISTS Stocks')
    c.execute('DROP TABLE IF EXISTS Tracks ')
    c.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
    c.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
              ('Thunderstruck', 20) )

    #output
    print('Tracks:')
    c.execute('SELECT * FROM Tracks')
    for row in c:
        print(row)

    conn.commit()
    conn.close()













if __name__ == '__main__':
    main()
