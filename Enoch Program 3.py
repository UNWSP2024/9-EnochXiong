def sum_numbers_from_file():
    try:
        total = 0

        numbers = open('numbers.txt', 'r')
        for line in numbers:
            try:
                number = int(line.strip())
                total += number
            except ValueError:
                print(f"Skipping invalid value: {line.strip()}")

        numbers.close()
        print(f"The total of the numbers is: {total}")

    except IOError:
        print("An error occurred while trying to read the file.")

if __name__ == '__main__':
    sum_numbers_from_file()
