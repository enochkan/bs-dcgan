import os, sys, glob
from PIL import Image, ImageOps


mydir = os.getcwd()
os.chdir(str(mydir)+'/samples/relu/')

for infile in glob.glob('*.png'):
    try:
        im = Image.open(infile)
        imgwidth, imgheight = im.size
        im1box = [(0, 0, imgwidth/2, imgheight/2), (imgwidth/2, 0, imgwidth, imgheight/2), (0, imgheight/2, imgwidth/2, imgheight), (imgwidth/2, imgheight/2, imgwidth, imgheight)]
        idx = 0
        for box in im1box:
            try:
                thumb=im.crop(box)
                print(str(os.getcwd()))
                outfile = str(os.getcwd()) + '/test_processed/' + str(infile).split('.')[0] + str(idx) + "_single.png"
                thumb.save(outfile, "PNG")
                print('image saved')
                idx+=1
            except IOError:
                print("cannot create thumbnail for '%s'" % infile)
    except IOError:
        print('error occured')

        