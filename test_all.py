import os

ListofFiles = os.listdir('.')

for entry in ListofFiles:
    if 'test' not in entry: 
        if '.py' in entry:
            print(entry)
            os.system("python3 " + entry)
