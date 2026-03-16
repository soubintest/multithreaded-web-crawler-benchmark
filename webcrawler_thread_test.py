import requests
import time
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

def crawl(url):
  try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
  except requests.exceptions.RequestException as e:
        print(f"Error: {url} -> {e}")
   
        return None
#input
urls=[
    "https://numpy.org/doc/stable/",
    "https://numpy.org/ja/",
    "https://numpy.org/doc/stable/building/index.html",
    "https://numpy.org/doc/stable/dev/index.html",
    "https://numpy.org/doc/stable/release.html",
    "https://numpy.org/numpy-tutorials/",
    "https://numpy.org/numpy-tutorials/mooreslaw-tutorial/",
    "https://numpy.org/numpy-tutorials/tutorial-deep-learning-on-mnist/",
    "https://numpy.org/numpy-tutorials/tutorial-x-ray-image-processing/",
    "https://numpy.org/numpy-tutorials/tutorial-static-equilibrium/"
]

#process
def main():
    thread_counts = []
    times = []
    for i in range(1, 16):
        t1 = time.time()
        with ThreadPoolExecutor(max_workers=i) as executor:
            results = list(executor.map(crawl, urls))
        t2 = time.time()
        elapsed_time = t2 - t1
        thread_counts.append(i)
        times.append(elapsed_time)

    # output
    plt.plot(thread_counts, times, marker="o")
    plt.xlabel("Thread count")
    plt.ylabel("Elapsed time (s)")
    plt.title("Thread count vs Elapsed time")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()




