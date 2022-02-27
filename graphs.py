import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

pdo = pd.read_csv("out-pdo.txt", delimiter="\t")
soi = pd.read_csv("out-soi.txt", delimiter="\t")

plt.axhline(y=0, color='black')
plt.plot(soi["date"], soi["MA-12"], label="soi")
plt.plot(pdo["date"], pdo["MA-12"], label="pdo")

plt.xticks(pdo.index[::24], pdo["date"][::24], rotation=45, fontsize=8)
plt.locator_params(axis='x', nbins=len(pdo.index)/24)

plt.ylabel("PDO/SOI index")
plt.title("PDO-SOI MA-12")
plt.legend()
plt.show()
