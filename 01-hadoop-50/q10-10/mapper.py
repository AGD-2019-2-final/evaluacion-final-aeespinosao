import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    
    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:
        line = line.strip()
        key,arr = line.split()

        arr = arr.strip()
        arr = arr.split(',')
        for i in arr:
            sys.stdout.write("{}\t{}\t{}\n".format(i+str(float(key)/100),i, key))