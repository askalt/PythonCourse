import numpy as np
from threading import Thread
from multiprocessing import Process
import time


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def slow_task():
    fib(32)


def execute_sequentially(task, times):
    for _ in range(times):
        task()


def execute_with_threads(task, times):
    workers = []
    for _ in range(times):
        workers.append(Thread(target=task))
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()


def execute_with_processes(task, times):
    workers = []
    for _ in range(times):
        workers.append(Process(target=task))
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()


def bench(name, execute, task, cnt):
    times = []
    for _ in range(7):
        before = time.time()
        execute(task, cnt)
        end = time.time()
        times.append(end - before)
    print(f"{name}: mean = {np.mean(times)}, std = {np.std(times)}")


if __name__ == "__main__":
    N = 10
    bench("sequential", execute_sequentially, slow_task, N)
    bench("threads", execute_with_threads, slow_task, N)
    bench("processes", execute_with_processes, slow_task, N)
    print()
