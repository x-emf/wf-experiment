import json, os

import numpy as np
from sklearn import tree
trials_with_same_data = 200
accuracies = []
for _ in range(trials_with_same_data):
    os.system("python3 split.py")
    train_set, test_set = [], []
    with open("ready.json", "r") as f:
        obj = json.load(f)
        train_set, test_set = obj["set_train"], obj["set_test"]

    X_train = [ i["data"] for i in train_set ]
    Y_train = [ ord(i["actual_class"]) - ord("A") for i in train_set ]

    X_test = [ i["data"] for i in test_set ]
    Y_test = [ ord(i["actual_class"]) - ord("A") for i in test_set ]

    clf = ensemble.RandomForestClassifier(n_estimators=5)

    print("Fitting model...")
    clf.fit(X_train, Y_train)
    print(f"Fitted model as {clf}. ")

    print("Predicting on test set...")
    yhat_test = clf.predict(X_test)
    print("Predicting complete. ")

    print(f"TRUTH: {np.array(Y_test)}")
    print(f"MODEL: {yhat_test}")

    acc = sum([ 0 + (Y_test[i] == yhat_test[i]) for i in range(len(Y_test)) ])
    acc /= len(Y_test)

    print(f"Accuracy: {acc*100:.2f}%")

    accuracies.append(acc)

mean_acc = sum(accuracies) / len(accuracies)
print("--- --- ---")
print(f"Mean Accuracy: {mean_acc*100:.2f}")
