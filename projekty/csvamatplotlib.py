import csv
import matplotlib.pyplot as plt

path = "2. prace_se_soubory/data/teploty.csv"

with open(path, "r") as file:
    reader = csv.DictReader(file)

    temps: list[float] = []
    years: list[int] = []
    max_temp: float = 0.00
    max_year: int = 0

    for line in reader:
        if (line["TIME"] == "AVG"):
            temp = float(line["TEMPERATURE"])

            temps.append(temp)
            years.append(int(line["YEAR"]))

        if temp > max_temp:
            max_temp = temp
            max_year = int(line["YEAR"])

print(f"Max temp {max_temp}˚C was in year {max_year}")

plt.plot(years, temps)
plt.title("Average temps in Czech republic")
plt.xlabel("Years")
plt.ylabel("Temp[˚C]")
plt.xticks(years[::5])
plt.show()
