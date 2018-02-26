# Letter Blocks

A fun side project to find a better combinations of letters for my daughter's letter blocks. These letter blocks came with the Vtech Alphabet Activity Cube, shown here below.

![alt text](https://github.com/kjgraves/LetterBlocks/blob/master/VtechCube.jpg "The Vtech Alphabet Activity Cube!!")


As you can somewhat make out in the picture, each block has two letters on it. One letter is on each side, giving thirteen total blocks. HOWEVER, the letters are not distributed in such a way to spell words with the blocks. For instance, R and A are on the same block and K and X are the same block. Tons of words and names have both R and A in them, and not many have both K and X! Like any caring parent, I decided that it is time to start building algorithms and writing code to better figure out how the letters should be arranged to better spell words. We hear multiple times every day, "let's play with letter blocks aaall day!" Well, singing lady in the box, it would be a lot more fun if you could actually spell things!!

## How bad is it

Here are a pictures of both sides of all of the letter blocks. The right-most block in the top picture corresponds to the left-most block in the bottom (and vise-versa). The colors also help.

![alt text](https://github.com/kjgraves/LetterBlocks/blob/master/WordBlocks_side1.jpg "Side 1")
![alt text](https://github.com/kjgraves/LetterBlocks/blob/master/WordBlocks_side2.jpg "Side 2")

To have a benchmark, I downloaded the top 200 boys and girls names from the 2010s, and the 1000 most common words in the English language. To my dismay (and expectation), this combination of letters can only spell 56% of all of the words and names in my list!

## A quick solution

For my solution, I quickly found out that trying all possible combinations was not a good idea as there are about 8 trillion different combinations. Instead I calculated a better combination directly from my dictionary of words and numbers. Check out the python script above, but I was able to find a combination of letters that can spell almost 85% of the words. A massive improvement! 

Here is the 
	

