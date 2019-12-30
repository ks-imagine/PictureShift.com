import os, re
directory = '/home/kevinscaringi/PictureShift.com/static/uploads/'
pattern = '^(?!example_01\.png).*'
def purge(directory, pattern):
    print("BEFORE")
    for f in os.listdir(directory):
        print(f)
        if re.search(pattern, f):
            os.remove(os.path.join(directory, f))

purge(directory, pattern)
print("AFTER")
print(os.listdir(directory))
print("###########")
