import os

while True:
  
  print('\nCurrect directory: ', os.getcwd())
  #print('Absolute path: ', os.path.abspath(os.getcwd()))
  content = os.listdir()
  content.insert(0,'..')
  #content = dict( zip( range(1,len(content)+1), content ) )
  #content_list = list(content.items())
  #for i,j in content_list:
  for i in range(len(content)):
    print(i+1,content[i])
  try:
    selection = int(input("Selection: "))-1
    selection = content[selection]
  except Exception as e:
    print("I didn't understand that: ", e)
    continue
  except:
    print('\n	---Exiting---\n')
    break
  if os.path.isfile(selection):
    #print("You selected a file.")
    with open(selection, 'rb') as f:
      print(f.read().decode())
  elif os.path.isdir(selection):
    print('You selected a directory')
    os.chdir(selection)


