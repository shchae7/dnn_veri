import sys
sys.path.append('../')

from utils.readNNet import readNNet


def nnet_converter_python(file_path, dest_path):
    # Get nnet info
    weights, biases, numLayers, layerSizes = readNNet(file_path)

    # Total num of Variables
    numNodes = 0
    for i in range(0, numLayers + 1):
        numNodes  += layerSizes[i]

    fol_file = open(dest_path, 'w')
    fol_file.write('from z3 import *\n\n')

    for i in range(0, numNodes):
        fol_file.write('x' + str(i) + ' = Real(\'x' + str(i) + '\')\n') # Python API: x0 = Reals('x0') SMT-LIB: (declare-const x0 Real)
    fol_file.write('\n')

    fol_file.write('s = Solver()\n\n')

    test_file = open('test.txt', 'w')
    passedNodes = layerSizes[0]
    for i in range(1, numLayers + 1):
        for j in range(0, layerSizes[i]):
            eq = 'x' + str(passedNodes + j) + ' == '
            for k in range(0, layerSizes[i - 1]):
                if k == layerSizes[i - 1] - 1:
                    eq += (str(weights[i - 1][j][k]) + ' * x' + str(passedNodes - layerSizes[i - 1] + k))
                else:
                    eq += (str(weights[i - 1][j][k]) + ' * x' + str(passedNodes - layerSizes[i - 1] + k) + ' + ')
            print(eq + '\n', file = test_file)
        passedNodes += layerSizes[i - 1]

    fol_file.write('s.add()\n')

    fol_file.write('print(s.check())\n')
    fol_file.write('print(s.model())\n')

    fol_file.close()


def nnet_converter_smt_lib(file_path, dest_path):
    # Converting to SMT-LIB variant FOL formulae
    print('not implemented yet')
