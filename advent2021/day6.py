import sys
from pathlib import Path
THIS_DIR = Path(__file__).parent
import time

def closure(seed=8):
    inner_seed = seed
    
    def inner():
        nonlocal inner_seed 
        
        if inner_seed == 0:
            inner_seed = 6
            return inner_seed, closure()
        else: 
            inner_seed -=1
                
        return inner_seed, None
    return inner

def simulate(generations, startingpoints,verbose=False):
    t0 = time.perf_counter()    
    fish = [closure(t) for t in startingpoints]
    for _ in range(generations):
        new_fish = []
        for l in fish:
            timer, newlife = l()
            if verbose: 
                print(timer, end="-")
            if newlife:
                new_fish.append(newlife)
        if verbose: 
            print()
        fish.extend(new_fish)
    t1 = time.perf_counter()
    print(f"Simulation for {generations} gen with {len(startingpoints)} 🐟: {t1 - t0:0.4f} seconds")
    return fish

def buildfishindex(startingpoints):
    fish = {}
    for t in startingpoints:
        if t in fish:
            fish[t] += 1
        else:
            fish[t] = 1 
    return fish

def faster_simulate(generations, startingpoints,verbose=False):
    t0 = time.perf_counter()    
    fishindex = buildfishindex(startingpoints)

    for _ in range(generations):        
        new_index = {t-1:fishindex.get(t,0) for t in range(8,0,-1)}
        new_index[8] = fishindex.get(0,0)        
        new_index[6] += fishindex.get(0,0)
        fishindex = dict(new_index)

    t1 = time.perf_counter()
    print(f"Simulation for {generations} gen with {len(startingpoints)} 🐟: {t1 - t0:0.4f} seconds")

    return fishindex

def main():
    print('----------- day6 -----------')

    startingpoints = [1,1,3,1,3,2,1,3,1,1,3,1,1,2,1,3,1,1,3,5,1,1,1,3,1,2,1,1,1,1,4,4,1,2,1,2,1,1,1,5,3,2,1,5,2,5,3,3,2,2,5,4,1,1,4,4,1,1,1,1,1,1,5,1,2,4,3,2,2,2,2,1,4,1,1,5,1,3,4,4,1,1,3,3,5,5,3,1,3,3,3,1,4,2,2,1,3,4,1,4,3,3,2,3,1,1,1,5,3,1,4,2,2,3,1,3,1,2,3,3,1,4,2,2,4,1,3,1,1,1,1,1,2,1,3,3,1,2,1,1,3,4,1,1,1,1,5,1,1,5,1,1,1,4,1,5,3,1,1,3,2,1,1,3,1,1,1,5,4,3,3,5,1,3,4,3,3,1,4,4,1,2,1,1,2,1,1,1,2,1,1,1,1,1,5,1,1,2,1,5,2,1,1,2,3,2,3,1,3,1,1,1,5,1,1,2,1,1,1,1,3,4,5,3,1,4,1,1,4,1,4,1,1,1,4,5,1,1,1,4,1,3,2,2,1,1,2,3,1,4,3,5,1,5,1,1,4,5,5,1,1,3,3,1,1,1,1,5,5,3,3,2,4,1,1,1,1,1,5,1,1,2,5,5,4,2,4,4,1,1,3,3,1,5,1,1,1,1,1,1]
    fish = simulate(80, startingpoints)
    
    print(f'For first ⭐: after 80 days there are {len(fish)} 🐟')

    fishindex = faster_simulate(256, startingpoints)
    print(f'For ⭐⭐: after 256 days there are {sum(fishindex.values())} 🐟')
    
if __name__ == '__main__':
    sys.exit(main())