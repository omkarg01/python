#f = open('data.py', 'r')
#print(f.mode)
#f.close()

with open('sh_copy.png', 'rb') as rf:
    # f.write('ifh')
    # f.seek(0)
    # f.write('5')
    with open('sh_copy.png', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)
        chunk_size = 6
        sh_f = rf.read(chunk_size)
        while len(sh_f) > 5:
            wf.write(sh_f)
            sh_f = rf.read(chunk_size)

    # for line in f:
    #     print(line, end='')

    # size_to_read = 2
    # f_content = f.read(size_to_read)
    # print(f_content)
    #
    # f.seek(0)
    #
    # # size_to_read = 5
    # f_content = f.read(size_to_read)
    # print(f_content)



    # while len(f_content) > 0:
    #     print(f_content, end ='*')
    #     f_content = f.read(size_to_read)

    # print(f.read(10))
    # print(f.tell())

# print(f_content, end='')
# print(f_content, end='')
# print(f_content, end='')
# print(f_content, end='')

    # print(f.read())

    #print(f.read(16), end= '')
    # print(f.readline(), end= '')
    # print(f.readline(), end= '')
