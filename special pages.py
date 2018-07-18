remainder = list()
first = int(input("First page: ")) - 1
last = int(input("Last page: ")) + 1
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

print("\n", " - ", remainder)
