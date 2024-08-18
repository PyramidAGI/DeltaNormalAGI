import pandas as pd
import random
import datetime

# Read behaviorblocks from the file
with open('behaviorblocks list.txt', 'r') as file:
    behaviorblocks = [line.split('\t')[1].strip() for line in file if line.strip()]

# Function to create a pyramid dataframe
def create_pyramid_dataframe(blocks, num_rows=13, num_cols=13, peak_col=7):
    df = pd.DataFrame('', index=range(num_rows), columns=range(num_cols))
    
    for row in range(num_rows):
        start_col = max(0, peak_col - row)
        end_col = min(num_cols, peak_col + row + 1)
        
        for col in range(start_col, end_col):
            if random.random() < 0.7:  # 70% chance to fill a cell
                if random.random() < 0.7:  # 70% chance for a behaviorblock, 30% for a dash
                    df.iloc[row, col] = random.choice(blocks)
                else:
                    df.iloc[row, col] = '-' * random.randint(3, 10)
    
    return df

# Create two random versions of the dataframe
df1 = create_pyramid_dataframe(behaviorblocks)
df2 = create_pyramid_dataframe(behaviorblocks)

# Function to write dataframe to file with timestamp
def write_dataframe_to_file(df, filename):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    full_filename = f"{filename}_{timestamp}.txt"
    
    with open(full_filename, 'w') as file:
        for _, row in df.iterrows():
            file.write('\t'.join(str(cell) for cell in row) + '\n')
    
    print(f"Dataframe written to {full_filename}")

# Write dataframes to files
write_dataframe_to_file(df1, "pyramid_dataframe_1")
write_dataframe_to_file(df2, "pyramid_dataframe_2")

# Print the dataframes
print("Dataframe 1:")
print(df1)
print("\nDataframe 2:")
print(df2)