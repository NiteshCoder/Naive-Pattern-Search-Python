
- Naive searching algorithm mainy used for pattern searching from the given data.
- Easiest algorithm to understand and perform.

How it works?
- Compare elements and if its successfully compared then ,
  both the data and search Increment by 1 to compare further element.
  
- If both the element is different then ,
  pattern again initilise to 0th index but Data not.


- Note : 
	- Each element of data compare with pattern again and again.
	
Let's Understand with Example.
- Example: 
	
	- Data    = A B C D B C A B C A B C A B C
	- pattern = B C
	
	- Step 1 : A B C D B C A B C A B C A B C
	- compare:   A B == B C
	
	- Step 2 : A B C D B C A B C A B C A B C
	- compare:   B C == B C  

	- Step 3 : A B C D B C A B C A B C A B C
	- compare:    C D ==  B C

	- Step 4 : A B C D B C A B C A B C A B C
	- compare:      D B ==   B C
	
	- Step 4 : A B C D B C A B C A B C A B C
	- compare:        B C ==   B C
	
	- Step 4 : A B C D B C A B C A B C A B C
	- compare:        C A ==  B C
	
	- Step 4 : A B C D B C A B C A B C A B C
	- compare:            ....
	Etc.
THANK YOU.

For Better understanding please visit :
	https://www.youtube.com/watch?v=k7UpWkVvajM&t=604s

