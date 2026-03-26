import random

def write_random_numbers():
    try:
        count = int(input("Enter the amount of numbers you want to generate (max 1000)? "))

        if count < 1 or count > 1000:
            print("Enter a number between 1 and 1000.")
            return

        with open('random_numbers.txt', 'w') as file:
            for _ in range(count):
                number = random.randint(1, 500)
                file.write(str(number) + '\n')

        print(f"{count} random numbers have been written to random_numbers.txt.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == '__main__':
    write_random_numbers()
