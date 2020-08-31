def convert_line_python(line):
    new_line = 's.add(' + line + ')\n'

    return new_line

def txt_prop_converter_python(prop_path, dest_path):
    prop_file = open(prop_path, 'r')
    converted_file = open(dest_path, 'w')

    while True:
        line = prop_file.readline().strip('\n')
        if not line:
            break

        converted_file.write(convert_line_python(line))

    prop_file.close()
