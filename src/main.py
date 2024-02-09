import os, shutil

path = input('Enter Path to Sort: ')
files = os.listdir(path)

for f in files:
    name, ext = os.path.splitext(f)
    ext = ext[1:]
    
    if os.path.exists(path + '/' + ext):
        upperext = ext.upper()

        shutil.move(path + '/' + f, path + '/' + upperext + '/' + f )
    
    else:
        upperext = ext.upper()
        os.makedirs(path + '/' + upperext)
        shutil.move(path + '/' + f, path + '/' + upperext + '/' + f )