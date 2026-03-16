# multithreaded-web-crawler-benchmark

This project measures the performance of a multithreaded web crawler in Python.

## Overview

The program crawls multiple URLs and measures the elapsed time while changing the number of threads.

The result is visualized using matplotlib.

## Technologies Used

- Python
- requests
- concurrent.futures (ThreadPoolExecutor)
- matplotlib

## How it Works

1. A list of URLs is prepared.
2. The crawler fetches each page using multiple threads.
3. The number of threads is increased from 1 to 15.
4. The elapsed time is recorded.
5. The results are visualized in a graph.

## Example Output

The graph shows the relationship between:

- Thread count
- Elapsed crawling time

## Purpose

This project demonstrates:

- Multithreading in Python
- Web crawling using requests
- Performance benchmarking
- Data visualization
