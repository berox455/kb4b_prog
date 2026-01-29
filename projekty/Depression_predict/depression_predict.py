# Neuronová síť predikující BMI kategorii
# Jedná se pouze o učební ukázku - pro BMi je jinak využití neuronky nevhodné

import csv
import random

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy
data = "projekty/Depression_predict/student_depression_dataset.csv"


with open(data, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age = float(row["age"])
        academic_pressure = float(row["academic_pressure"])
        CGPA = float(row["CGPA"])
        study_satisfaction = float(row["study_satisfaction"])
        sleep_duration = int(row["sleep_duration"])
        dietary_habits = int(row["dietary_habits"])
        suicidal_thoughts = int(row["suicidal_thoughts"])
        study_hours = float(row["study_hours"])
        financial_stress = float(row["financial_stress"])
        family_histrory = int(row["family_histrory"])

        depression = int(row["depression"])

        X.append([
            age, 
            academic_pressure, 
            #CGPA, 
            study_satisfaction, 
            sleep_duration,
            dietary_habits,
            suicidal_thoughts,
            study_hours,
            financial_stress,
            family_histrory
            ])
        Y.append(depression)


# ---------- Rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.9 * rows)

train_X, test_X, train_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.1,
        #random_state=4
        )

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(8, 4),#16,8,4),
    activation="relu",
    max_iter=2000,
    verbose=True,
    #random_state=4
)

neural_network.fit(train_X, train_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Accuracy:", correct / len(results))

# ---------- Confusion matrix ----------
# zobrazuje jaké odpovědi dává neuronka pro dané vstupy
ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()
