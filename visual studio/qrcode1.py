""" import qrcode
img = qrcode.make("this is qrcode in python")
img.save("image.jpg") """

#
import cv2
qr_img = cv2.imread("image.jpg")
qr_det = cv2.QRCodeDetector()
val, pts, st_code = qr_det.detectAndDecode(qr_img)
print("Information:", val)