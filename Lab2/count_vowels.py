s = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(f"Number of vowels = {count}")