# Function to calculate the power of a number using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
    
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Call the power function to calculate the result
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")