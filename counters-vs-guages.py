#!/usr/bin/python
import socket
import time
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2003))

interval = 1
now = int(time.time())
start = now - 3600*24*7
offset = start % interval


def metric(t):
    if (t - offset) % (interval*random.randint(55, 65)) == 0:
        return 100 + random.random()*50
    else:
        return 0


counter = 0
for t in range(start, now, interval):
    gauge = metric(t)
    counter += gauge
    s.send('%s %d %d\n' % ('simulation.low_res.counter', counter, t))
    s.send('%s %d %d\n' % ('simulation.low_res.counter_last', counter, t))
    s.send('%s %d %d\n' % ('simulation.low_res.gauge', gauge, t))
    s.send('%s %d %d\n' % ('simulation.high_res.gauge', gauge, t))

s.close()
