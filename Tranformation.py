import cv2 as cv
import numpy as np

img = cv.imread(r"D:\Space\Space\WhatsApp Image 2022-05-25 at 11.52.29 AM.jpeg")
#rescaling and resizing
def rescaleImg(img,scale = 0.5):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

resized_image1 = rescaleImg(img)
cv.imshow('My Photos',resized_image1)

#Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (resized_image1.shape[1],resized_image1.shape[0])
    return cv.warpAffine(resized_image1,transMat,dimensions)

#-x --> Left
#-y --> Up
#x -->Right
#y -->Down

translated = translate(resized_image1,-100,100)
cv.imshow('Translated',translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height) 
    
    return cv.warpAffine(resized_image1,rotMat,dimensions)

rotated = rotate (resized_image1,45)
cv.imshow('Rotated',rotated)

#Resized
resized = cv.resize(img,(250,250),interpolation = cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Flipping
flip = cv.flip(resized_image1,0)
cv.imshow('Flipped',flip)

#Cropping
cropped = resized_image1[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
