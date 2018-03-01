# Letter Blocks

A fun side project to find a better combinations of letters for my daughter's letter blocks. These letter blocks came with the Vtech Alphabet Activity Cube, shown here below.

![alt text](https://github.com/kjgraves/LetterBlocks/blob/master/VtechCube.jpg "The Vtech Alphabet Activity Cube!!")


As you can somewhat make out in the picture, each block has two letters on it. One on each side, giving thirteen total blocks. HOWEVER, the letters are not distributed in such a way to spell words with the blocks. For instance, R and A are on the same block and K and X are the same block. Tons of words and names have both R and A in them, and not many have both K and X! Like any caring parent, I decided that it is time to start building algorithms and writing code to better figure out how the letters should be arranged to better spell words. We hear multiple times every day, "let's play with letter blocks aaallll day!" Well, singing lady in the box, it would be a lot more fun if you could actually spell things!!

## How bad is it

Here are a pictures of both sides of all of the letter blocks. The right-most block in the top picture corresponds to the left-most block in the bottom (and vise-versa). The colors also help.

![alt text](https://github.com/kjgraves/LetterBlocks/blob/master/WordBlocks_side1.jpg "Side 1")
![alt text](https://github.com/kjgraves/LetterBlocks/blob/master/WordBlocks_side2.jpg "Side 2")

To have a benchmark, I downloaded the top 200 boys and girls names from the 2010s from [ssa.gov](https://www.ssa.gov/oact/babynames/decades/names2010s.html), and the 1000 most common words in the English language from [here](https://gist.github.com/deekayen/4148741). Then, I removed all of the words that have double letters because these blocks can never spell words with double letters. To my dismay (and expectation), this combination of letters can only spell 59% of all of the words and names in my list! 

## A simple solution

For my quick and simple solution, I quickly found out that trying all possible combinations was not a good idea as there are about 8 trillion different combinations. If you are interested in finding out how I calculated those possibilities check out the python script [WordCombinations.py](https://github.com/kjgraves/LetterBlocks/blob/master/WordCombinations.py).

Instead, I calculated a better combination directly from my dictionary of words and numbers. For each letter, I found the other letter that was present with the first letter in the least amount of words/names. Then of all of those combinations, I chose the pairing that was in the HIGHEST amount of words and names. This algorithm ensured that two uncommon letters (\*cough\* like X and K \*cough\*) would not be paired together. I don't know if it necessarily the best solution, but I can't think of a better one without a lot more work. If you want more information on how this all worked, check out the python script [RankLetterPairs.py](https://github.com/kjgraves/LetterBlocks/blob/master/RankLetterPairs.py). 

On to the results! 

Here is the best grouping of letter pairs from my algorithm:


| L1 | L2 |
|---|---|
| e | q |
| a | z |
| n | x |
| o | k |
| i | j |
| r | v |
| t | d |
| l | f |
| h | b |
| s | w |
| u | p |
| m | g |
| c | y |


Just visually, that makes a lot more sense. Commonly used vowels are used with less commonly used letters (like e and q, o and k, and a and z). Using these letters, we can spell 87% of all of the names/words without double letters. Woohoo! That is so much better!

Now to see if I can pull these letter blocks apart without breaking them...


