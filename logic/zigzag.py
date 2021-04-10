import numpy as np

def zigzagcoding(image):
    ycodedlist = []
    ucodedlist = []
    vcodedlist = []
    margin = image.shape[:2]
    for i in range(0,margin[0],8):
        for j in range(0,margin[1],8):
            blockdct = image[i:i + 8, j:j + 8, :]
            ycodedlist.append(np.concatenate([np.diagonal(blockdct[:,:,0][::-1,:], i)[::(2*(i % 2)-1)] for i in range(1-blockdct[:,:,0].shape[0], blockdct[:,:,0].shape[0])]))
            ucodedlist.append(np.concatenate([np.diagonal(blockdct[:,:,1][::-1,:], i)[::(2*(i % 2)-1)] for i in range(1-blockdct[:,:,1].shape[0], blockdct[:,:,1].shape[0])]))
            vcodedlist.append(np.concatenate([np.diagonal(blockdct[:,:,2][::-1,:], i)[::(2*(i % 2)-1)] for i in range(1-blockdct[:,:,2].shape[0], blockdct[:,:,2].shape[0])]))

    return ycodedlist,ucodedlist,vcodedlist