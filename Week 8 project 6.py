def compute_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = list(map(float, file.readlines()))
        total_sum = sum(numbers)
        count = len(numbers)
        if count == 0:
            print("The file is empty. No numbers to average.")
            return None
        average = total_sum / count
        return average
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def main():
    filename = input("Please enter the name of the file containing numbers: ")
    average = compute_average(filename)
    if average is not None:
        print(f"The average of the numbers in '{filename}' is: {average}")
if __name__ == "__main__":
    main()
