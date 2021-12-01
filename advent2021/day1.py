import sys
import time

def readdepths(file):
    depths = []
    with open(file, 'r', newline='', encoding='utf-8') as f:
        depths = [int(line)for line in f]
    return depths

def countdepthincreases(depths):
    t0 = time.perf_counter()
    slice0 = depths[:-1]
    slice1 = depths[1:]        
    zipped = [1 for (l,r) in zip(slice0, slice1) if r>l]
    t1 = time.perf_counter()
    print(f"Counted depth increases in {t1 - t0:0.4f} seconds")
    return len(zipped)

def main():
    print('----------- day1 -----------')

if __name__ == '__main__':
    sys.exit(main())