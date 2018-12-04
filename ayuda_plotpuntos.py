############DEBUG 3
from scipy.ndimage import rotate
import os
from matplotlib import pyplot as plt
vector=[
		[[367, 107], [405, 103], [405, 73], [367, 41]], 
		[[384, 266], [369, 261], [322, 253], [369, 221], [392, 228], [376, 216], [377, 182], [399, 158], [371, 139]], 
		[[337, 386], [339, 379], [362, 344], [386, 332], [365, 294], [373, 307], [319, 319], [379, 295]], 
		[[359, 538], [348, 509], [316, 505],[329, 496], [366, 448], [367, 475], [393, 471], [353, 414], [313, 425]], 
		[[423, 675], [448, 670], [464, 666], [375, 670], [418, 662], [455, 657], [400, 625], [423, 605], [345, 602], [396, 608], [375, 587], [338, 544]], 
		[[427, 814], [411, 814], [382, 814], [378, 814], [506, 810], [526, 810], [507, 798], [446,759], [369, 688], [498, 740], [445, 690], [436, 725], [416, 695], [405, 711], [398, 766]], 
		[[422, 948], [439, 948], [504, 935], [560, 940], [440, 930], [421, 918], [264, 906], [486, 917], [357, 892], [283, 861], [420, 847], [271, 895], [531, 876], [446, 817], [420, 816], [393, 817], [384, 893], [343, 820]], 
		[[354, 1082], [437, 1080], [358, 1071], [499, 1065], [513, 1065], [335, 1031], [430, 1019], [345, 1014], [366, 1013], [362, 1043], [408, 997], [434, 998], [267, 980], [334, 993], [540, 1027], [494, 986], [439, 952], [423, 953], [362, 965], [242, 991]], 
		[[473, 1088], [330, 1088]]
		]

ttitulo_final='todoslospuntos.png'
tamaño=len(vector)
vector_pro=[]
for i in range (0,tamaño):
	#print(vector[i])
	tam_i=len(vector[i])
	print(tam_i)
	#plt.plot(*sum(a, []), marker='o', color='r')
	#plt.show()
	for ii in range (0,tam_i):
		#print(vector[i][ii])
		alfa=vector[i][ii]
		bravo = alfa[::-1]

		vector_pro.append(alfa)
print(vector_pro)
img = plt.imread("ex.png")
#img2 = rotate(img, -270)
fig, ax = plt.subplots()
ax.imshow(img)
lar=len(vector_pro)
x_vector=[]
y_vector=[]
for i in range(0,lar):
	x_vector.append(vector_pro[i][0])
	y_vector.append(vector_pro[i][1])

plt.plot(x_vector,y_vector, marker='o')
#818
#1090
plt.xlim(0, 818)
plt.ylim(0, 1090)
titulo_final='aabbccdd.png'
plt.savefig(titulo_final)
plt.show()


