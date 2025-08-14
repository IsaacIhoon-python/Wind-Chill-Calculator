<section class="project">
    <h3>Wind Chill Calculator</h3>
    <p>A Python program that calculates the wind chill based on temperature and wind speed. Supports both Celsius and Fahrenheit input.</p>
    <pre><code>
# Function to calculate wind chill using the given formula
def calculate_wind_chill(T, V):
    return 35.74 + (0.6215 * T) - (35.75 * (V ** 0.16)) + (0.4275 * T * (V ** 0.16))

def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32

def main():
    temp = float(input("What is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()
    if scale == 'C':
        temp = celsius_to_fahrenheit(temp)
    for speed in range(5, 65, 5):
        wc = calculate_wind_chill(temp, speed)
        print(f"At temperature {temp:.1f}F, and wind speed {speed} mph, the windchill is: {wc:.2f}F")

if __name__ == "__main__":
    main()
    </code></pre>
    <a href="https://github.com/IsaacIhoon-python/Wind_Chill_Calculator" target="_blank">View on GitHub</a>
</section>
