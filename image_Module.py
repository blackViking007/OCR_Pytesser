import numpy as np
import cv2
from pytesser import *
from espeak import espeak

cap = cv2.VideoCapture(1)

while(True):
	ret, frame = cap.read()
	cv2.imwrite('in_conv.png',frame)
	gray_img = cv2.imread('in_conv.png', 0)
	blur_img = cv2.GaussianBlur(gray_img,(5,5),0)
	ret,thresh2 = cv2.threshold(blur_img,127,255,cv2.THRESH_BINARY)
	cv2.imwrite('im.png',thresh2)
	#cv2.imshow('image', frame)

	in_img = Image.open("im.png")
	text = image_to_string(in_img)
	print "Unprocessed text",text
	cleanedValue =  ''.join([j for j in text if j.isalpha()])
	print "Processed text",cleanedValue
	espeak.synth(cleanedValue)

cap.release()
cv2.destroyAllWindows()