# datasets -> https://archive.ics.uci.edu/ml/datasets/Spambase

# numpy module
import numpy as np

# pandas module
import pandas as pd

# skleran module
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn import cross_validation

def read_data():
    data = pd.read_csv('spambase/spambase.data').as_matrix()
    np.random.shuffle(data)

    X = data[:,:48]
    Y = data[:,-1]
    return X, Y

def spam_clf_naive_bayes(X, Y):
    X_train = X[:-100,]
    y_train = Y[:-100,]
    X_test = X[-100:,]
    y_test = Y[-100:,]

    model = MultinomialNB()
    model.fit(X_train, y_train)
    print ("Classification rate for NB:", model.score(X_test, y_test))

def spam_clf_svm(X, Y):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        X, Y, test_size=0.4, random_state=0)
    clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
    print ("Classification rate for SVM:", clf.score(X_test, y_test))

def main():
    X, Y = read_data()
    spam_clf_naive_bayes(X, Y)
    spam_clf_svm(X, Y)

if __name__ == '__main__':
    main()