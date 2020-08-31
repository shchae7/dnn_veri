import argparse

from src.prop_converter import *

def prop_convert(prop_path, prop_format, dest_path, variant):
    if prop_format == 'txt':
        if variant == 'python':
            txt_prop_converter_python(prop_path, dest_path)
        else:
            print('txt prop 2 smt converter not provided yet')
    else:
        print('other prop format not supported yet')

    print('property ' + prop_path + ' converted at ' + dest_path)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--prop_path', default='./resources/properties/test_prop.txt')
    parser.add_argument('--prop_format', default='txt')
    parser.add_argument('--dest_path', default='./fol/properties/test_prop.py')
    parser.add_argument('--variant', default='python')

    config = parser.parse_args()


    prop_convert(config.prop_path, config.prop_format, config.dest_path, config.variant)

if __name__ == '__main__':
    main()
