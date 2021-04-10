import numpy as np

def rlencoding(image):
    image = np.asarray(image)
    where = np.flatnonzero
    n = len(image)
    starts = np.r_[0, where(~np.isclose(image[1:], image[:-1], equal_nan=True)) + 1]
    lengths = np.diff(np.r_[starts, n])
    values = image[starts]


    return starts, lengths, values
