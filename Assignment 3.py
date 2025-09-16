#Question 1
def classify_number(num):
    #Classify a number as Positive, Negative, or Zero
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# Main program
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)   # Try converting input to int
        result = classify_number(number)
        print("Result:", result)
        break  # Exit the loop after valid input
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


#Question 2
def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Parameters:
        *args (float or int): A variable number of numeric values.

    Returns:
        float: The average of the given numbers.
        None: If no numbers are provided.

    Example:
        >>> calculate_average(10, 20, 30)
        20.0

        >>> calculate_average(5)
        5.0

        >>> calculate_average()
        None
    """
    if len(args) == 0:
        return None  # No values provided

    return sum(args) / len(args)


# Example usage
print(calculate_average(10, 20, 30))  # 20.0
print(calculate_average(5))           # 5.0
print(calculate_average())            # None



#Question 3
while True:
    try:
        user_input = input("Enter a number: ")
        number = float(user_input)   # Try converting input to a float
        print(f"You entered: {number}")
        break   # Exit loop if successful
    except ValueError:
        print(" Invalid input! Please enter a valid number.")


#Question 4
# List of names
names = ["Winnie", "Marcus", "Keith", "Ruvarashe"]

# Write names to the file, each on a new line
with open("names.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

# Read the file and print each name
with open("names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character



        #Question 5
        # Sample list of temperatures in Celsius
        celsius_temps = [0, 20, 37, 100]

        # Convert to Fahrenheit using map and lambda
        fahrenheit_temps = list(map(lambda c: c * 9 / 5 + 32, celsius_temps))

        # Print the converted list
        print("Celsius:", celsius_temps)
        print("Fahrenheit:", fahrenheit_temps)


    #Question 6
    def divide_numbers(numerator, denominator):
        """
        Divide two numbers and handle exceptions.

        Parameters:
            numerator (int or float): The numerator.
            denominator (int or float): The denominator.

        Returns:
            float: The result of numerator / denominator if successful.
            None: If an exception occurs.
        """
        try:
            result = numerator / denominator
            return result
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except TypeError:
            print("Error: Both numerator and denominator must be numbers (int or float).")


    # Example usage
    print(divide_numbers(10, 2))  # 5.0
    print(divide_numbers(10, 0))  # Error: Cannot divide by zero!
    print(divide_numbers(10, "a"))  # Error: Both numerator and denominator must be numbers



#Question 7
# Define custom exception
class NegativeNumberError(Exception):
    """Exception raised when a number is negative."""
    pass


# Function to check if a number is positive
def check_positive(number):
    """
    Raises NegativeNumberError if the number is negative.

    Parameters:
        number (int or float): The number to check.
    """
    if number < 0:
        raise NegativeNumberError(f"Error: {number} is negative!")
    else:
        print(f"{number} is positive.")


# Example usage
try:
    check_positive(10)   # Positive number
    check_positive(-5)   # Negative number, will raise exception
except NegativeNumberError as e:
    print(e)


#Question 8
import random

def generate_random_numbers(count=10, start=1, end=100):
    """
    Generate a list of random integers.

    Parameters:
        count (int): Number of random integers to generate.
        start (int): Minimum value (inclusive).
        end (int): Maximum value (inclusive).

    Returns:
        list: A list of random integers.
    """
    return [random.randint(start, end) for _ in range(count)]


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
        numbers (list): A list of integers or floats.

    Returns:
        float: The average of the numbers.
    """
    return sum(numbers) / len(numbers) if numbers else 0


# Main program
random_numbers = generate_random_numbers()
average = calculate_average(random_numbers)

print("Random numbers:", random_numbers)
print("Average:", average)



#Question 9
import re

# -------------------------
# I. Extract all email addresses
# -------------------------
def extract_emails(text):
    """
    Extracts all email addresses from a given text.
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


# -------------------------
# II. Validate date (YYYY-MM-DD)
# -------------------------
def validate_date(date_str):
    """
    Validates a date in the format YYYY-MM-DD.
    """
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date_str))


# -------------------------
# III. Replace word in a string
# -------------------------
def replace_word(text, old_word, new_word):
    """
    Replaces all occurrences of old_word with new_word in the text.
    """
    pattern = r"\b" + re.escape(old_word) + r"\b"  # ensures full word match
    return re.sub(pattern, new_word, text)


# -------------------------
# IV. Split string by non-alphanumeric characters
# -------------------------
def split_by_non_alnum(text):
    """
    Splits a string by all non-alphanumeric characters.
    """
    return re.split(r"\W+", text)


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    # I. Extract emails
    sample_text = "Contact us at support@example.com or sales@company.org."
    print("Extracted Emails:", extract_emails(sample_text))

    # II. Validate dates
    print("Valid date (2023-08-31):", validate_date("2023-08-31"))
    print("Invalid date (2023-15-10):", validate_date("2023-15-10"))

    # III. Replace words
    sentence = "Python is great. I love Python!"
    print("After replacement:", replace_word(sentence, "Python", "Java"))

    # IV. Split by non-alphanumeric
    messy_string = "Hello, world! Python_3.10 is awesome."
    print("Split result:", split_by_non_alnum(messy_string))


#Question 10
import socket

def run_server(host="127.0.0.1", port=65432):
    # Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)  # listen for 1 connection
        print(f"Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b"Hello from server!")

if __name__ == "__main__":
    run_server()

#ii)
import socket

def run_server(host="127.0.0.1", port=65432):
    # Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)  # Listen for 1 client
        print(f"Server listening on {host}:{port}...")

        conn, addr = server_socket.accept()  # Accept client connection
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b"Hello from server!")  # Send message

if __name__ == "__main__":
    run_server()
#iii)
import socket

def run_server(host="127.0.0.1", port=65432):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(1)
            print(f"✅ Server listening on {host}:{port}...")

            while True:
                try:
                    conn, addr = server_socket.accept()
                    with conn:
                        print(f"🔗 Connected by {addr}")
                        conn.sendall(b"Hello from server!")
                except Exception as e:
                    print(f"⚠️ Connection error: {e}")
    except Exception as e:
        print(f" Server error: {e}")

if __name__ == "__main__":
    run_server()

