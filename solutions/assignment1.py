# This is an empty python file
# where you have to add your code to
# read the content of the 3 qrcodes
# provided and print them using python
# and _______, _____ libraries!
# 
# Good Luck!!!

import os
import cv2

wd = os.getcwd()
path = wd+'/qrcodes'
qrcodes = os.listdir(path)

d = cv2.QRCodeDetector()

for qrcode in qrcodes:
    val, _, _ = d.detectAndDecode(cv2.imread(path + '/' + qrcode))
    print("Decoded text is: ", val)