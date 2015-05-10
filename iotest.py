#iotest.py

import time

LOG_FILE = 'iotest.log'

def main():
    f = open(LOG_FILE, 'w')
    f.write(time.asctime() + '\n') 
    f.write('test\n')
    f.close()




if __name__ == '__main__':
    main()
