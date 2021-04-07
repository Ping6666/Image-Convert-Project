import os
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
PicPathBase = "PATH"

counter = 0
for dirPath, dirNames, fileNames in os.walk(PicPathBase):
    imageList, fName, fLen = [], '', 0
    for i, f in enumerate(fileNames):
        # print(os.path.join(dirPath, f))
        if i == 0:
            fName = f
        if ('.jpg' or '.png') in fName:
            inputImage = Image.open(os.path.join(dirPath, f))
            inputImage = inputImage.convert('RGB')
            imageList.append(inputImage)
            fLen += 1
    if len(imageList) != 0:
        imageList.pop(0)
        if ('.jpg' or '.png') in fName:
            inputImageNew = Image.open(os.path.join(dirPath, fName))
            inputImageNew = inputImageNew.convert('RGB')
            inputImageNew.save(PicPathBase + '/' + 'BookName' +
                               str('%02d' % counter) + '.pdf',
                               save_all=True,
                               append_images=imageList)
            if len(imageList) + 1 != fLen:
                print('wrong!!!!')
            counter += 1
