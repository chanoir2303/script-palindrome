x = input()
y = []

for i in range(len(x)):
    y.append(x[i])
if y == y[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')
