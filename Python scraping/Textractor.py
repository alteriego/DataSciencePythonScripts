import re

textfile = open('regex_sum_206925.txt')
sumlist = []

for line in textfile:
    line = line.rstrip()
    for line in textfile:
        stuff = re.findall('([0-9]+)', line)
        if len(stuff) > 0:
            for item in stuff:
                sumlist.append(int(item))

sumoflist = sum(sumlist)

print "Sum equals", sumoflist
print "And this is the list", sumlist
