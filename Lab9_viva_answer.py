
# Apply the threshold
_ , thresholded_image = cv2.threshold(img_grey, 200, 255, cv2.THRESH_BINARY)

# Display Thresholded image
plt.imshow(cv2.cvtColor(thresholded_image, 4))
plt.axis("on")
plt.show()

# https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html




# Apply the threshold
_ , thresholded_image = cv2.threshold(img_grey, 200, 255, cv2.THRESH_BINARY_INV)

# Display Threshold image
plt.imshow(cv2.cvtColor(thresholded_image, 4))
plt.axis("on")
plt.show()





# Edge Detection
edges = cv2.Canny(img_grey, 30, 150)

# Display Edges in the image
plt.imshow(cv2.cvtColor(edges, 4))
plt.axis("on")
plt.show()





# https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
# https://www.youtube.com/watch?v=zvqZ67XOAMQ&ab_channel=BleedAIExtras
# Contours

# Make a copy of the original image so it won’t be corrupted during drawing
image_copy   = img_grey.copy()

_ , thresholded_image = cv2.threshold(image_copy, 200, 255, cv2.THRESH_BINARY_INV)

# Detect Contours
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw the detected contours, -1 means draw all detected contours
cv2.drawContours(img , contours, -1 , (0,255,0), 3)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("on")
plt.show()


print('Total Shapes present in image are: {}'.format(len(contours)))



img = cv2.imread("o5a4b1A.jpg", 1)
img_grey = cv2.imread("o5a4b1A.jpg", 0)
plt.imshow(cv2.cvtColor(img_grey, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
# Apply the threshold
_ , thresholded_image = cv2.threshold(img_grey, 220, 255, cv2.THRESH_BINARY)

# Display Thresholded image
plt.imshow(cv2.cvtColor(thresholded_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

# Edge Detection
edges = cv2.Canny(img_grey, 30, 150)

# Display Edges in the image
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
image_copy   = img_grey.copy()

_ , thresholded_image = cv2.threshold(image_copy, 220, 255, cv2.THRESH_BINARY_INV)

# Detect Contours
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Draw the detected contours, -1 means draw all detected contours
cv2.drawContours(img , contours, -1 , (0,255,0), 3)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
