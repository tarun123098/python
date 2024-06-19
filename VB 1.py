def power(base, exponent):
    if exponent == 0:
        return 1  # Base case: any number raised to the power of 0 is 1
    else:
        return base * power(base, exponent - 1)  # Recursive case

result = power(5, 3)
print(result)  # Output: 125
"""Step 1: Understanding the Function
Base Case (if exponent == 0):

If the exponent is 0, return 1. This is because any number raised to the power of 0 is 1.
Recursive Case (else: return base * power(base, exponent - 1)):

If the exponent is not 0, multiply the base by the result of the same function with the exponent decreased by 1.
Step 2: Breaking Down the Recursive Calls
Let’s see how this works with power(5, 3):

First Call (power(5, 3)):

exponent is 3, so it calculates 5 * power(5, 2).
Second Call (power(5, 2)):

exponent is 2, so it calculates 5 * power(5, 1).
Third Call (power(5, 1)):

exponent is 1, so it calculates 5 * power(5, 0).
Fourth Call (power(5, 0)):

exponent is 0, so it returns 1 (base case).
Step 3: Returning Values Back Up the Call Stack
Now, let’s return the values back up the call stack:

Fourth Call Returns:

power(5, 0) returns 1.
Third Call Returns:

power(5, 1) returns 5 * 1 = 5.
Second Call Returns:

power(5, 2) returns 5 * 5 = 25.
First Call Returns:

power(5, 3) returns 5 * 25 = 125.
Final Result
So, power(5, 3) returns 125, which is the result of 
5
3
5 
3
 .

Summary
Base Case: Stops the recursion when the exponent is 0 and returns 1.
Recursive Case: Multiplies the base by the result of the same function with the exponent decreased by 1.
Result Calculation: The function multiplies the base (5) by itself the number of times specified by the exponent (3) to give the result 125.
"""





