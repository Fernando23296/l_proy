import csv
import numpy as np
a = np.empty((2, 3))
#2 = numero de filas, 3= numero de columnas
for i in range(0, 2):
    for j in range(0, 3):
        a[i][j] = np.random.normal()
print(a)

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, 2):
        for j in range(0, 3):
            
            #employee_writer.writerow([2, 'Accounting', 'November'])
            employee_writer.writerow(['numero', a[i][j], 'November'])
  
