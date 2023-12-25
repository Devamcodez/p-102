import os
import shutil

from_dir="C:/Users/vikra/OneDrive/Desktop/Game Code/C20-Student-boilerplate-code"
to_dir="test_1"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
  name, extensions=os.path.splitext(file)
  if extensions=='':
    continue
  if extensions in['.txt','.doc','.docx','.pdf']:
    path1=from_dir+'/'+file
    path2=to_dir + '/' + "Document_Files"
    path3=to_dir + '/' + "Document_Files" + '/' + file
    if os.path.exists(path2):
        print("Moving "+file+"...")
        shutil.move(path1,path3)
    else:
        os.mkdir(path2)
        print("Moving "+file+"...")
        shutil.move(path1,path3)

