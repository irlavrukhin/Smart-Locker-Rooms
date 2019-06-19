# происходит построчное чтение файла в цикле для случая, когда в файле одно значение
def read_epc():
    f = open('epc.txt', 'r')
    for line in f:
        epc0 = str(line)
        break
    f.close()
    epc = epc0.split()
    return epc


# происходит построчное чтение файла в цикле для случая, когда в файле много значений
# значения передаются в множество
def read_epc_set():
    set_of_epc = set()
    f = open('epc.txt', 'r')
    for line in f:
        epc0 = str(line)
        set_of_epc.add(epc0)
    f.close()
    with open('epc.txt', 'wb'):
        pass
    return set_of_epc


def read_range_of_epc():
    set_of_epc_range = set()
    f = open('epc.txt', 'r')
    for line in f:
        epc0 = str(line)
        set_of_epc_range.add(epc0)
    f.close()
    return set_of_epc_range

