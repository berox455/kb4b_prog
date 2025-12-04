import csv
import matplotlib.pyplot as plt

cesta = r"2. prace_se_soubory\data\vira_v_cesku.csv"
with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    nazev_viry = []
    pocet_vericich = []

    for radek in reader:
        if (radek["uzemi_txt"] == "Česká republika"):
            if(int(radek["hodnota"]) > 10_000):
                nazev_viry.append(radek["vira_txt"])
                pocet_vericich.append(int(radek["hodnota"]))

    for i in range(len(nazev_viry)):
        print(nazev_viry[i], pocet_vericich[i])
    
    fig, ax = plt.subplots()
    # viditelne hodnoty na ose x
    fig.autofmt_xdate()

    ax.bar(nazev_viry, pocet_vericich)
    bars = ax.bar(nazev_viry, pocet_vericich, color=plt.cm.tab20.colors[:len(nazev_viry)])

    # výpis hodnoty
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height - 10, str(height), ha='center', va='bottom')

    ax.set_title('Počet věřících v ČR    [2021; pouze nad 10 000 věřících]')
    ax.set_xlabel('Víra')
    ax.set_ylabel('Počet věřících')
    plt.show()
