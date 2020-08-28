import argparse

def verify():


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file_path', default='./fol/simplified_mnist10x10.py')
    parser.add_argument('--file_format', default='python')
    parser.add_argument('--dest_path', default='./result/')

    config = parser.parse_args()

    verify(config.file_path, config.file_format, config.dest_path)

if __name__ == '__main__':
    main()
