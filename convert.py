import argparse

from src.nnet_converter import *

def convert(file_path, file_format, dest_path, variant):
    if file_format == 'nnet':
        if variant == 'python':
            nnet_converter_python(file_path, dest_path + '.py')
        else:
            nnet_converter_smt_lib(file_path, dest_path + '.smt')

    elif file_format == 'tf':
        print('not provided yet')
    else:
        print('not provided yet')

    print('file ' + file_path + ' converted at ' + dest_path)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file_path', default='./nnet/simplified_mnist10x10.nnet')
    parser.add_argument('--file_format', default='nnet')
    parser.add_argument('--dest_path', default='./fol/simplified_mnist10x10')
    parser.add_argument('--variant', default='python')

    config = parser.parse_args()


    convert(config.file_path, config.file_format, config.dest_path, config.variant)

if __name__ == '__main__':
    main()
