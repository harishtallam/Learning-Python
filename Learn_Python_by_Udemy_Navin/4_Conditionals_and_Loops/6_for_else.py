# Check the numbers divisible by 5

nums = [12,16,18,29,28]

for num in nums:
    if num%5 == 0:
        print(num)
        break
else:
    print("Not Found")