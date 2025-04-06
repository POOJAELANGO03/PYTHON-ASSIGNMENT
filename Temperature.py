def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

try:
    celsius = float(input("🌡️ Enter temperature in Celsius: "))
    fahrenheit, kelvin = convert_temperature(celsius)

    print("\n📊 Temperature Conversion Results:")
    print(f"→ Fahrenheit: {fahrenheit:.2f}°F")
    print(f"→ Kelvin: {kelvin:.2f}K")
except ValueError:
    print("\n⚠️ Invalid input! Please enter a valid number.")
