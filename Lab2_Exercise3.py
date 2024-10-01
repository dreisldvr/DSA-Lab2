def generate_hollow_square():
    # Get the side length of the square
    while True:
        try:
            n = int(input("Enter the side length of the square: "))
            if n >= 2:
                break
            else:
                print("Please enter a positive integer greater than or equal to 2.")
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    # Generate the hollow square pattern
    for i in range(n):
        if i == 0 or i == n - 1:
            print('x' * n)
        else:
            print('x' + ' ' * (n - 2) + 'x')

generate_hollow_square()