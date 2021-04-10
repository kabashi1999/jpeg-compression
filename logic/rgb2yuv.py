import numpy as np

def rgb2yuv(image):
    if(image.shape[2]==4):
        image = image[:, :, :-1]
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = image.dot(xform.T)
    ycbcr[:,:,[1,2]] += 128
    return np.int16(ycbcr)
