# 8 Queens Puzzle

This is an attempt to solve the famous [Eight queen puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) using python.

As you can try for yourself, the brute force method is too slow, as there are 64\*63\*62\*61\*60\*59\*58\*57 ~ 1.8\*10^14 ways you can arrange 8 queens on one chess board. Even using numba compiler which increases the speed by 10 times isn't enough.

One needs to implement a genetic algorithm to achieve optimal results. Here's the result of a test run with only 14 generations and 4.49 seconds runtime:

```
Gen 	Best 	Avg
1 	60 	51.001
2 	62 	51.133
3 	62 	51.3
4 	60 	51.282
5 	60 	51.458
6 	62 	51.372
7 	60 	51.37
8 	60 	51.447
9 	60 	51.473
10 	60 	51.518
11 	60 	51.397
12 	62 	51.507
13 	60 	51.545
14 	60 	51.665
Time: 4.49 seconds
◻ ◼ ◻ ◼ ◻ ◼ ♕ ◼
◼ ♕ ◼ ◻ ◼ ◻ ◼ ◻
◻ ◼ ◻ ♕ ◻ ◼ ◻ ◼
♕ ◻ ◼ ◻ ◼ ◻ ◼ ◻
◻ ◼ ◻ ◼ ◻ ◼ ◻ ♕
◼ ◻ ◼ ◻ ♕ ◻ ◼ ◻
◻ ◼ ♕ ◼ ◻ ◼ ◻ ◼
◼ ◻ ◼ ◻ ◼ ♕ ◼ ◻
```

You can find the logic for the genetic algorithm [here](https://github.com/smal1378/Genetic8Vazir/blob/master/README.md) in the README.
