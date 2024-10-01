def main():
    # Get the size of the array
    while True:
        try:
            array_size = int(input("Enter the size of the array: "))
            if array_size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input! Please enter a positive integer.")
    
    # Get the elements of the array        
    while True:
        try:
            elements = input("Enter the elements separated by space: ").split()
            if len(elements) == array_size:
                elements = [float(i) for i in elements]
                break
            else:
                print(f"Please enter exactly {array_size} elements.")
        except ValueError:
            print("Invalid input! Please enter numerical values.")
       
    # Calculate and display the cubes of the elements     
    for i in elements:
        cubed_value = i ** 3
        print(int(cubed_value))
        
if __name__ == "__main__":
    main()