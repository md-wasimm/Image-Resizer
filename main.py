import cv2

# Configurable Parameters
source = 'wasim.jpg'
destination = 'resized.png'
scale_percent = 50

img = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", img)

# Calculate the 50 percent of original dimensions
new_width = int(img.shape[1] * scale_percent / 100)
new_height = int(img.shape[0] * scale_percent / 100)

# Resize image
output = cv2.resize(img, (new_width, new_height))

cv2.imwrite(destination, output)
cv2.waitKey(0)