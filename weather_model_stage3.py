# weather_model_stage3.py
def temperature(t, a, b, c):
    return a * t**2 + b * t + c

# Read values from file
params = {}
with open("input_single.txt", "r") as file:
    for line in file:
        key, value = line.strip().split('=')
        params[key] = float(value)

t = params['t']
a = params['a']
b = params['b']
c = params['c']

print(f"Predicted temperature at time {t}: {temperature(t, a, b, c)}°C")
