'''
for i in range(1000):
    if i % 100 == 0:
        print(i)
'''
'''

costs=[]

# print the cost over all data points every 1k iters
data = [[[282,   0,],
         [209,  71],
         [216, 119],
         [187, 207],
         [297, 320],
         [267, 416],
         [229, 519],
         [242, 575],
         [281, 745],
         [282, 915], 1],
        [[409,    0],
         [338,   66],
         [336,  132],
         [284,  264],
         [505,  330],
         [365,  462],
         [334,  528],
         [409,  594],
         [409,  726],
         [282, 915], 0]]
point=data[1][2]
print(point)
'''

def nombre_archivo(na):
        punto=na.find(".")
        b=''
        for i in range(0,punto):
                b+=str(na[i])
        return b

print(nombre_archivo('bruno.jk'))