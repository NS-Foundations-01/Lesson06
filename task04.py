numbers = []

print("sonlarni kiriting")
for son in range(1, 10):
    numbers.append(int(input(f"{son}-kiriting ->  ")))


print(numbers)

katta_son = numbers[0]
kichik_son = numbers[0]

for num in numbers:
    if num > katta_son:
        katta_son = num

    elif num < kichik_son:
        kichik_son = num


print(f"Katta son : {katta_son}")
print(f"Kichik son : {kichik_son}")
