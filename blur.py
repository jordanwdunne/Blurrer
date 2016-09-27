import pygame
import os
import sys
from pygame import gfxdraw
from StringIO import StringIO
from PIL import Image
from pygame.locals import*

def evenPixelDivision(width, height, pixelSize):
    if width % pixelSize != 0 or height % pixelSize != 0:
        print "ERROR: New pixel size is not an even multiple of the input image dimensions"
        print width, height
        return False
    return True

def getAverageSurroundingColor(x, y, pixelSize, image):
    rSum = 0
    gSum = 0
    bSum = 0
    aSum = 0

    for row in range(pixelSize):
        for col in range(pixelSize):
            pixelColor = image.get_at((x+int(pixelSize/2), (y+int(pixelSize/2))))
            # print "pixelColor", pixelColor
            rSum += pixelColor[0]
            gSum += pixelColor[1]
            bSum += pixelColor[2]
            aSum += pixelColor[3]

    rAvg = rSum/(pixelSize**2)
    bAvg = bSum/(pixelSize**2)
    gAvg = gSum/(pixelSize**2)
    aAvg = aSum/(pixelSize**2)

    # print rSum, gSum, bSum
    # print rAvg, gAvg, bAvg, aAvg
    return (bAvg, gAvg, rAvg, aAvg)

def blurImage(filename, newPixelSize):
    pygame.init()
    inputImage = pygame.image.load(filename)
    white = (255, 64, 64)

    width = inputImage.get_width()
    height = inputImage.get_height()

    cropArea = (0, 0, width - width % newPixelSize, height - height % newPixelSize)
    croppedImage = inputImage.subsurface(cropArea)

    width = croppedImage.get_width()
    height = croppedImage.get_height()

    newHeight = height / newPixelSize
    newWidth = width / newPixelSize

    for row in range(newWidth):
        for col in range(newHeight):
            replacementColor = getAverageSurroundingColor(row * newPixelSize, col * newPixelSize, newPixelSize, croppedImage)
            if replacementColor[1] != 255:
                print replacementColor
            for subRow in range(newPixelSize):
                for subCol in range(newPixelSize):
                    croppedImage.set_at(((row * newPixelSize + subRow), (col * newPixelSize + subCol)), replacementColor)

    pygame.image.save(croppedImage, str("blurred_" + str(newPixelSize) + "_" + filename))

def printUsage():
    print "Usage:"
    print "python blur [filename.png] [pixelSize]"
    print "Ex. python blur test.png 4"

def main(argv):
    if len(argv) == 0:
        printUsage()
    elif len(argv) == 3:
        if argv[0].lower() == "blur" and isinstance(int(argv[2]), int):
            blurImage(argv[1], int(argv[2]))
    else:
        printUsage()

if __name__ == "__main__":
    main(sys.argv[1:])
