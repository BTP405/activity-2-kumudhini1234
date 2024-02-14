def graphSnowfall(t):

#def graphSnowfall(t):

import matplotlib.pyplot as plt

def graphSnowfall(t):
    try:
        with open(t, 'r') as file:
            data = file.readlines()

        # Assuming the data is in the format: Year, Snowfall
        years = []
        snowfall = []

        for line in data:
            year, snow = map(int, line.strip().split(','))
            years.append(year)
            snowfall.append(snow)

        # Plotting the bar chart
        plt.bar(years, snowfall, color='blue')
        plt.xlabel('Year')
        plt.ylabel('Snowfall (inches)')
        plt.title('Snowfall Data Over the Years')
        plt.show()

    except FileNotFoundError:
        print(f"Error: File '{t}' not found.")

# Example usage:
file_path = 'snowfall_data.txt'  # Replace with your file path
graphSnowfall(file_path)

