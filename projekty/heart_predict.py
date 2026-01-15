import csv
from sklearn.neural_network import MLPClassifier
from time import sleep as sl

X = []
Y = []

path = r"3. strojove_uceni/data/heart.csv"

with open(path) as file:
    for row in csv.DictReader(file):
        age = int(row["age"])
        cp = int(row["cp"])
        trestbps = int(row["trestbps"])
        chol = int(row["chol"])
        restecg = int(row["restecg"])
        thalach = int(row["thalach"])
        exang = int(row["exang"])
        oldpeak = float(row["oldpeak"])
        sex = int(row["sex"])

        heart_disease = int(row["heart_disease"])

        X.append([
            age, 
            sex, 
            cp, 
            trestbps, 
            #chol, 
            restecg, 
            thalach, 
            exang, 
            oldpeak
            ])
        Y.append(heart_disease)

X_train = X[:round(0.8*len(X))]
Y_train = Y[:round(0.8*len(Y))]

X_test = X[round(0.8*len(X)):]
Y_test = Y[round(0.8*len(Y)):]


neuronka = MLPClassifier(
    hidden_layer_sizes=(12, 6),
    activation="relu",
    learning_rate="adaptive",
    max_iter=2000,
    #random_state=1,
    #verbose=True
)

together = 0
test_num = 100

for i in range(test_num):
    neuronka.fit(X_train, Y_train)

    prediction = neuronka.predict(X_test)
    number = len(prediction)

    correct = 0
    for i in range(number):
        if Y_test[i] == prediction[i]:
            correct += 1

    right_ans = correct/number*100
    together += right_ans
    print(f"{right_ans}%")
    #sl(1)



print(f"Right answers: {round(together/test_num, 1)}%")
