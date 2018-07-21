import pyperclip

pages = int(input("How mach page you want to print: "))


def right_sequence(sheet, new_list):
    count = 0
    while count < 4:      
        try:
            seq = [sheet.pop(-1), sheet.pop(0), sheet.pop(0), sheet.pop(-1)]
            new_list.extend(seq)

        except:
            break

        count = count + 1
        
    return new_list


all_pages = [x for x in range(1, pages+1)]

pages_mod = pages % 4

if pages_mod != 0:
    first_part = all_pages[:-pages_mod]
    second_part = all_pages[-pages_mod:]
else:
    first_part = all_pages
    second_part = []

sorted_first_part = list()

start = 0
end = 16
count = 0


while start+1 < first_part[-1]:
    right_sequence(first_part[start:end], sorted_first_part)

    to_print = sorted_first_part[start:end]
    count = count + 1
    print("\n", count, " - ", to_print, 4 * " ", \
        "min page:", min(to_print), "max page: ", max(to_print))

    start = start + 16
    end = end + 16


if second_part != []:
        print("\n", count, " - ", second_part, 4 * " ", \
        "min page:", min(second_part), "max page: ", max(second_part))


printing_list = str(sorted_first_part + second_part)[1:-1]
print("\n Printing list:\n", printing_list)


try:
    pyperclip.copy(printing_list)
except:
    pass
