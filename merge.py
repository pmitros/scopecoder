'''
Merge aligned images picking pixels from images where we have maximum contrast
'''

import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from alnumsort import sort_nicely

a = []


def update_image(combined_image, combined_lap, new_image):
    lap = cv2.Laplacian(new_image, cv2.CV_64F)
    lap = np.sum(abs(lap), axis=2)
    lap = cv2.blur(lap, (700, 200))
    a.append(lap[100][500])

    mask = (lap < combined_lap)*1.0

    mask = np.array(mask * 255, dtype=np.uint8)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    mask = cv2.medianBlur(mask, 5)

    source_cv = cv2.bitwise_and(combined_image, combined_image, mask=mask)
    im2_cv = cv2.bitwise_and(new_image, new_image, mask=cv2.bitwise_not(mask))

    out = cv2.add(source_cv, im2_cv)
    lap = lap * (mask < 0.5) + combined_lap * (mask > 0.5)
    return out, lap

files = os.listdir('aligned')
sort_nicely(files)
im1 = cv2.imread('aligned/P5150010-138.JPG')
lap1 = cv2.Laplacian(im1, cv2.CV_64F)
lap1 = np.sum(lap1, axis=2)
lap1 = cv2.blur(abs(lap1), (10, 10))

im2 = cv2.imread('aligned/P5150010-115.JPG')

out, lap = update_image(im1, lap1, im2)

# writer = highgui.cvCreateVideoWriter(
#  'movie.avi',
#  highgui.CV_FOURCC('M','P','E','G')
# )

for file in files:
    print file
    im2 = cv2.imread('aligned/'+file)
    print file
    # cv2.imshow('Old image', out)
    out, lap = update_image(out, lap, im2)
    print np.max(lap)
    # cv2.imshow('New image',out)
    # cv2.imshow('Source image',im2)
    # cv2.waitKey(0)


# cv2.imshow('New image',out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.plot(a)
plt.show()
