# gif_info.py, r_p/src/
import os, sys
import json

from PIL import Image


def get_info(filename):
    im = Image.open(filename)
    o = {
        'size': im.size,
        'mode': im.mode,
        'n_frames': im.n_frames,
        'filename': im.filename,
        'format': im.format,
        'info': im.info,
    }
    # fix b'' in info
    i = o['info']
    if 'version' in i:
        i['version'] = i['version'].decode('utf-8')
    if ('extension' in i) and (len(i['extension']) > 0):
        i['extension'] = list(i['extension'])
        i['extension'][0] = i['extension'][0].decode('utf-8')

    return o


def main(args):
    i_f = args[0]

    info = get_info(i_f)
    text = json.dumps(info, indent=4, sort_keys=True, ensure_ascii=False)
    print(text)

if __name__ == '__main__':
    main(sys.argv[1:])
# end gif_info.py
