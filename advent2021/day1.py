import sys
import time

from pathlib import Path
THIS_DIR = Path(__file__).parent

def readdepths(file):
    depths = []
    with open(file, 'r', newline='', encoding='utf-8') as f:
        depths = [int(line)for line in f]
    return depths

def slidingwindows(depths, windowsize = 3):
    slice = depths[:-(windowsize-1)]    
    windows = []
    for i, _ in enumerate(slice):
        w = depths[i:i+windowsize]
        windows.append(sum(w))
    return windows

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
    depths = readdepths(THIS_DIR.parent / 'data/day1_p1.txt')
    print(f'For first ⭐: {countdepthincreases(depths)}')

    windows = slidingwindows(depths)
    print(f'For ⭐⭐: {countdepthincreases(windows)}')

if __name__ == '__main__':
    sys.exit(main())