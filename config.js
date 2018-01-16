{
  "graphiteHost": "127.0.0.1",
  "graphitePort": 2003,
  "port": 8125,
  "flushInterval": 10000,
  "percentThreshold": [90, 95, 99],
  "histogram": [
    { "metric": "app.latency", "bins": [1, 10, 100, 1000, 10000, 'inf'] }
  ]
}
