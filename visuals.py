import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pdo = pd.read_csv("out-pdo.txt", delimiter="\t")
soi = pd.read_csv("out-soi.txt", delimiter="\t")
x = pdo["pdo-index"]
y = soi["soi-index"]

print("pdo mean")
print(np.mean(x))
print("pdo standard deviation")
print(np.std(x))

print("soi mean")
print(np.mean(y))
print("soi standard deviation")
print(np.std(y))

print("pdo-soi correlation")
print(x.corr(y))

#ax = plt.gca()
#pdo.plot(kind="line", x="date", y="pdo-index", ax=ax)
#soi.plot(kind="line", x="date", y="soi-index", color="red", ax=ax)


plt.scatter(x=x, y=y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")

plt.xlabel("pdo-index")
plt.ylabel("soi-index")

plt.show()
