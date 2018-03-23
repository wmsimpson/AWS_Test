import re

f = open('AWStest.csv', 'r')

for line in f.readlines():
    line = line.strip()
    line.split('[a-zA-Z][^A-Z]*')
    print(re.findall('[A-Z][^A-Z]*', line))

    # parts = line.split('[a-zA-Z][^A-Z]*')
    #
    # for part in parts:
    #     print(part)