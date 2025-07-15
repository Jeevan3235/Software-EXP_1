# weather_model_stage2.py
def temperature(t, a, b, c):
    return a * t**2 + b * t + c

# Get input from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t: "))

print(f"Predicted temperature at time {t}: {temperature(t, a, b, c)}°C")
