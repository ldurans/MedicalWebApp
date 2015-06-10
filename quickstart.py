import os, sys
exe = sys.executable
if exe == None or exe == '':
    sys.exit('Python not installed on your computer.')
os.system(exe + ' manage.py syncdb --noinput')
os.system(exe + ' manage.py runserver')
