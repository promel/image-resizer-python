from PIL import Image
from resizeimage import resizeimage
from os import walk

for (dirpath, dirnames, filenames) in walk('./old--images'):
    for filename in filenames:
        path = dirpath + '/' + filename
        with open(path, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [578 , 575])
                cover.save('new-images/' + filename, image.format)