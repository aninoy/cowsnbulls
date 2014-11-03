This repository contains different AI algorithms used to solve user created puzzles for the [Bulls & Cows game](http://en.wikipedia.org/wiki/Bulls_and_cows).

### Brute Force Method ###
In this method we use a recursive function to generate all the unique permutations of numbers with the number of digits in the game. The solver script usage is as shown below:

```shell
$ python solver.py 1234 10 4
```
1. 	The first argument here is the secret number thought by the user.
2.	The second argument is the maximum number of guesses allowed to the
	algorithm. Giving -1 as the input will not apply any limits on the number of allowed guesses.
3.	The third argument is the number of digits being played in the current game.

__Limitations__
The current implementation only works with digits 1-9 and not 0.


