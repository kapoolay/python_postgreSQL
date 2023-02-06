import mymodule
import sys          # sys module helps you see the various file paths

# Running the file prints the following:
# mymodule.py:  mymodule  --> printed from the mymodule.py file
# mylib:  libs.mylib      --> printed from the libs.mylib.py file THRU the mymodule.py file

# Calling a function from an imported module
print(mymodule.divide(10,2))
# 5.0                     --> printed calling the divide function from the mymodule.py


print(sys.modules)         # prints out all of the modules that were imported
'''{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, 
'_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, 
'_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, 
'_weakref': <module '_weakref' (built-in)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 
'posix': <module 'posix' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, 
'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, 
'_codecs': <module '_codecs' (built-in)>, 
'codecs': <module 'codecs' from '/usr/local/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/codecs.py'>, ...... 
'''


'''
You can also import and call the function this way:

import my module
print(mymodule.divide(10, 2))
'''


'''
import sys
print(sys.path)     # ['/Users/Kev/learning/Udemy/python_postgreSQL/python-refresher/29_imports_in_python', '/Users/Kev/learning/Udemy/python_postgreSQL', '/Users/Kev/learning/Udemy/automateTheBoringStuffWithPython', '/usr/local/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', '/usr/local/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9', '/usr/local/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', '/Users/Kev/.local/share/virtualenvs/python_postgreSQL-kOpjPlTp/lib/python3.9/site-packages']
'''


