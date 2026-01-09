import csv
from sklearn.neural_network import MLPClassifier

X = []
Y = []

dataset = r"3. strojove_uceni/data/bmi.csv"
with open(dataset) as file:
    for line in csv.DictReader(file):
        Y.append(int(line["Index"]))
        gender = int(line["Gender"] == "Male")
        height = int(line["Height"])
        weight = int(line["Weight"])
        X.append([gender, height, weight])

X_train = X[:round(0.8*len(X))]
Y_train = Y[:round(0.8*len(Y))]

X_test = X[round(0.8*len(X)):]
Y_test = Y[round(0.8*len(Y)):]


neuronka = MLPClassifier(
    hidden_layer_sizes=(5,4,2),
    activation="relu",
    max_iter=1_000
)

neuronka.fit(X_train, Y_train)

prediction = neuronka.predict(X_test)
pocet = len(prediction)

correct = 0
for i in range(pocet):
    if prediction[i] == Y_test[i]:
        correct += 1

print(f"Right answers: {round(correct/pocet)*100}%")
