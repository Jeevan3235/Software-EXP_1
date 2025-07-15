# weather_model_stage4.py

def temperature(t, a, b, c):
    return a * t**2 + b * t + c

# Read and process multiple sets from file
with open("input_multiple.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        a, b, c, t = map(float, line.strip().split(','))
        temp = temperature(t, a, b, c)
        print(f"Set {i}: At time {t}, predicted temperature is {temp:.2f}°C")
