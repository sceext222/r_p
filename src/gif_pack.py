# gif_pack.py, r_p/src/
#
#   --output FILENAME
#   --duration MS
#   --loop LOOP_N
#   -- FILES
#
import os, sys

from PIL import Image


def pack(i_f, o_f, duration=40, loop=0):
    # open first img to get size
    first = Image.open(i_f[0])
    # DEBUG
    print('DEBUG: -> ' + i_f[0])

    size = (first.size[0], first.size[1])
    # DEBUG
    print('DEBUG: size ' + str(size))

    # create output gif
    im = Image.new('RGBA', size)  # FIXME mode 'P' 'L' ?
    # paste first frame
    im.paste(first.copy())
    # read rest frame
    f = []
    for i in range(1, len(i_f)):
        m = Image.open(i_f[i])
        # DEBUG
        print('DEBUG: -> ' + i_f[i])

        f.append(m)
    # DEBUG
    print('DEBUG: => ' + o_f)
    # save output gif
    im.save(o_f, 'GIF', save_all=True, append_images=f, duration=duration, loop=loop)


def main(args):
    i_f = []
    duration = 40  # 40ms, 25fps
    loop = 0  # infinity
    o_f = None

    rest = args[:]
    # parse args
    while len(rest) > 0:
        one, rest = rest[0], rest[1:]
        if one == '--output':
            o_f, rest = rest[0], rest[1:]
        elif one == '--duration':
            d, rest = rest[0], rest[1:]
            duration = int(d)
        elif one == '--':
            i_f, rest = rest[:], []
        else:
            raise Exception('unknow arg  ' + one)
    # TODO more checks on args ?
    # DEBUG
    fps = 1e3 / duration
    print('DEBUG: ' + str(len(i_f)) + ' input files, duration = ' + str(duration) + 'ms ' + str(fps) + 'fps, loop = ' + str(loop))
    pack(i_f, o_f, duration=duration, loop=loop)

if __name__ == '__main__':
    main(sys.argv[1:])
# end gif_pack.py
