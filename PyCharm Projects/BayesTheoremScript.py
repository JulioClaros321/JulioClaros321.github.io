a = float(input("What is the probability of A?(Decimal): "))
b = float(input("What is the probability of B?(Decimal): "))
c = float(input("What is the probability of B given A?(Decimal): "))

def bayesTheorem(a, b, c):
    answer = (c * a) / b
    return answer

bayes = bayesTheorem(a, b, c)

print("Probability Calculated is", round(bayes, 2))





