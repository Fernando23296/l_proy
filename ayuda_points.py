import pylab as pl

y1 = [0, 1, 2, 3, 4, 5]
y2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

x1 = range(len(y1))
x2 = range(len(y2))

pl.plot(x1, y1, 'go')
pl.plot(x2, y2, 'bo')
pl.show()
