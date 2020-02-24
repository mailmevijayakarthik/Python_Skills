with open('myfile.txt', 'rb') as infile, with open('outfile.txt', 'wb') as outfile:
    for lineno, line in enumerate(infile):
        if lineno % 2 == 0:
            line = line + 'S'
        outfile.write(line)