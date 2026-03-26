def count_file_lines():
    try:
        names = open('names.txt', 'r')
        count = 0
        for line in names:
            count += 1
        names.close()
        print(f'The number of names in the file is: {count}')
    except FileNotFoundError:
        print('The file names.txt was not found.')

if __name__ == '__main__':
    count_file_lines()
