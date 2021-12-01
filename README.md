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
