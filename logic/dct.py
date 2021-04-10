import numpy as np

def dct(image):
    C = np.zeros((8, 8))
    for k in range(8):
        for n in range(8):
            if k == 0:
                C[k, n] = np.sqrt(1 / 8)
            else:
                C[k, n] = np.sqrt(2 / 8) * np.cos((np.pi * k * (1 / 2 + n)) / 8)
    np.set_printoptions(threshold=np.inf)
    margin = image.shape[:2]
    print(image.shape, "this is the image size")
    temp = np.resize(image,[image.shape[0]+(8 - margin[0]%8),image.shape[1]+(8 - margin[1]%8),image.shape[2]])
    margin = temp.shape[:2]
    print("what is going on", margin)
    temp -= 128
    for i in range(0,margin[0],8):
        for j in range(0,margin[1],8):
            blockdct = temp[i:i+8,j:j+8,:]
            temp[i:i + 8, j:j + 8,0] = (C.dot(blockdct[:,:,0])).dot(C.T)
            temp[i:i + 8, j:j + 8, 1] = (C.dot(blockdct[:,:,1])).dot(C.T)
            temp[i:i + 8, j:j + 8, 2] = (C.dot(blockdct[:,:,2])).dot(C.T)
    print(temp.shape)
    return temp

