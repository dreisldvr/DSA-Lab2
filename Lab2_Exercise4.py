def generate_inverted_triangle():
    # Get the height of the triangle
    while True:
        try:
            height = int(input("Enter the height of the triangle: "))
            if height > 0:
                break
            else:
                print("Please enter a positive integer greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    # Generate the inverted triangle pattern
    for i in range(height, 0, -1):
        print('*' * i)

generate_inverted_triangle()