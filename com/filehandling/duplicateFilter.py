






#   Writing only unique files 

with open('source.loc.txt', "r") as fp:
    lines = fp.readlines()
    destination_lines=[]
    for line in lines:
        if line not in destination_lines:
            destination_lines.append(line)


with open('destination.loc.txt', "w+")as destination:
    destination.write("\n".join(destination_lines))

