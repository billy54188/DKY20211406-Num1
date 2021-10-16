import matplotlib.pyplot as plt#用于显示图片
import matplotlib.image as mping#用于读取图片

a=mping.imread('abc.BMP')#读取和代码同一目录下的图片
print(a)
b=a[0]
import pylab

plt.imshow(b)
pylab.show()