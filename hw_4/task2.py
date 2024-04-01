
import numpy as np
import os
import math
import multiprocessing
import time
import functools
import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


logs_path = os.path.join(os.path.dirname(__file__), "artifacts", "task2.log")
logs_f = open(logs_path, "w")


def log(msg):
    logs_f.write(f"[{datetime.datetime.now()}]: {msg}\n")


def integrate(f, a, b, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def worker(f, j, l_cur, r_cur, one_work):
    log(f"worker {j} started")
    return integrate(f, l_cur, r_cur, n_iter=one_work)


def integrate_partition(f, a, b, n_jobs, precision=10000000):
    one_work = (precision + n_jobs - 1) // n_jobs
    one_segment_len = (b - a) / n_jobs

    tasks = []
    for i in range(n_jobs):
        l_cur = a + one_segment_len * i
        r_cur = l_cur + one_segment_len

        tasks.append(functools.partial(worker, f, i, l_cur, r_cur, one_work))
    return tasks


def calculate(executor, n_jobs):
    times = []

    for _ in range(7):
        partition = integrate_partition(math.cos, 0, math.pi / 2, n_jobs)
        futures = []

        before = time.time()
        for part in partition:
            futures.append(executor.submit(part))
        acc = 0
        for future in futures:
            acc += future.result()
        after = time.time()

        assert math.fabs(acc - 1) < 1e-4
        times.append(after - before)
    return times


if __name__ == "__main__":
    for n_jobs in range(1, multiprocessing.cpu_count() * 2):
        print("n_jobs =", n_jobs)
        log(f"n_jobs = {n_jobs}")

        fmt = "{}: mean = {}, std = {}"
        threads_times = calculate(ThreadPoolExecutor(), n_jobs=n_jobs)
        print(fmt.format("threads", np.mean(threads_times),
                         np.std(threads_times)))

        process_times = calculate(ProcessPoolExecutor(), n_jobs=n_jobs)
        print(fmt.format("processes", np.mean(process_times),
                         np.std(process_times)))
