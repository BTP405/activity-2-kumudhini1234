def printStats(t):
# def printStats(t):

def print_stats_decorator(func):

    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        count = len(numbers)
        average = sum(numbers) / count if count > 0 else 0
        maximum = max(numbers) if numbers else None

        print("Numbers:", numbers)
        print("Count:", count)
        print("Average:", average)
        print("Maximum:", maximum)

    return wrapper

@print_stats_decorator
def printStats(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file]
            return numbers

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

# Example usage:
file_path = 'sample.txt'  
printStats(file_path)
