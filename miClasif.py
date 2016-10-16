from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from scipy.spatial import distance

def eucDist(a , b):
    return distance.euclidean(a,b)

#############################################################
class miClasif():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        predicciones = []

        for row in x_test:
            lab = self.closest(row)
            predicciones.append(lab)
            
        return predicciones

    def closest(self ,row):
        cercano , ind = eucDist(row, self.x_train[0]) , 0

        for i in range(len(self.x_train)):
            
            if eucDist(row,self.x_train[i]) < cercano:
                cercano , ind = eucDist(row,self.x_train[i]) , i

        return self.y_train[ind]

##########################################################

iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = .5)

clsf = miClasif()
clsf.fit(x_train,y_train)

predicciones = clsf.predict(x_test)
print(accuracy_score(y_test,predicciones))
