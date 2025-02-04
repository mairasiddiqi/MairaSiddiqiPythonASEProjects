import pandas as pd

def load_cvs(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found at: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "/Users/mairasiddiqi/PycharmProjects/PythonProject/Fundamentals1/womenInSTEM.csv"
data = load_cvs(file_path)

if data is not None:
    print(data)