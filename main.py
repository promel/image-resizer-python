import os
from PIL import Image
from resizeimage import resizeimage
from os import walk

oldDir ='/'
newDir = 'new-images/'
isExist = os.path.exists(newDir)
if not isExist:
    os.mkdir(newDir)

for (dirpath, dirnames, filenames) in walk(oldDir):
    for filename in filenames:
        path = dirpath + '/' + filename
        with open(path, 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [578 , 575])
                cover.save(newDir + filename, image.format)