import csv
import matplotlib.pyplot as plt

dataset = "2. prace_se_soubory/data/vira_v_cesku.csv"

with open(dataset, "r") as file:
    reader = csv.DictReader(file)

    max_believers: int = 0
    most_popular: str = ""
    brno_believers: list[int] = []
    brno_faiths: list[str] = []
    jedi_believers: int = 0
    max_jedi_believers: int = 0

    for line in reader:
        n_believers = int(line["hodnota"])
        
        if n_believers > max_believers:
            max_believers = n_believers
            most_popular = line["vira_txt"]

        if line["uzemi_txt"] == "Brno":
            brno_faiths.append(line["vira_txt"])
            brno_believers.append(n_believers)

        if line["vira_txt"] == "Jedi" and line["uzemi_txt"] != "Česká republika":
            jedi_believers += n_believers
            if n_believers > max_jedi_believers:
                max_jedi_believers = n_believers
                most_jedi = line["uzemi_txt"]
        


print(f"The most popular is {most_popular} with {max_believers} believers")
print(f"There is {len(brno_faiths)} faiths in Brno and on average there is {round(sum(brno_believers)/len(brno_believers))} people who believe in a given faith")
print(f"Most Jedi: {most_jedi}, {max_jedi_believers}, Jedi believers: {jedi_believers}")

plt.bar(brno_faiths, brno_believers)
plt.xlabel("Faith")
plt.ylabel("Believers")
plt.show()