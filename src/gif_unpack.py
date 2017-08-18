# gif_unpack.py, r_p/src/
import os, sys

from PIL import Image


def unpack(filename):
    im = Image.open(filename)
    base_name = filename.rsplit('.', 1)[0]
    count = 0
    im.seek(0)
    while True:
        count += 1
        # create a new image and copy content
        m = Image.new('RGBA', (im.size[0], im.size[1]))
        m.paste(im.copy())

        out_file = base_name + '-' + str(count) + '.png'
        # output one file
        m.save(out_file, 'PNG')
        # DEBUG
        print('DEBUG: -> ' + out_file)

        # seek after save image
        try:
            im.seek(im.tell() + 1)
        except EOFError:
            break


def main(args):
    i_f = args[0]

    unpack(i_f)

if __name__ == '__main__':
    main(sys.argv[1:])
# end gif_unpack.py
