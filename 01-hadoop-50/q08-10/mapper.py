import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:
        line = line.replace('\n','')
        key,date,value = line.split('   ')
        
        sys.stdout.write("{}\t{}\n".format(key, value))
