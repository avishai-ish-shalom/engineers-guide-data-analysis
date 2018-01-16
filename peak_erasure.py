#!/usr/bin/python

import socket
import time
import random


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2003))

interval = 10
now = int(time.time())
start = now - 3600*24*7
offset = start % interval


def metric(t):
    if (t - offset) % (interval*random.randint(40, 50)) == 0:
        return 300 + random.random()*100
    else:
        return random.random()*100

for t in range(start, now, interval):
    s.send('%s %f %d\n' % ('simulation.peak_erasure', metric(t), t))

s.close()
