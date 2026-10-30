import cv2
# from google.colab.patches import cv2_imshow

image = cv2.imread("gedungpnl.jpeg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

cv2.imshow("Hasil Gambar" ,image)
cv2.waitKey(0) 
cv2.imshow("Hasil Gambar RGB" ,image_rgb)
cv2.waitKey(0) 
cv2.imshow("Hasil Gambar HSV" ,image_hsv)
cv2.waitKey(0) 
cv2.imshow("Hasil Gambar GRAY" ,image_gray)
cv2.waitKey(0) 
cv2.imshow("Hasil Gambar LAB" ,image_lab)

# WAJIB tambahkan dua baris ini di bawahnya agar jendela gambar tidak langsung tertutup
cv2.waitKey(0) 
cv2.destroyAllWindows()