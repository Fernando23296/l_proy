c=24
b=25
a=12

import math


cos_a=((a**2)-(b**2)-(c**2))/(-2*(b*c))
rad_a= math.acos(cos_a)
pi = math.pi
a_angle = 180 * rad_a / pi


cos_b=((b**2)-(a**2)-(c**2))/(-2*(a*c))
rad_b= math.acos(cos_b)
b_angle = 180 * rad_b / pi

c_angle=180-a_angle-b_angle
print(a_angle)
print(b_angle)
print(c_angle)