import os
from shutil import copy2

def add_properties(file_path, property_path):
    copy2(file_path, "/Users/seunghyunchae/veriDNN/copy2_test.py")

    result_file = open("/Users/seunghyunchae/veriDNN/copy2_test.py", "a")
    prop_file = open(property_path, "r")

    while True:
        line = prop_file.readline().strip('\n')
        if not line:
            break

        result_file.write(line + '\n')
    result_file.write('\n')

    result_file.write('print(s.check())\n')
    result_file.write('print(s.model())\n')



def z3py_verifier(file_path, property_path, dest_path):
    add_properties(file_path, property_path)

    #os.system('python3 ' + file_path + ' > ' + dest_path)
