import random

n=6
z = ""
for i in range(n):
    z+=random.choice("abc")

print(n)
print(z)
print("".join(random.sample(z, len(z))))

