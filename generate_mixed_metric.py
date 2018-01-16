#!/usr/bin/python

import statsd
import time
import random


base_value1 = 1000
base_value2 = 100
interval = 10


def rand_value(v):
    return v + random.random()*v*0.2

s = statsd.StatsClient('localhost', 8125, prefix='simulation')


def send(m, value):
    s.timing('mixed.' + m, value)
    s.timing('mixed.both', value)


while True:
    start = time.time()
    for _ in range(3):
        c = random.choice(['one', 'two', 'both'])
        if c == 'both':
            send('ok', rand_value(base_value1))
            time.sleep(interval * random.random() * 0.1)
            send('err', rand_value(base_value2))
        elif c == 'one':
            send('ok', rand_value(base_value1))
        else:
            send('err', rand_value(base_value2))

    sleep_time = interval - time.time() + start
    if sleep_time > 0:
        time.sleep(sleep_time)
