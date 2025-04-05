def temperature_analysis():
    temperatures = []

    for i in range(7):
        temp = float(input(f"Enter temperature for day {i+1}: "))
        temperatures.append(temp)

    highest = max(temperatures)
    lowest = min(temperatures)
    total = sum(temperatures)
    average = total / 7

    print(f"Highest Temperature: {highest}")
    print(f"Lowest Temperature: {lowest}")
    print(f"Sum of Temperatures: {total}")
    print(f"Average Temperature: {average:.2f}")

temperature_analysis()



















