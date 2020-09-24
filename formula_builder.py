from z3 import *

class Z3File():
    def __init__(self, layerSizes):
        self.inputs = []
        self.variables = []
        self.formulas = []

        self.layerSizes = layerSizes

    def add_inputs(self, variable):
        self.inputs.append(variable)

    def add_variable(self, variable):
        self.variables.append(variable)

    def add_formula(self, formula_info):
        self.formulas.append(formula_info)


    # Solve without file I/O
    def solve(self):
        s = Solver()

        # Declare input variables using list comprehensions
        input_list = [ Real('x_%s_%s' % (self.inputs[i][0], self.inputs[i][1])) for i in range(len(self.inputs)) ]

        # Declare variables using list comprehensions
        x_list = [ Real('x_%s_%s' % (self.variables[i][0], self.variables[i][1])) for i in range(len(self.variables)) ]
        z_list = [ Real('z_%s_%s' % (self.variables[i][0], self.variables[i][1])) for i in range(len(self.variables)) ]

        # Add Sig formulas
        #for i in range(len(self.variables)):
        #    sig_val = 0
        #    for j in range(len(self.formulas[i][0])):
        #        sig_val += formulas[i][0][j] * x_list[]

        #    sig_exp = z_list[i] == sig_val
        #    s.add(sig_exp)

        # For other layers
        for i in range(len(self.variables)):
            if(self.formulas[i][2] == 1): # For the first layer --> takes input as 'input'
                sig_exp = z_list[i] == Sum([self.formulas[i][0][j] * input_list[j] for j in range(len(self.inputs))]) + self.formulas[i][1]

            else:
                sig_exp = z_list[i] == Sum([self.formulas[i][0][j] * x_list[j + self.layerSizes[self.formulas[i][2]]] for j in range(self.formulas[i][3])]) + self.formulas[i][1]
            
            print(sig_exp)

            s.add(sig_exp)


        # Add Or formulas       Assuming ReLU activation function --> Differentiate functions by getting function type as input
        for i in range(len(self.variables)):
            left = And(z_list[i] >= 0, x_list[i] == z_list[i])
            right = And(z_list[i] < 0, x_list[i] == 0)

            val = Or(left, right)
            s.add(val)

        print(s.check())
        print(s.model())
