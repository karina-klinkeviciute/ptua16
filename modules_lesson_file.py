import sys

from datetime import datetime

from PIL import Image

from modules_lesson import add

a = add(1, 2)

print(a)

# import dictionaries

# from dictionaries import *

# from dictionaries import a_dict

# print(a_dict)



from exercises import can_find

can_find(['a', 'b', 'c'], ['flower', 'plant', 'animal'])

im = Image.open("img.png")

print(im.format, im.size, im.mode)

# im.show()

today_date = datetime.today()



print(sys.path)


