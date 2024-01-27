'''import qrcode
img=qrcode.make("ok google")
img.save("image1.jpg")
'''
import cv2
qr_img=cv2.imread("image.jpg")
qr_det=cv2.QRCodeDetector()
val,pts,st_code=qr_det.detectAndDecode(qr_img)
print("Message: ",val)