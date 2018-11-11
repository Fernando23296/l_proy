
def nombre_archivo(na):
        punto = na.find(".")
        b = ''
        for i in range(0, punto):
                b += str(na[i])
        return b
