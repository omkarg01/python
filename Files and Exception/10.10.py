try:
    with open('dogs.txt', 'r') as d:
        print(d.read())

    with open('read.py') as c:
        print(c.read())

except FileNotFoundError:
    pass

with open('moby_dick.txt', encoding='utf-8') as the:
    a = the.read()
    # word = a.split()
    c = a.lower().count('the')
    # c = len(word)
    print(c)

# with open('moby_dick.txt', encoding='utf-8') as f:
#     contents = f.read()
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {'moby_dick'} has about {num_words} words.")


