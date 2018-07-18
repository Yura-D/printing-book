pages = input("How mach page you want to print: ")

template = [16, 1, 2, 15, 14, 3, 4, 13, 12, 5, 6, 11, 10, 7, 8, 9]


ready_numbers = list()
x = 0
count = 0
while x + 16 < int(pages):
    current_pages = list()
    for n in template:
        n = n + x
        ready_numbers.append(n)
        current_pages.append(n)
    count = count + 1
    print("\n", count, " - ", current_pages, 4 * " ", "min page:", min(current_pages), "max page: ", max(current_pages))
    del current_pages[:]
    x = x + 16

last_number = max(ready_numbers)

remainder = list()
first = last_number
last = int(pages) + 1
while True:
    if last - 1 not in remainder:
        last = last - 1
        remainder.append(last)
    else:
        break
    if first + 1 not in remainder:
        first = first + 1
        remainder.append(first)
    else:
        break
    if first + 1 not in remainder:
        first = first + 1
        remainder.append(first)
    else:
        break
    if last - 1 not in remainder:
        last = last - 1
        remainder.append(last)
    else:
        break

print("\n", count + 1, " - ", remainder, 4 * " ", "min page:", min(remainder), "max page: ", max(remainder))

for n in remainder:
    ready_numbers.append(n)


print("\n", ready_numbers)
