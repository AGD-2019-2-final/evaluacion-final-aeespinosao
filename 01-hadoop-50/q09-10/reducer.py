import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##

    for num, line in enumerate(sys.stdin, start=0):

        ide,key,date,value = line.split(',')
        value = int(value)
        sys.stdout.write("{}\t{}\t{}\n".format(key, date, value))
        if(num==5):
            break