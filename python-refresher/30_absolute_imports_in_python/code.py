import mymodule

print("code.py: ", __name__)


## code.py -> mymodule.py -> mylib.py -> operator.py -> mylib.py -> mymodule.py -> code.py
# operator.py:  libs.operations.operator
# mylib:  libs.mylib
# mymodule.py:  mymodule
# code.py:  __main__