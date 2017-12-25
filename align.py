'''
This script will try to align all of the images in the data/
directory, and save them in the 'aligned' directory.
'''

import cv2
import os
import numpy as np


files = os.listdir('data')
base = files[0]
im1 = cv2.imread('data/'+base)
im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

sz = im1.shape
warp_mode = cv2.MOTION_TRANSLATION
warp_matrix = np.eye(2, 3, dtype=np.float32)
number_of_iterations = 5000
termination_eps = 1e-10
criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
            number_of_iterations,  termination_eps)

for file in files:
    print file
    # Define the motion model
    warp_mode = cv2.MOTION_TRANSLATION
    im2 = cv2.imread('data/'+file)
    im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    (cc, warp_matrix) = cv2.findTransformECC(
        im1_gray, im2_gray,
        warp_matrix, warp_mode,
        criteria
    )
    print warp_matrix
    im2_aligned = cv2.warpAffine(
        im2, warp_matrix,
        (sz[1], sz[0]),
        flags=cv2.INTER_LINEAR+cv2.WARP_INVERSE_MAP
    )
    cv2.imwrite("aligned/"+file, im2_aligned)
    lap = cv2.Laplacian(im2, cv2.CV_64F)
    print lap.max()
