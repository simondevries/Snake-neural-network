# Taken from https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

# first neural network with keras make predictions
import numpy
from directions import DIRECTIONS
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
import random
# load the dataset
# dataset = loadtxt('pima-indians-diabetes-2.csv', delimiter=',')
# # split into input (X) and output (y) variables
# X = dataset[:,0:4]
# y = dataset[:,4:12]

# print(y)
# # define the keras model

# # (1) defining the network
# model = Sequential()
# # input_dim is number nodes
# model.add(Dense(4, input_dim=4, activation='sigmoid'))
# model.add(Dense(4, activation='sigmoid'))
# model.add(Dense(8, activation='relu')) #  rectified linear unit activation function
# # model.add(Dense(8, activation='sigmoid'))
# # model.add(Dense(4, activation='sigmoid'))
# # model.add(Dense(4, activation='relu'))

# # plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

# # (2) 
# # Loss funciton used to evaluate a set of weights
# # Optimizer is used to search through different weights we would like to correct and report during training
# # compile the keras model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # Actually train the set. Epochs is one iteration of all the rows, batch size is how many it should do before weights are updated
# model.fit(X, y, epochs=150, batch_size=10, verbose=0)

# # (3) Get some results
# # make class predictions with the model
# predictions = model.predict_classes(X)

# _, accuracy = model.evaluate(X, y)
# print('Accuracy: %.2f' % (accuracy*100))
# # summarize the first 5 cases
# for i in range(10):
# 	print(i)
# 	print(X[i].tolist())
# 	print(predictions[i])
# 	print(y[i])
# 	print("")
# 	print(X[i].tolist(), '=>', predictions[i], '(expected=', y[i].tolist(),')')


def createBrain():
    model = Sequential()
    # # input_dim is number nodes
    model.add(Dense(18, input_dim=11, activation='sigmoid'))
    # model.add(Dense(18, activation='sigmoid'))
    model.add(Dense(4, activation='softmax'))

    return model



def networkThink(model, snakeDirection, dWall, dFood, dSnake):
    # print("network think")
    
    snakeDirectionNormalized = (snakeDirection / 2) - 1
    # print("snakeDirectionNormalized:", str(snakeDirectionNormalized))
    #model, distaceToFood, distanceToFood, distanceToSelf):
    inputs = numpy.array([[snakeDirectionNormalized, dWall[0],dWall[1],dWall[2],dWall[3],dFood[0],dFood[1], dSnake[0], dSnake[1], dSnake[2], dSnake[3]]])

    predictions = model.predict(inputs)
    # print("1" + predictions)
    predictionsTwo = numpy.asarray(predictions, dtype=float)
    # # print("2" + predictionsTwo)
    # print("1" + predictionsTwo[0])
    # print("2" + predictionsTwo[1])
    # print("3" + predictionsTwo[2])
    # print("4" + predictionsTwo[3])
    # # print(predictionsTwo[0][0])

    if (predictionsTwo[0][0] >= max(predictionsTwo[0][1],predictionsTwo[0][2],predictionsTwo[0][3])):
        # print("down")
        return DIRECTIONS.Down #which one???

    elif (predictionsTwo[0][1] >= max(predictionsTwo[0][0],predictionsTwo[0][2],predictionsTwo[0][3])):
        # print("up")
        return DIRECTIONS.Up #which one???

    elif (predictionsTwo[0][2] >= max(predictionsTwo[0][0],predictionsTwo[0][1],predictionsTwo[0][3])):
        # print("left")
        return DIRECTIONS.Left #which one???

    elif (predictionsTwo[0][3] >= max(predictionsTwo[0][0],predictionsTwo[0][1],predictionsTwo[0][2])):
        # print("right")
        return DIRECTIONS.Right #which one???

def mutateBrain(modelBrain, amount):
    weights = modelBrain.get_weights()
    newBrain = createBrain()
    # print(weights)
    
    for i in range(len(weights)):
        if (i % 2 is 0):
            for j in range(len(weights[i])):
                    for k in range(len(weights[i][j])):
                        newVal = weights[i][j][k] + random.gauss(0, amount)
                        weights[i][j][k] = newVal
    # print(weights)
    newBrain.set_weights(weights)
    return newBrain