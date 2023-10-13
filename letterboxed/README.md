# letterboxed_solver.py

A solver for NYT Games' "Letter Boxed"

Wordlist from: [https://github.com/aliceyliang/letter-boxed-solver/](https://github.com/aliceyliang/letter-boxed-solver/blob/master/words_hard.txt)

## Definitions

Definition of 'Word' for this task: English dictionary word, no proper nouns, no curse words or very offensive terms ('clean' words only).

## Preparation
- Take as input a list of 12 letters.
- Split letters into sets of four sets of three.

## Problem
- Find a set of words that uses all letters.
- Letters can repeat.
- Letters from the same group may not be used back-to-back.
- Word boundaries must share a letter, e.g. the next word must start wit the last letter of the former word.
- Try to find the least amount of words that meet these conditions.
- When two sets of words are tied, the set with the least amount of total letters wins.

In other words: When laid out along the edges of a square, with each edge containing three letters from a group, find a line that connects all letters without touching or leaving the boundaries of the square. The letters must spell out words from the English dictionary. The least amount of words wins.

# Optimization Ideas
- Words which contain letters not present in the input string can obviously be disregarded.
- The first word should contain as many unique letters as possible. The first 'try' should therefore be: The word with the longest set of letters that is contained within the input set.
- However, there might be an incentive to pick a suboptimal first word if the optimal second word starts with a different letter than the optimal first word ends with.

One approach might be:
- Find all words that are possible.
	- Words which only contain letters in the input string.
	- Words without any substrings of length 2 that contain letters from the same input group.
- Consider each word a node in a graph.
- Words that share a letter at their boundary (last & first or first & last) are connected.
- Then somehow find the shortest path until all letters are found.
- This might produce suboptimal results because the traversal does not prefer words that contain "new" letters.
- So we would have to assign weights to the vertices/connections based on how many new letters are in the next word. 
- But those weights are static, so not aware of the previous nodes checked in that iteration.
- Maybe assigning weights based on a comparison of the two words connected would be enough to get a good algorithm.