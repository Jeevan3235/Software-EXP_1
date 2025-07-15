# weather_model_stage1.py
def temperature(t):
    a = -0.5
    b = 2.4
    c = 18
    return a * t**2 + b * t + c

# Example time
t = 3
print(f"Predicted temperature at time {t}: {temperature(t)}°C")
