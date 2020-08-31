import argparse

from src.z3py_verifier import *

def verify(file_path, property_path, file_format, dest_path):
    if file_format == 'python':
        z3py_verifier(file_path, property_path, dest_path)
    else: # if file_format == 'smt'
        print('not provided yet')

    print(file_path + '\'s ' + property_path + ' verified, result at ' + dest_path)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file_path', default='./fol/dnn/1_mnist10x10.py')
    parser.add_argument('--property_path', default='./fol/properties/test_prop.py')
    parser.add_argument('--file_format', default='python')
    parser.add_argument('--dest_path', default='./result/')

    config = parser.parse_args()


    verify(config.file_path, config.property_path, config.file_format, config.dest_path)

if __name__ == '__main__':
    main()
