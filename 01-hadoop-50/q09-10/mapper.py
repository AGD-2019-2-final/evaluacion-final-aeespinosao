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
        value = int(value)
        sys.stdout.write("{},{},{},{}\n".format(str(value/100), key, date, value))