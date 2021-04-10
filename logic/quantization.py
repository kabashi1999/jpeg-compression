import numpy as np

def quantization(image):
    q = np.array([
        [16,11,10,16,24,40,51,61],
        [12,12,14,19,26,58,60,55],
        [14,13,16,24,40,57,69,56],
        [14,17,22,29,51,87,80,62],
        [18,22,37,56,68,109,103,77],
        [24,35,55,64,81,104,113,92],
        [49,64,78,87,103,121,120,101],
        [72,92,95,98,112,100,103,99]
    ])
    margin = image.shape[:2]
    print(image.shape)
    for i in range(0, margin[0], 8):
        for j in range(0, margin[1], 8):
            blockdct = image[i:i + 8, j:j + 8, :]
            image[i:i + 8, j:j + 8, 0] = np.divide(blockdct[:,:,0],q)
            image[i:i + 8, j:j + 8, 1] = np.divide(blockdct[:,:,1],q)
            image[i:i + 8, j:j + 8, 2] = np.divide(blockdct[:,:,2],q)

    return image
   # print(image[:8, :8, 0], "\n")
   # print(image[8:16, 8:16, 0], "\n")
    #print(image[16:24, 16:24, 0])