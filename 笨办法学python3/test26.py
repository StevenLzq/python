from sys import argv
prompt='>'
print("How old are you?", end=' ')
age = input(prompt)
print("How tall are you?", end=' ')
height=input(prompt)
print("How much do you weigh?", end=' ')
weight = input(prompt)

print(format,"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)

print(format,"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


