from tkinter import *
import numpy as np
import pandas as pd

df = pd.read_csv("dispred_train.csv")
l1 = sorted(df.iloc[:, :-1])
#List of Diseases is listed in list disease.

#list of diseases
diseases = list(df.prognosis.unique())
l2 = []
for i in range(0, len(l1)):
    l2.append(0)

df = pd.read_csv("dispred_train.csv")
for i in range(len(diseases)):
    df.replace({"prognosis": {diseases[i]: i}},inplace=True)

#read test dataset
df2 = pd.read_csv("Prototype-1.csv")
for i in range(len(diseases)):
    df2.replace({"prognosis": {diseases[i]: i}},inplace=True)

#splitting the datasets
X_train = df.iloc[:, :-1]
y_train = df.iloc[:, -1]
X_test = df2.iloc[:, :-1]
y_test = df2.iloc[:, -1]


def DecisionTree():
    from sklearn import tree

    dt = tree.DecisionTreeClassifier()
    dt = dt.fit(X_train, y_train)

    from sklearn.metrics import accuracy_score
    y_pred = dt.predict(X_test)
    print(accuracy_score(y_test, y_pred))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(len(l1)):
        for z in psymptoms:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predict = dt.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(len(diseases)):
        if predicted == a:
            h = 'yes'
            break

    if h == 'yes':
        t1.delete("1.0", END)
        t1.insert(END, diseases[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    import joblib
    from sklearn.ensemble import RandomForestClassifier
    rf1 = RandomForestClassifier()
    rf1 = rf1.fit(X_train, np.ravel(y_train))

    # calculating accuracy
    from sklearn.metrics import accuracy_score
    y_pred = rf1.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    joblib.dump(rf1, "rf.pkl")
    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predict = rf1.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(len(diseases)):
        if predicted == a:
            h = 'yes'
            break

    if h == 'yes':
        t2.delete("1.0", END)
        t2.insert(END, diseases[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb = gnb.fit(X_train, np.ravel(y_train))

    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    for k in range(len(l1)):
        for z in psymptoms:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(len(diseases)):
        if predicted == a:
            h = 'yes'
            break

    if h == 'yes':
        t3.delete("1.0", END)
        t3.insert(END, diseases[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

root = Tk()

Symptom1 = StringVar()
Symptom1.set("Select")

Symptom2 = StringVar()
Symptom2.set("Select")

Symptom3 = StringVar()
Symptom3.set("Select")

Symptom4 = StringVar()
Symptom4.set("Select")

Symptom5 = StringVar()
Symptom5.set("Select")

Name = StringVar()

w2 = Label(root, justify=LEFT, text="Disease Predictor")
w2.config(font=("Times",30,"bold italic"))
w2.grid(row=1, column=0, columnspan=2, padx=100)


lb1 = Label(root, text="Symptom 1")
lb1.grid(row=7, column=0, pady=10, sticky=W)

lb2 = Label(root, text="Symptom 2")
lb2.grid(row=8, column=0, pady=10, sticky=W)

lb3 = Label(root, text="Symptom 3")
lb3.grid(row=9, column=0, pady=10, sticky=W)

lb4 = Label(root, text="Symptom 4")
lb4.grid(row=10, column=0, pady=10, sticky=W)

lb5 = Label(root, text="Symptom 5")
lb5.grid(row=11, column=0, pady=10, sticky=W)
OPTIONS = sorted(l1)

S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=7, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=8, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=9, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=10, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=11, column=1)


dst = Button(root, text="Decision Tree", command=DecisionTree)
dst.grid(row=12, column=0,padx=10,pady=10)

rnf = Button(root, text="Random forest", command=randomforest)
rnf.grid(row=13, column=0,padx=10,pady=10)

lr = Button(root, text="Naive Bayes", command=NaiveBayes)
lr.grid(row=14, column=0,padx=10,pady=10)


t1 = Text(root, height=1, width=40)
t1.grid(row=12, column=1, padx=10)

t2 = Text(root, height=1, width=40)
t2.grid(row=13, column=1 , padx=10)

t3 = Text(root, height=1, width=40)
t3.grid(row=14, column=1, padx=10)

root.mainloop()

