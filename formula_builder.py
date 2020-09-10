class Z3File():
    def __init__(self):
        self.variables = []
        self.formulas = []

    def add_variable(self, variable):
        self.variables.append(variable)

    def add_formula(self, formula):
        self.formulas.append(formula)

    # Solve without file I/O
    def solve(self):


    # Just in case
    def write_file(self, dest):
        res_file = open(dest, 'w')

        res_file.write('from z3 import *\n\n')

        # Add variables
        for i in range(len(self.variables)):
            res_file.write(self.variables[i] + ' = Real(' + '\'' + self.variables[i] + '\')\n')

        res_file.write('s = Solver()\n\n')

        # Add formulas
        for i in range(len(self.formulas)):
            res_file.write('s.add(' + self.formulas[i] + ')\n')

        res_file.write('\nprint(s.check())\n')
        res_file.write('print(s.model())\n')

        res_file.close()

        print('file written to ' + dest)
