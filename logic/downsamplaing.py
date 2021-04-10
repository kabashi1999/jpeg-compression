import numpy as np

def downsamplaing(image):
    image = np.asarray(image)
    downsampled= image
    y = image.shape[1]
    x = image.shape[0]
    for i in range(x):
        for j in range(y):

            print()
