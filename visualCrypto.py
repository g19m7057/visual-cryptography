import numpy
import cv2
import random
import sys

def monoThresh(image): 
    w, h = image.shape      
    newImage = numpy.zeros((w,h),dtype='int8')+255

    for i in range (w):
        for j in range(h):
            if image[i,j]>128:
                new=255
            else:
                new=0
            newImage[i,j]=new
    return newImage


def splitImage(newImage): 
    w, h = newImage.shape
    image1 = numpy.zeros((2*w,2*h),dtype = 'int8')+255  
    image2 = numpy.zeros((2*w,2*h),dtype = 'int8')+255

    white=['*','*']

    white[0]=numpy.array([[1,0],[0,1]])*255
    white[1]=numpy.array([[0,1],[1,0]])*255

    for i in range(w):
        for j in range(h):
            rand = random.randint(0,1)
            if newImage[i,j]==255:
                image1[2*i:2*i+2,2*j:2*j+2]=white[rand]
                image2[2*i:2*i+2,2*j:2*j+2]=white[rand]
            if newImage[i,j]==0:
                image1[2*i:2*i+2,2*j:2*j+2]= white[rand]
                image2[2*i:2*i+2,2*j:2*j+2]= white[1-rand]
    return image1,image2


def reconstructImage(encoded1,encoded2): 
    if encoded1.shape != encoded2.shape:
        print('image dimensions are different')
    else:
        return numpy.minimum(encoded1,encoded2)


def main():
    p = sys.argv[1]
    
    if (p == 'encode'):
        file = sys.argv[2]
        image = cv2.imread(file,0) 
        newImage = monoThresh(image)
        encoded1,encoded2 = splitImage(newImage)
        cv2.imwrite('encoded1.png',encoded1)
        cv2.imwrite('encoded2.png',encoded2)
        
    if (p == 'decode'):
        img1 = sys.argv[2]
        encoded1 = cv2.imread(img1)
        img2 = sys.argv[3]
        encoded2 = cv2.imread(img2)
        reconstructed = reconstructImage(encoded1,encoded2)
        cv2.imwrite('reconstructed.png',reconstructed)

if __name__ == "__main__":
    main()











                
