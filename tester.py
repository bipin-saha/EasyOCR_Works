import pandas as pd

df = pd.read_csv("/home/bipin/projects/EasyOCR/trainer/all_data/train/labels.csv")
print(df)(bnocr) (base) bipin@ml-server:~/projects/EasyOCR/trainer$ cat tester.py
import pandas as pd

# Read the text file line by line and split into image name and text
data = []
with open('/home/bipin/projects/EasyOCR/trainer/all_data_example/scut_data/scut_test.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            data.append((parts[0], parts[1]))

# Create a DataFrame from the list of tuples
df = pd.DataFrame(data, columns=['ImageName', 'Text'])

# Write the DataFrame to a CSV file
df.to_csv('/home/bipin/projects/EasyOCR/trainer/all_data_example/scut_data/test_labels.csv', index=False)

# Print the DataFrame
print(df)
