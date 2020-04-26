import numpy as np

def getcolId(colName):
    """
    Get the number of the column according to the column name, as follows:
    :A - 1
    :B - 2
    ...
    :Z - 26
    :AA - 27
    :AB - 28
    :BA - 53
    :AAA - 703

    """
    abc = [char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

    letters = [char for char in colName]

    id = 0
    for i in range(len(letters)):
        id += pow(26,len(letters)-1-i)*(abc.index(letters[i])+1)
    print(id)
    pass

if __name__ == '__main__':
    getcolId('BAA')
