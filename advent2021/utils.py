import time 

class Timer:
    def __enter__(self):
        self.t0 = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        t1 = time.perf_counter()
        print(f"Timed: {t1 - self.t0:0.4f} seconds")

