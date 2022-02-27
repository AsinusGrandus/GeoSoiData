import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pdo = pd.read_csv("out-pdo.txt", delimiter="\t")
soi = pd.read_csv("out-soi.txt", delimiter="\t")
x = pdo["MA-12"][12:]
y = soi["MA-12"][12:]

print("pdo mean")
print(np.mean(x))
print("pdo standard deviation")
print(np.std(x))

print("soi mean")
print(np.mean(y))
print("soi standard deviation")
print(np.std(y))

print("pdo-soi r correlation")
print(x.corr(y))


plt.scatter(x=x, y=y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r")

plt.xlabel("pdo-index")
plt.ylabel("soi-index")

'''
plt.hist(y, bins=15)
plt.title("SOI")
plt.ylabel("# months")
plt.xlabel("SOI index")
'''

plt.show()
