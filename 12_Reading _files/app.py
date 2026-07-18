# Reading files

from pathlib import Path

# pi_file = Path('./pi_digits.txt')

# print(pi_file.read_text())


readme = Path('./pi_digits.txt')
contents = readme.read_text()

contents = contents.rstrip()

print(contents)

# print(type(contents))


# for i in contents:
#     print(i)
