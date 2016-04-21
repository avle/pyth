import os

while True:
  
  print('\nCurrect directory: ', os.getcwd())
  content = os.listdir()
  content.insert(0,'..')  #to back up a directory
  for i in range(len(content)):
    print(i+1,content[i])  #numbered list to select from

  try:  #prompt user for choice here
    selection = int(input("Selection: "))-1
    selection = content[selection]
  except Exception as e:
    print("I didn't understand that: ", e)
    continue
  except:
    print('\n	---Exiting---\n')
    break

  #change directory or print file by bytes
  if os.path.isfile(selection):
    with open(selection, 'rb') as f:
      print(f.read())
  elif os.path.isdir(selection):
    print('You selected a directory')
    os.chdir(selection)


