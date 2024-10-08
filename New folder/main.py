def calculate_probability(n):
    return (1/6)**n
n = int(input("Enter the number of rolls: "))
print("Probability:", calculate_probability(n))