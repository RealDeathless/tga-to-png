from os import listdir
from os.path import isfile
from PIL import Image


def main():
    for f in listdir():
        if isfile(f):
            n, e = f.split('.')
            if e == "tga":
                Image.open(f).save(f'.\\converted\\{n}.png')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        input()
