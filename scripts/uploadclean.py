import os, re

def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

purge('/home/kevinscaringi/PictureShift.com/static/uploads/', '^(?!example_01\.png).*')
