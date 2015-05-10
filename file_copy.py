#file_copy.py
#Copies all file of type FILE_TYPES from directory_destination to
# directory_source
#Override default directories via command line arguments
# argv[1] = source
# argv[2] = destination

#GLOBALS
EXIT_MESSAGE = '\n\nExiting.\n.\n.\n.\n'
#Define file types (lowercase, constant) to be included in copy
FILE_TYPES = ('.png','.gif', '.jpg')
#Default directories, override via cmd line argv
directory_source = 'C:\\Users\\ale\\Documents\\GitHub\\pyth'
directory_destination = 'C:\\temp'
#Displays sizes, for pretty formatting only, constant
SIZE_COLUMN_1 = 25
SIZE_COLUMN_2 = 17
#Log file to be dropped in source directory
LOG_FILE = 'file_copy.log'


import os
import sys
import time
import shutil



def main():

    #fetch mutable globals
    global directory_source
    global directory_destination

    #begin process cmd line arguments
    # print('Num of cmd line args:'.ljust(SIZE_COLUMN_1), len(sys.argv))
    # print('Command line args:'.ljust(SIZE_COLUMN_1), '-'*10)
    # for arg in sys.argv:
        # print(''.ljust(SIZE_COLUMN_1),arg)
    if len(sys.argv) > 1:
        directory_source = sys.argv[1]
        if len(sys.argv) > 2:
            directory_destination = sys.argv[2]

    #validate directories
    if os.path.isdir(directory_source):
        directory_source = os.path.abspath(directory_source)
        print('Source directory:'.ljust(SIZE_COLUMN_1), directory_source)
    else:
        print('Bad source directory.', EXIT_MESSAGE)
        return
    if os.path.isdir(directory_destination):
        directory_destination = os.path.abspath(directory_destination)
        print('Destination directory:'.ljust(SIZE_COLUMN_1),
              directory_destination)
    else:
        print('Bad destination directory.', EXIT_MESSAGE)
        return

    #double check before starting
    if(input('Continue? (Y/N): ').strip().upper() != 'Y'):
        print(EXIT_MESSAGE)
        return

    #begin copy sequency
    os.chdir(directory_source)
    print('Starting from:'.ljust(SIZE_COLUMN_1), os.getcwd())

    #setup log file
    f = open(LOG_FILE, 'w')
    f.write(time.asctime() + '\n'*2)

    #grab files to copy
    copy_files = list()
    for file in os.listdir():
        if file.lower().endswith(FILE_TYPES):
            copy_files.append(file)
        else:
            f.write('Skipping file:'.ljust(SIZE_COLUMN_2) + file + '\n')
    for file in copy_files:
        f.write('Grab:'.ljust(SIZE_COLUMN_2) + file + '\n')
        
    #filter destination directory
    os.chdir(directory_destination)
    print('Jump to:'.ljust(SIZE_COLUMN_1), os.getcwd())
    files_moved = 0
    for file in copy_files:
        if os.path.isfile(file):
            f.write('Already exists:'.ljust(SIZE_COLUMN_2) + file + '\n')
        else:
            f.write('Moving:'.ljust(SIZE_COLUMN_2) + file + '\n')
            #moving files:
            shutil.copy2(os.path.join(directory_source,file),
                         directory_destination)
            files_moved += 1
    print('Files moved:', files_moved)

    #close log file    
    f.close()
    print('Log file: "' + LOG_FILE + '" created in source directory.')
    if(input('Delete log file? (Y/N): ').strip().upper() == 'Y'):
        os.remove(os.path.join(directory_source, LOG_FILE))
        print('Log file deleted.')
    else:
        print('Please review log file for messages.')

    #end main
    

if __name__ == "__main__":
    main()
