year = int(input("Enter your year: "))

def is_leap(year):
		
	divisible_by_4 = year % 4 == 0
	# the way to return a Boolean value
	return divisible_by_4
	
print(is_leap(year))
	
	
	
	




