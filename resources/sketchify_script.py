import cv2
import numpy as np
from matplotlib import pyplot as plt
import os


############# Script copied from sketchify_script.ipynb iPython notebook##############

########################################################################
############################  Parameters ###############################



# Where A/ and B/ should be.
dataset_loc = './'

# Where the cartoonset is
cartoonset_loc = dataset_loc + 'cartoonset/'

## A input -- The location of the "train" data-- the edges.
A_loc = dataset_loc + 'A/'
## B input -- The location of the "label" data-- the colorized images.
B_loc = dataset_loc + 'B/'

train_loc = 'train/'
val_loc = 'val/'
test_loc = 'test/'
groups = [train_loc, val_loc, test_loc]

# Group counts
TRAIN_COUNT = 1000
VAL_COUNT = 100
TEST_COUNT = 100

# "Indices" of the data, when the files are alphabetized.
train_indices = [i for i in range(TRAIN_COUNT)]
val_indices = [i for i in range(TRAIN_COUNT, TRAIN_COUNT + VAL_COUNT)]
test_indices = [i for i in range(TRAIN_COUNT + VAL_COUNT, TRAIN_COUNT + VAL_COUNT + TEST_COUNT)]


if not os.path.isdir(dataset_loc + B_loc):
    os.makedirs(dataset_loc + B_loc)

for group in groups:
    if not os.path.isdir(dataset_loc + B_loc + group):
        os.makedirs(dataset_loc + B_loc + group)

if not os.path.isdir(dataset_loc + A_loc):
    os.makedirs(dataset_loc + A_loc)

for group in groups:
    if not os.path.isdir(dataset_loc + A_loc + group):
        os.makedirs(dataset_loc + A_loc + group)

########################################################################
#####################  Pull into A/ and B/  ############################

# Set png_files to be just the png images.
for root, dirs_root, files in os.walk(cartoonset_loc):
    png_files = [img for img in files if '.png' in img]

# Train files
for i in range(TRAIN_COUNT):
    source = cartoonset_loc + '/' + png_files[i]
    destination = A_loc + train_loc + png_files[i]
    os.popen('cp {0} {1}'.format(source, destination))

# Val files
for i in range(TRAIN_COUNT, TRAIN_COUNT + VAL_COUNT):
    source = cartoonset_loc + '/' + png_files[i]
    destination = A_loc + val_loc + png_files[i]
    os.popen('cp {0} {1}'.format(source, destination))

# Test files
for i in range(TRAIN_COUNT + VAL_COUNT, TRAIN_COUNT + VAL_COUNT + TEST_COUNT):
    source = cartoonset_loc + '/' + png_files[i]
    destination = A_loc + test_loc + png_files[i]
    os.popen('cp {0} {1}'.format(source, destination))





########################################################################
#############################  Script  #################################

def img_to_sketch(img_name_in, img_name_out):
    img = cv2.imread(img_name_in)
    edges = cv2.Canny(img,500,500)
    plt.imsave(img_name_out, edges, cmap='binary')
    return




# For each image set (group)
for group in groups:
    # Walk the files within the group
    for root, dirs_root, files_root in os.walk(A_loc + group):
        # For each file, sketchify and put it in B/group/
        for filename in files_root:
            if 'png' in filename:
                img_name_in = A_loc + group + filename
                img_name_out = B_loc + group + filename
                img_to_sketch(img_name_in, img_name_out)
