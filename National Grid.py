import matplotlib.pyplot as plt
import requests

url = "https://api.carbonintensity.org.uk/generation"
data = []
data2 = []
r = requests.get(url)
r1 = r.json()
r2 = r1["data"]
genMix = r2["generationmix"]

for i in range(len(genMix)):
    data.append(genMix[i]["perc"])
for i in range(len(genMix)):
    data2.append(genMix[i]["fuel"])
print(data)
print(data2)

plt.pie(data, labels=data2, labeldistance=1.2, autopct="%1.0f%%", pctdistance=1.1, startangle=90)
plt.legend(
    title="Fuel",
    loc="center left",
    bbox_to_anchor=(1, 0.1))
plt.show()
