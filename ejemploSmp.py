from sklearn import tree

# textura = 1 rugosa # textura = 0 lisa -> [peso,textura]
features = [[112, 0], [110, 0], [150, 1], [170, 1]]
# manzana  = 1 , naranja = 0
etiqueta = [1, 1, 0, 0]

# metodo que clasifica

clasificador = tree.DecisionTreeClassifier()
clasificador = clasificador.fit(features, etiqueta)

a = clasificador.predict([[190, 2]])

if a == 1:
    print("manzana")
elif a == 0:
    print("naranja")
else:
    print("no reconocido")
