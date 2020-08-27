import sys
sys.path.append('../')

from utils.readNNet import readNNet


def nnet_converter_python(file_path, dest_path):
    # Get nnet info
    weights, biases, numLayers, layerSizes = readNNet(file_path)

    print(numLayers)
    print(layerSizes)

    # Total num of Variables
    numNodes = 0
    for i in range(0, numLayers + 1):
        numNodes  += layerSizes[i]
    print(numNodes)

    fol_file = open(dest_path, 'w')
    fol_file.write('from z3 import *\n\n')

    for i in range(0, numNodes):
        fol_file.write('x' + str(i) + ' = Reals(x' + str(i) + ')\n') # Python API: x0 = Reals('x0') SMT-LIB: (declare-const x0 Real)

    fol_file.write('s.add()\n')

    fol_file.close()


def nnet_converter_smt_lib(file_path, dest_path):
    # Converting to SMT-LIB variant FOL formulae
    print('not implemented yet')
