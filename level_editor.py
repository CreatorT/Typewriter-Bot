import tkinter as tk
from tkinter import messagebox
import json
import os
import math

data_file = "level_data.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return {}

def save_data():
    with open(data_file, "w") as f:
        json.dump(levels_data, f, indent=4)

def save_manual_input():
    level = level_var.get()
    speed = speed_entry.get()
    error_rate = error_rate_entry.get()

    if speed and error_rate:
        try:
            speed = float(speed)
            error_rate = float(error_rate)

            levels_data[level] = {"Speed": speed, "Error Rate": error_rate}

            save_data()

            messagebox.showinfo("Success", f"Level {level} data saved!\nSpeed: {speed}, Error Rate: {error_rate}")
            
            speed_entry.delete(0, tk.END)
            error_rate_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter numeric values for Speed and Error Rate.")
    else:
        messagebox.showerror("Missing data", "Please enter both Speed and Error Rate.")

def apply_functions():
    speed_function = speed_function_entry.get()
    error_rate_function = error_rate_function_entry.get()

    start_level = int(start_level_var.get())
    end_level = int(end_level_var.get())

    if speed_function and error_rate_function:
        try:
            for level in range(start_level, end_level + 1):
                x = level
                speed = eval(speed_function)
                error_rate = eval(error_rate_function)
                
                levels_data[f"Level {level}"] = {"Speed": speed, "Error Rate": error_rate}

            save_data()

            messagebox.showinfo("Success", "Functions applied and values saved for specified levels.")
        
        except Exception as e:
            messagebox.showerror("Error", f"Invalid function. Please enter valid Python expressions. Error: {e}")
    else:
        messagebox.showerror("Missing functions", "Please enter valid functions for Speed and Error Rate.")

# Create the main window
root = tk.Tk()
root.title("Level Input with Functions")

# Load existing data from JSON file
levels_data = load_data()

# Variables for level selection (manual input)
level_var = tk.StringVar(value="Level 1")

# Dropdown for selecting level
level_label = tk.Label(root, text="Select Level (Manual Entry):")
level_label.pack()

level_dropdown = tk.OptionMenu(root, level_var, *[f"Level {i}" for i in range(1, 101)])
level_dropdown.pack()

# Manual input for Speed
speed_label = tk.Label(root, text="Speed:")
speed_label.pack()

speed_entry = tk.Entry(root)
speed_entry.pack()

# Manual input for Error Rate
error_rate_label = tk.Label(root, text="Error Rate:")
error_rate_label.pack()

error_rate_entry = tk.Entry(root)
error_rate_entry.pack()

# Button to submit manual input
submit_button = tk.Button(root, text="Submit Manual Input", command=save_manual_input)
submit_button.pack()

# Section for function input
function_label = tk.Label(root, text="Apply Function to Levels:")
function_label.pack()

# Dropdown for starting level
start_level_var = tk.StringVar(value="1")
start_level_label = tk.Label(root, text="Select Start Level:")
start_level_label.pack()
start_level_dropdown = tk.OptionMenu(root, start_level_var, *[str(i) for i in range(1, 101)])
start_level_dropdown.pack()

# Dropdown for ending level
end_level_var = tk.StringVar(value="100")
end_level_label = tk.Label(root, text="Select End Level:")
end_level_label.pack()
end_level_dropdown = tk.OptionMenu(root, end_level_var, *[str(i) for i in range(1, 101)])
end_level_dropdown.pack()

# Input for Speed function
speed_function_label = tk.Label(root, text="Speed Function (use 'x' for level):")
speed_function_label.pack()
speed_function_entry = tk.Entry(root)
speed_function_entry.insert(0, "5 + 0.1 * x")  # Default function example
speed_function_entry.pack()

# Input for Error Rate function
error_rate_function_label = tk.Label(root, text="Error Rate Function (use 'x' for level):")
error_rate_function_label.pack()
error_rate_function_entry = tk.Entry(root)
error_rate_function_entry.insert(0, "0.5 - 0.01 * x")  # Default function example
error_rate_function_entry.pack()

# Button to apply the functions
apply_functions_button = tk.Button(root, text="Apply Functions", command=apply_functions)
apply_functions_button.pack()

# Start the GUI event loop
root.mainloop()

# When the window is closed, data is already saved in the JSON file
print("Collected Data (stored in JSON):")
for level, data in levels_data.items():
    print(f"{level}: {data}")
