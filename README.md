# advent2021
🎄https://adventofcode.com/2021

I set up this Python repo as per [these excellent guidelines](https://docs.python-guide.org/writing/structure/).

## Day1: TIL

### Neat trick to work around path issues

I found when running tests, I was using relative referencing to get to data files, and that would work differently depending on where in the directory structure I ran the code from.

To work around it, I found [this little snippet](https://stackoverflow.com/questions/32527861/python-unit-test-that-uses-an-external-data-file), which uses `Path` to work it out:

```
from pathlib import Path
THIS_DIR = Path(__file__).parent

# construct path like this:
THIS_DIR.parent /'data/day1_sample.txt'
```
## Day 3: TIL

### Building blocks

Taking a "building blocks" approach to these challenges means I have to re-write less between parts.

So, for example, today:
1. a function to read in the data as arrays of bits
2. a separate function to transform arrays of bits into counts

Keeping those two bits separate meant I could just reuse those for the second part.


### Counter helpers

Using Counters in Python gets a bit fiddly because you're accessing the Counter (dictionary), a list of tuples (most_common()), so you end up with things like `counter[0][0]` which is hard to decipher without context.

I created two simple helper lambdas to make it a touch more readable:

```
most_common = lambda counter: counter.most_common()[0][0]
least_common = lambda counter: counter.most_common()[-1][0]
```