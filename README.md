# Engineer's guide to Data Analysis
This repository contains the demos of the "Engineer's guide to data analysis" presentation.

To run the demos:
```
docker-compose up -d
python peak_erasure.py
python counters-vs-guages.py
python generate_mixed_gauge.py &
python generate_mixed_metric.py &
```

The first two scripts work by generating a timeseries and sending it to Carbon and can 7 days of metrics in a few seconds. The `generate_mixed_*.py` scripts work by sending generated metrics to StatsD which doesn't support timestamps on metric packets, so it must run in real-time. This means you need to leave the scripts running in the background for some time - I may simulate StatsD at some point in the future to speed things up but currently it's not annoying enough.

## License
All the material in this repository is under the MIT license. Enjoy.