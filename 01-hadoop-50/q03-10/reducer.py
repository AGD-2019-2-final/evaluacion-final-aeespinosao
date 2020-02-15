import sys
import operator
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
    data=sorted(sys.stdin,key=operator.itemgetter(2))
    for line in data:
            
            sys.stdout.write(line)
            # sys.stdout.write("{}\t{}\n".format(key, val))

           