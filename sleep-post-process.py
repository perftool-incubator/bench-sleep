#!/usr/bin/env python3
# -*- mode: python; indent-tabs-mode: nil; python-indent-level: 4 -*-
# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import sys
import os
import math
import json
from pathlib import Path

TOOLBOX_HOME = os.environ.get('TOOLBOX_HOME')
if TOOLBOX_HOME is None:
    print("This script requires libraries that are provided by the toolbox project.")
    print("Toolbox can be acquired from https://github.com/perftool-incubator/toolbox and")
    print("then use 'export TOOLBOX_HOME=/path/to/toolbox' so that it can be located.")
    exit(1)
else:
    p = Path(TOOLBOX_HOME) / 'python'
    if not p.exists() or not p.is_dir():
        print("ERROR: <TOOLBOX_HOME>/python ('%s') does not exist!" % (p))
        exit(2)
    sys.path.append(str(p))
from toolbox.cdm_metrics import CDMMetrics

params = {}

class t_global(object):
     args = None

def main():
    metrics = CDMMetrics()

    # In any benchmark post-process script, the metrics generated need to be attributed to a
    # time-period (AKA benchmark-phase).  The period which is used to report an official
    # result for the benchmark is the 'measurement' period.  Other periods that may exist
    # could be "warm-up", "prep", etc.

    iter_sample = {
        'primary-period': "measurement",
        'benchmark': "sleep",
        'periods': [],
        'rickshaw-bench-metric': { 'schema': { 'version': '2021.04.12' } }
        }

    metric_files = []
    iter_sample['primary-metric'] = 'nightmares-sec'
    period = { 'name': 'measurement', 'metric-files': [] }
    file_id = 'measurement'
    desc = {'source' : 'sleep', 'class': 'throughput', 'type': 'nightmares-sec'}
    names = {}
    sleep_start = open("sleep-start.txt").readline().rstrip()
    sleep_stop = open("sleep-stop.txt").readline().rstrip()
    end_ts = int(math.floor(float(sleep_stop) * 1000))
    begin_ts = int(math.floor(float(sleep_start) * 1000))
    sample = {'begin': begin_ts, 'end': end_ts, 'value': 100}
    metrics.log_sample(file_id, desc, names, sample)
    metric_file_name = metrics.finish_samples()
    period['metric-files'].append(metric_file_name)
    iter_sample['periods'].append(period)
    f = open('postprocess/post-process-data.json', 'w')
    f.write(json.dumps(iter_sample))
    f.close()
    return(0)

if __name__ == "__main__":
    exit(main())
