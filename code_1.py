def print_array_elements(array):
    for element in array:
        print(element*2)

def main():
    # Taking user input for the size of the array
    size = int(input("Enter the size of the array: "))

    # Taking user input for the elements of the array
    array = []
    print("Enter the elements of the array:")
    for i in range(size):
        element = int(input(f"Enter element {i + 1}: "))
        array.append(element)

    # Printing the elements of the array
    print("Elements of the array times 2:")
    print_array_elements(array)

if __name__ == "__main__":
    main()