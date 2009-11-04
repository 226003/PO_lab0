#!/usr/bin/python

import sys

labels = []
values = []

for line in sys.stdin:
    value, label = line.strip().split(' ')
    labels.append(label)
    values.append(int(value))

values = [value * 100 / sum(values) for value in values]

print "http://chart.apis.google.com/chart?cht=p&chd=t:%s&chs=600x300&chl=%s" % ( ','.join(map(str,values)), '|'.join(labels))