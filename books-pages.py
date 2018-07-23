import pyperclip

while True:
    PAGES = input("How mach page you want to print: ")
    try:
        NUM_PAGES = int(PAGES)
        break

    except ValueError:
        print("Oops!  That was no numbers.  Try again...")
        continue


def right_sequence(sheet, new_list):
    count = 0
    papers_in_sheet = 4
    while count < papers_in_sheet:
        if len(sheet) > 3:
            seq = [sheet.pop(-1), sheet.pop(0), sheet.pop(0), sheet.pop(-1)]
            new_list.extend(seq)

        else:
            print("\nYour last sheets don't have 4 papers...")
            break

        count = count + 1

    return new_list


ALL_PAGES = [x for x in range(1, NUM_PAGES+1)]

PAGES_MOD = NUM_PAGES % 4

if PAGES_MOD != 0:
    FIRST_PART = ALL_PAGES[:-PAGES_MOD]
    SECOND_PART = ALL_PAGES[-PAGES_MOD:]
else:
    FIRST_PART = ALL_PAGES
    SECOND_PART = []

SORTED_FIRST_PART = []

START = 0
END = 16
COUNT_SHEET = 0


while START+1 < FIRST_PART[-1]:
    right_sequence(FIRST_PART[START:END], SORTED_FIRST_PART)

    TO_PRINT = SORTED_FIRST_PART[START:END]
    COUNT_SHEET = COUNT_SHEET + 1
    print("\n", COUNT_SHEET, " - ", TO_PRINT, 4 * " ", \
    "min page:", min(TO_PRINT), "max page: ", max(TO_PRINT))

    START += 16
    END += 16


if SECOND_PART != []:
    print("\nSpecial sheet", " - ", SECOND_PART, 4 *" ",\
    "min page:", min(SECOND_PART), "max page: ", max(SECOND_PART))


PRINTING_LIST = str(SORTED_FIRST_PART + SECOND_PART)[1:-1]
print("\n Printing list:\n", PRINTING_LIST)


try:
    pyperclip.copy(PRINTING_LIST)
except:
    pass
