
import matplotlib.pyplot as plt

inflex_x = [955.60429496, 583.16980415, 173.81825133]
inflex_y=[403.18654089960387, 385.00817304454716, 500.64653539961296]

point_x=[1000, 678.18396024]
point_y=[500, 700.11426059173402]

tam_point=len(point_x)
if (tam_point==1):
	pass
if (tam_point==2):	
	enl_x1=[]
	enl_y1=[]
	enl_x1.append(inflex_x[0])
	enl_y1.append(inflex_y[0])

	enl_x2=[]
	enl_y2=[]
	enl_x2.append(inflex_x[1])
	enl_y2.append(inflex_y[1])


	enl_x3=[]
	enl_y3=[]
	enl_x3.append(inflex_x[1])
	enl_y3.append(inflex_y[1])

	enl_x4=[]
	enl_y4=[]
	enl_x4.append(inflex_x[2])
	enl_y4.append(inflex_y[2])


	#point_x=[1000, 678.18396024]
	#point_y=[500, 154.11426059173402]

	enl_x1.append(point_x[0])
	enl_y1.append(point_y[0])
	enl_x2.append(point_x[0])
	enl_y2.append(point_y[0])


	enl_x3.append(point_x[1])
	enl_y3.append(point_y[1])
	enl_x4.append(point_x[1])
	enl_y4.append(point_y[1])

	point_x1=point_x[0]
	point_x2=point_x[1]
	point_y1=point_x[0]
	point_y2=point_x[1]

	plt.plot(inflex_x, inflex_y, marker = 'o')

	plt.plot(point_x1,point_y1, marker = 'o',color='red')
	plt.plot(point_x2,point_y2, marker = 'o',color='blue')


	point_prueba1=[955,313]

	point_prueba2=[403,237]


	plt.plot(enl_x1,enl_y1, marker = 'o',color='red')
	plt.plot(enl_x2,enl_y2, marker = 'o',color='red')

	plt.plot(enl_x3,enl_y3, marker = 'o',color='red')
	plt.plot(enl_x4,enl_y4, marker = 'o',color='red')

	point_prueba3=[583,313]

	point_prueba4=[385,237]
	#plt.plot(point_prueba3,point_prueba4, marker = 'o')

	plt.show()
