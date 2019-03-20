import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)

# Other way
from mymodule import say_hi, __version__

say_hi()
print('Version', __version__)

# I could also use: from mymodule import *   but it not imported __version__  because __