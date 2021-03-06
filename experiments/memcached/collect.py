#!/usr/bin/env python
import re
import os
from core import collect


def main():
    res_path = os.environ['PROJ_ROOT'] + '/results/memcached/raw.csv'
    full_output_file = os.environ['DATA_PATH'] + "/results/memcached/memcached.log"

    # reshape log file for per-line collection
    with open(full_output_file, 'r') as f:
        old = f.readlines()
        new = old[:]
        for i, l in enumerate(old):
            if l.startswith('Total Statistics'):
                new[i + 3] = 'TotalStatistics' + new[i + 3]
    with open(full_output_file, 'w') as f:
        for s in new:
            f.write("%s" % s)

    collect.collect(
        "memcached",
        user_parameters={
            "num_clients": ["input:", lambda l: collect.get_int_from_string(l)],
            "tput": ["TPS: ", lambda l: float(l.split('TPS: ')[1].split()[0])],
            "lat": ["TotalStatisticsGlobal", lambda l: float(l.split()[8].split()[0])],
        },
        result_file=res_path
    )
