text = "2020 1 28.5 15.2 0 45.5\n2020 2 29.1 16.0 0 50.2\n2021 1 27.8 14.5 0 40.3"
lines = text.split('\n')

print(type(lines))        # <class 'list'>
print(len(lines))         # 3
print(lines[0])           # '2020 1 28.5 15.2 0 45.5'
print(lines[1])           # '2020 2 29.1 16.0 0 50.2'