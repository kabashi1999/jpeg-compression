import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import rgb2yuv as f
import downsamplaing as g
import dct as d
import quantization as q
import zigzag as z
import runlength as rl
image = np.asarray(Image.open('../images/ashlad.png'))


convImage = f.rgb2yuv(image)

min = np.amin(convImage)
max = np.amax(convImage)
#print(convImage[:,:,1],np.amax(convImage[:,:,1]))
dctimage = d.dct(convImage)
quantized = q.quantization(dctimage)
yimage,uimage,vimage = z.zigzagcoding(quantized)
starts, lengths, values = rl.rlencoding(yimage)
print(starts,"\n",lengths,"\n",values)



