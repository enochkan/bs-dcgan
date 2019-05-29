import os, sys, glob
from PIL import Image, ImageOps

size = 1024, 1024

# def is_grey_scale(img_path):
#     img = Image.open(img_path).convert('RGB')
#     w,h = img.size
#     for i in range(w):
#         for j in range(h):
#             r,g,b = img.getpixel((i,j))
#             if r != g != b: return False
#     return True

mydir = os.getcwd()
imdir = os.chdir(str(mydir)+'/images/' + ''.join(sys.argv[1:]))
os.mkdir(str(mydir)+'/processed/'+''.join(sys.argv[1:]))
cur = 0
for infile in glob.glob('*.jpg'):
    # if not is_grey_scale(infile):
    outfile = str(mydir) + '/processed/' + ''.join(sys.argv[1:]) + '/'+ str(cur) + "_compressed.jpg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            thumb = ImageOps.fit(im, size, Image.ANTIALIAS)
            thumb.save(outfile, "JPEG")
            print('image saved')
            cur+=1
        except IOError:
            print("cannot create thumbnail for '%s'" % infile)
    # else:
    #     continue