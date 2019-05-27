#происходит построчное чтение файла в цикле
def read_epc():
    f = open('epc.txt', 'r')
    for line in f:
        epc0 = str(line)
        break
    f.close()
    epc = epc0.split()
    return epc
