from abc import ABC, abstractmethod

import sys
sys.path.append('../')
from utils.readNNet import readNNet

# Input Format : [d, i] (d: depth, i: index)

class Component(ABC):
    def __init__(self, input_num, output_num):  # Take number of inputs and outputs as input
        self.input_num = input_num
        self.output_num = output_num

    @abstractmethod
    def print_info(self):
        print('Number of inputs: ' + str(self.input_num))
        print('Number of outputs: ' + str(self.output_num))

    @abstractmethod
    def encode(self):
        pass


class Network(Component):
    def __init__(self, input_num, output_num, weights, biases, numLayers, layerSizes, inputMins, inputMaxes):
        super().__init__(input_num, output_num)

        # Additional Network Info
        self.weights = weights
        self.biases = biases
        self.numLayers = numLayers
        self.layerSizes = layerSizes

        # For consideration --> Specific only to NNet format?
        self.inputMins = inputMins
        self.inputMaxes = inputMaxes

        self.layers = [Layer(layerSizes[i], layerSizes[i + 1] , weights[i], biases[i], i + 1) for i in range(numLayers)] # Depth starting from 1 (depth 0: input layer)


    def print_info(self):
        print('Network Information')
        super().print_info()
        print(self.numLayers)


    def encode(self):
        print('Encoding Network')
        for i in range(self.numLayers):
            self.layers[i].encode()



class Layer(Component):
    def __init__(self, input_num, output_num, weight, bias, d):
        super().__init__(input_num, output_num)
        self.weight = weight
        self.bias = bias
        self.depth = d

        self.nodes = [Node(input_num, 1, weight[i], bias[i], d, i) for i in range(output_num)]


    def print_info(self):
        print(str(self.depth) + 'th Layer Information')
        super().print_info()


    def encode(self):
        print('Encoding ' + str(self.depth) + 'th Layer')
        for i in range(self.output_num):
            self.nodes[i].encode()



class Node(Component):
    def __init__(self, input_num, output_num, weight, bias, d, i):
        super().__init__(input_num, output_num)
        self.weight = weight
        self.bias = bias
        self.depth = d
        self.index = i

        self.fol = ''


    def print_info(self):
        print(str(self.index) + 'th Node at ' + str(self.depth) + 'th Layer Information')
        super().print_info()


    def encode(self): # z3 solver dependent (for now) Only assuming ReLU activation function
        print('Encoding Node')
        self.fol += 'x' + str(self.depth) + '_' + str(self.index) + ''
        print('x' + str(self.depth) + '_' + str(self.index) + ' == ')

        for i in range(self.input_num):
            print(str(self.weight[i]) + ' * ' + 'x' + str(self.depth - 1) + '_' + str(i))


if __name__ == '__main__':
    weights, biases, numLayers, layerSizes, inputMins, inputMaxes = readNNet('./resources/nnet/5_mnist10x10.nnet')

    network = Network(layerSizes[0], layerSizes[-1], weights, biases, numLayers, layerSizes, inputMins, inputMaxes)

    network.encode()
