file = 'learning_python.txt'
with open(file) as f:
    contents = f.readlines()
    # print(contents)

    for line in contents:
        line = str(line)

        b = line.replace('Python', 'C')

        print(b)

        # line.replace('Python', 'C')
    # print(contents)


with open('programming.txt', 'a') as fb:
    fb.write('hello!\n')