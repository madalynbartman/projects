import pandas as pd

def extract_column_sum(file_path, column_index):
    # Read the text file into a DataFrame
    df = pd.read_csv(file_path, delimiter=r'\s+', header=None)
    
    # Sum the values in the specified column
    column_sum = df[column_index].sum()
    return column_sum

text_file_path = 'your_file.txt'
column_index = 0  # Change this to the index of the column you want to sum (0 for first column, 1 for second column, 2 for third column, etc.)

column_sum = extract_column_sum(text_file_path, column_index)
print(f'The sum of the values in column {column_index + 1} is: {column_sum}')
