import sys
sys.path.append('../')

from utils.readNNet import readNNet


def nnet_converter_python(file_path, dest_path):
    # Get nnet info
    weights, biases, numLayers, layerSizes, inputMins, inputMaxes = readNNet(file_path)

    fol_file = open(dest_path, 'w')
    fol_file.write('from z3 import *\n\n')

    # Total num of Vars
    numNodes = 0
    for i in range(0, numLayers + 1):
        numNodes += layerSizes[i]

    # Var Declartation
    for i in range(0, numNodes):
        fol_file.write('x' + str(i) + ' = Real(\'x' + str(i) + '\')\n') # Python API: x0 = Reals('x0') SMT-LIB: (declare-const x0 Real)
    fol_file.write('\n')

    fol_file.write('s = Solver()\n\n')

    # Network Constraints
    passedNodes = layerSizes[0]
    for i in range(1, numLayers + 1): # Output layer nodes labeled x... as well
        for j in range(0, layerSizes[i]):
            eq = ''
            for k in range(0, layerSizes[i - 1]):
                eq += (str(weights[i - 1][j][k]) + ' * x' + str(passedNodes - layerSizes[i - 1] + k) + ' + ')   # Add weights * previous layer nodes
            eq += (str(biases[i - 1][j]))        # Add bias

            # ReLU activation function -->  (zi >= 0 /\ xi == zi) \/ (zi < 0 /\ xi == 0) /\ (zi == axi-1 + bxi-2 ...)
            index = str(passedNodes + j)
            fol_file.write('z' + index + ' = Real(\'z' + index + '\')\n')
            fol_file.write('s.add(z' + index + ' == ' + eq + ')\n')

            leftconstraint = 'x' + index + '_left = And([z' + index + ' >= 0, x' + index + ' == z' + index + '])'
            fol_file.write(leftconstraint + '\n')

            rightconstraint = 'x' + index + '_right = And([z' + index + ' < 0, x' + index + ' == 0])'
            fol_file.write(rightconstraint + '\n')

            reluconstraint = 'Or([x' + index + '_left, x' + index + '_right])'
            fol_file.write('s.add(' + reluconstraint + ')\n\n')

        passedNodes += layerSizes[i - 1]

    # Input Constraints
    inputSize = weights[0].shape[1]
    for i in range(0, inputSize):
        min_constraint = 'x' + str(i) + ' >= ' + str(inputMins[i])
        max_constraint = 'x' + str(i) + ' <= ' + str(inputMaxes[i])
        fol_file.write('s.add(' + min_constraint + ' , ' + max_constraint + ')\n')
    fol_file.write('\n')

    fol_file.close()


def nnet_converter_smt_lib(file_path, dest_path):
    # Converting to SMT-LIB variant FOL formulae
    print('not implemented yet')
