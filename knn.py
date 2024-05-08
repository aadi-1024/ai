import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
# from sklearn.naive_bayes import CategoricalNB
import pandas as pd

df = pd.read_csv("./iris.csv")
train, test = train_test_split(df, test_size=0.2)

y_train, y_test = train["variety"], test["variety"]
x_train, x_test = train.drop("variety", axis=1), test.drop("variety", axis=1)

knn = RandomForestClassifier()
knn.fit(x_train, y_train)
pred = knn.predict(x_test)

print(classification_report(y_test, pred))