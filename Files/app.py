from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft

# Relative path

path = Path('ecommerce')

# checking if the directory exists
print(path.exists())

# creating directory
# print(path.mkdir())

# deleting
print(path.rmdir())