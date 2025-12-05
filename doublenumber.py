nums = [1, 2, 3, 4, 5, 6]
print("Numbers:", nums)
even = list(filter(lambda n:True if n % 2 == 0 else False, nums))
print("Even numbers:", even)
double = list(map(lambda dn: dn * 2, even))
print("Doubled even numbers", double)