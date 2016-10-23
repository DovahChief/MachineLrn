from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5)

clsf = tree.DecisionTreeClassifier()
clsf2 = KNeighborsClassifier()

clsf.fit(x_train, y_train)
predicciones = clsf.predict(x_test)
print(accuracy_score(y_test, predicciones))

clsf2.fit(x_train, y_train)
predicciones2 = clsf.predict(x_test)
print(accuracy_score(y_test, predicciones2))
