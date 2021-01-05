# Naive-Pattern-Search-Python
Naive search in data structure with desription and code in Python

- Naive searching algorithm mainy used for pattern searching from the given data.
- Easiest algorithm to understand and perform.

How it works?

- Compare elements and if its successfully compared then ,
  both the data and search Increment by 1 to compare further element.
  
- If both the element is different then ,
  pattern again initilise to 0th index but Data not.
 

Let's Understand with Example.
- Example: 
	
	Data    = ABCDBCABCABCABC
	pattern = BC
	
	compare A == B // False,
		Now pattern initilize to index 0.
	
	compare B == B // True,
		Both incremented by 1.
	
	compare C == C // True,
		Both incremented by 1.
		
		Now pattern size became 2 // So here we initilize pattern again with 0.
		
	Compare D == B // False,
		Now pattern initilize to index 0.
		
	Compare A == B // False
		Now pattern initilize to index 0.
		
- So you can see if element of data failed to compare with pattern ,
  Pattern initilise with 0 but data increment in each situation.
	
		
THANK YOU.

For Better understanding please visit :
	https://www.youtube.com/watch?v=k7UpWkVvajM&t=604s
			

