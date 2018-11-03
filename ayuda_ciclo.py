from random import *
limite=1
'''
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")
'''
count=1

l=[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
def limpio(l):
    tam=len(l)
    a=[]
    for i in range(0,tam):
        if(l[i]!=None):
            a.append(l[i])
    return a


def existencia_cero(l):
    tam = len(l)
    a = 0
    for i in range(0, tam):
        if(l[i] == None):
            a=a+1
    if (tam==a):
        return True
    else:
        return False

def rellenador(l,ancho,largo):
    tam=len(l)
    largo=int(largo/12)
    ancho=int(ancho/2)
    for i in range(1,tam):
        if (l[i]==[]):
            relleno=[ancho,largo*i]
            l[i].append(relleno)
        else:
            pass
    return l


ll = [[[129, 7]], [[129, 142]], [], [], [], [], [[363, 479]], [[363, 614], [361, 569]], [[361, 703], [361, 661]], [
    [355, 763], [389, 720], [311, 720]], [[389, 855], [311, 855], [343, 814], [263, 814]], [[343, 946], [263, 946]]]

#print(rellenador(ll,622,952))


'''
-  79
____
0
343,77
0
263,77
-  158
____
1
389,65
1
311,65
1
343,24
1
263,24
-  237
____
2
355,52
2
389,9
2
311,9
-  316
____
3
361,71
3
361,29
-  395
____
4
363,61
4
361,16
-  474
____
5
363,5
-  553
____
-  632
____
-  711
____
-  790
____
-  869
____
10
129,63
-  948
____
11
129,7
-  1027
____
ll = [[[129, 7]], [[129, 142]], [], [], [], [], [[363, 479]], [[363, 614], [361, 569]], [[361, 703], [361, 661]], [
    [355, 763], [389, 720], [311, 720]], [[389, 855], [311, 855], [343, 814], [263, 814]], [[343, 946], [263, 946]]]

[[[129, 7]], [[129, 142]], [[622, 158]], [[622, 237]], [[622, 316]], [[622, 395]], [[363, 479]], [[363,614], [361, 569]], [[361, 703], [361, 661]], [[355, 763], [389, 720], [311, 720]], [[389, 855], [311, 855], [343, 814], [263, 814]], [[343, 946], [263, 946]]]


[[622, 158]], [[622, 237]], [[622, 316]], [[622, 395]]
'''



lll = [[[129, 7]], [[129, 142]], [[311, 158]], [[311, 237]], [[311, 316]], [[311, 395]], [[363, 479]], [[363, 614], [361, 569]], [
    [361, 703], [361, 661]], [[355, 763], [389, 720], [311, 720]], [[389, 855], [311, 855], [343, 814], [263, 814]], [[343, 946], [263, 946]]]
def seleccionador(l):
    a=[]
    tam=len(l)
    for i in range(1,tam):
        tam1=(len(l[i])-1)
        
        a.append(l[i][randint(0, tam1)])
    return a
print(seleccionador(lll))
