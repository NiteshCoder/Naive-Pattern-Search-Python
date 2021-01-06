
#Naive Pattern Searching Algorithm
'''
- Naive searching algorithm mainy used for pattern searching from the given data.
- Easiest algorithm to understand and perform.

How it works?
- Compare elements and if its successfully compared then ,
  both the data and search Increment by 1 to compare further element.
  
- If both the element is different then ,
  pattern again initilise to 0th index but Data not.

Let's Understand with Example.
- Example: 
	
	Data    = A B C D B C A B C A B C A B C
	pattern = B C
	
	-Step 1 : A B C D B C A B C A B C A B C
	/compare:   B C
	
	-Step 2 : A B C D B C A B C A B C A B C
	/compare:     B C  

	-Step 3 : A B C D B C A B C A B C A B C
	/compare:       B C

	-Step 4 : A B C D B C A B C A B C A B C
	/compare:         B C
	
	-Step 4 : A B C D B C A B C A B C A B C
	/compare:           B C
	
	-Step 4 : A B C D B C A B C A B C A B C
	/compare:             B C
	
	-Step 4 : A B C D B C A B C A B C A B C
	/compare:               B C

	Etc.
THANK YOU.

For Better understanding please visit :
	https://www.youtube.com/watch?v=k7UpWkVvajM&t=604s

'''



'''
ord() = Used to convert character to integer.
chr() = Used to convert integer to character.

- String is immutable so we can't overwrite again and again ,
  so I have taken new variable called result.
'''
def upper_case(data):
	result =''
	len_data = len(data)
	for i in range(len_data):
		if data[i] >= 'a' and data[i] <= 'z':
			result += chr((ord(data[i])) - 32 )
		else:
			result+=data[i]
		
	return result


'''
- Actual logic of naive pattern search algorithm.
- What this logic gives ?
		- Search for pattern
		If FOUND then
		- Number of pattern that mathched.
		
		Otherwise notify user that particulat pattern not found.
'''	
def naive_pattern_search(data,search):
	n = len(data)
	m = len(search)
	cnt = 1
	result = []
	for i in range(n-m+1):
		for j in range(m):
			#print(f"\n data = { data[i+j] }  Search : { search[j] }")
			if data[i+j] == search[j]:
				cnt += 1
			else:
				cnt = 0
				
			if cnt == m:
				result.append(i)
				#print("Pattern Found At : ", i)
				
	return result		
				
				
#Main method : Start Execution from here.
if __name__ == "__main__":
	main_string = str(input("Enter String : "))
	main_string = upper_case(main_string)
	print("\n-----------------DATA------------------------")
	print(f"{ main_string } ")
	
	search_pattern = str(input("\nEnter Search Pattern : "))
	search_pattern = upper_case(search_pattern)
	print("\n-----------------SEARCHED FOR-----------------")
	print(f"{ search_pattern }")
	
	
	
	print("\n-----------------RESULT-----------------------")
	
	list = naive_pattern_search(main_string,search_pattern)
	if not list:
		print("\nOops! Searched pattern not found.")
	else:
		print(f"\nFound at : { list }")
