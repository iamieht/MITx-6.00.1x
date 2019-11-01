#Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon 0

epsilon = 0.01
k = 24
guess = k/2.0
numberOfGuesses = 0
while abs(guess*guess - k) >= epsilon:
    numberOfGuesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print("Square root of", k, "is about", guess, "in", numberOfGuesses, "number of guesses")