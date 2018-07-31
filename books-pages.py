import pyperclip


def get_pages():
    """Get number of pages and check if it right."""
    num_of_pages = None
    MIN_PAGES = 4

    while True:
        pages = input("How mach page you want to print: ")
        try:
            num_of_pages = int(pages)

            if num_of_pages < MIN_PAGES:
                print("less than 4 pages. Try again...")
                continue

            break

        except ValueError:
            print("Oops!  That was no numbers.  Try again...")
            continue

        if num_of_pages < MIN_PAGES:
            print("less than 4 pages. Try again...")
            continue

    return num_of_pages


def right_sequence(sheet, new_list):
    """Take the right sequence of numbers and create new list"""
    count = 0
    PAPERS_IN_SHEET = 4
    while count < PAPERS_IN_SHEET:
        if len(sheet) >= PAPERS_IN_SHEET:
            seq = [sheet.pop(-1), sheet.pop(0), sheet.pop(0), sheet.pop(-1)]
            new_list.extend(seq)

        else:
            print("\nYour last booklet don't have 4 papers...")
            break

        count = count + 1

    return new_list


def check_pages(num_of_pages):
    """Checks if there mudulo from the numbers and divides at the to part"""
    ALL_PAGES = [x for x in range(1, num_of_pages+1)]

    PAGES_MOD = num_of_pages % 4

    if PAGES_MOD != 0:
        first_part = ALL_PAGES[:-PAGES_MOD]
        second_part = ALL_PAGES[-PAGES_MOD:]

    else:
        first_part = ALL_PAGES
        second_part = []

    return first_part, second_part


def printing_sheet(first_part, second_part):
    """Print all by sheets"""
    start = 0
    end = 16
    count_sheet = 0
    sorted_first_part = []

    while start+1 < first_part[-1]:
        right_sequence(first_part[start:end], sorted_first_part)

        to_print = sorted_first_part[start:end]
        count_sheet = count_sheet + 1
        print("\n", count_sheet, " - ", to_print, 4 * " ", \
        "min page:", min(to_print), "max page: ", max(to_print))

        start += 16
        end += 16


    if second_part != []:
        print("\nSpecial sheet", " - ", second_part, 4 *" ",\
        "min page:", min(second_part), "max page: ", max(second_part))


    printing_list = str(sorted_first_part + second_part)[1:-1]
    print("\n Printing list:\n", printing_list)
    return printing_list


def main():
    pages = get_pages()
    first_part, second_part = check_pages(pages)
    printing_list = printing_sheet(first_part, second_part)
    try:
        pyperclip.copy(printing_list)
    except pyperclip.PyperclipException as error:
        print(error)

if __name__ == "__main__":
    main()
