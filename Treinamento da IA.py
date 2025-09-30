import numpy as np 

xTreino = np.array([[1,0],[0,1],[1,1],[0,0]])


yTreino = np.array([[1],[1],[1],[0]])

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_derivative(z):
    return z*(1-z)

np.random.seed(42)
pesos = np.random.rand(2,1) #duas entradas e uma saidas
bias = np.random.rand(1) #viés

taxaDeAprendizado = 0.1 #com a taxa menor fica mais rapido e menos preciso, ideal < 0.7

for epoca in range (10000000): #A quantidade de testes
    z = np.dot(xTreino, pesos) + bias 
    yPredito = sigmoid(z)

    erro = yTreino - yPredito

    dW = np.dot(xTreino.T, erro * sigmoid_derivative(yPredito))

    db = np.sum(erro * sigmoid_derivative(yPredito))

    pesos += taxaDeAprendizado * dW
    bias = bias + taxaDeAprendizado * db

print (yPredito.round(3)) #round serve para colocar a quantidade de casas apos a virgula
