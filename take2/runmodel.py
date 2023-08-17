import json, random

from sklearn import tree

import cfg

deser_target = "alldata.json"
print(f"Loading data from {deser_target}...")
data = None
with open(deser_target, "r") as f:
    data_obj = json.load(f)
    data = data_obj["data"]
    print("Selecting desired classes...")
    data = [ i for i in data if i["class"] in cfg.DESIRED_CLASS_INDICES ]
    print("Shuffling dataset...")
    random.shuffle(data)
    print("Dataset shuffled.")
print(f"Loaded full dataset with {len(data)} entries.")
print()

ttsplit = cfg.TRAIN_TEST_SPLIT
print(f"Splitting into training and testing sets...")
print("Split, as specified in \"cfg.py\":")
n_train = int(ttsplit * len(data))
n_test = len(data) - n_train
print(f"> Training Set: {ttsplit*100:>5.1f}% ({n_train} items)")
print(f"> Test Set:     {(1-ttsplit)*100:>5.1f}% ({n_test} items)")
set_train = data[:n_train]
set_test  = data[n_train:]
assert len(set_train) == n_train and len(set_test) == n_test
print("Performed train/test split.")
print()

print(f"Preparing data and model...")
print("Seperating into X and Y arrays for use by scikit-learn...")
X_train = [ i["trace"] for i in set_train ]
Y_train = [ i["class"] for i in set_train ]
X_test  = [ i["trace"] for i in set_test  ]
Y_test  = [ i["class"] for i in set_test  ]
print("Seperation complete.")
print("Creating model object...")
clf = tree.DecisionTreeClassifier()
print(f"Model object created as {clf}.")
print("Preperation complete. Ready to train model. ")
print()

print("Fitting model...")
clf.fit(X_train, Y_train)
print(f"Fitted model as {clf}.")
print()

print("Predicting on test set and evaluating prediction...")
print(f"Predicting with model {clf}...")
yhat_test = clf.predict(X_test)
print("Predicting complete.")
print("Computing metrics (evaluating)...")
acc = sum([ 0 + (Y_test[i] == yhat_test[i]) for i in range(len(Y_test)) ])
acc /= len(Y_test)
print("Done computing all metrics.")
print()

print(f"Accuracy: {acc*100:.3f}%")
