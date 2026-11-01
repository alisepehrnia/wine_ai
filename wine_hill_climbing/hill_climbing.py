from random import random
from random import randint
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot
import numpy as np
from sklearn.linear_model import LinearRegression
 
# load dataset
def load_dataset():
        url = 'wine.xls'
        df = read_csv(url)
        data = df.values
        X, y = data[:, :-1], data[:, -1]
        return X, y

# optimize (pre-process)
def optimize_target(y):
        scaler = MinMaxScaler()
        y = y.reshape((len(y), 1))
        y = scaler.fit_transform(y)
        return y
 
# modify the current set of predictions
def modify_predictions(current):
        # copy current solution
        updated = current.copy()
        # select a point to change
        ix = randint(0, len(updated)-1)
        # flip the class label
        updated[ix] = random()
        return updated
 
# run a hill climb for a set of predictions
def hill_climb_testset(X_test, y_test, max_iterations):
        mseList = list()
        # generate the random initial solution
        solution = [random() for i in range(X_test.shape[0])]
        # evaluate the initial solution
        mse = mean_squared_error(y_test, solution)
        print('=>first random => mse=%.4f' % mse)
        # hill climb to a solution
        for i in range(max_iterations):
                # record mse's
                mseList.append(mse)
                # generate new candidate
                candidate = modify_predictions(solution)
                # evaluate candidate
                value = mean_squared_error(y_test, candidate)
                # check if it is as good or better
                if value <= mse:
                        solution, mse = candidate, value
                        print('%d => mse=%.4f' % (i, mse))
                # stop once we achieve the best mse
                if mse <= 0.01:
                        break
        return solution, mseList
 
# load dataset
X, y = load_dataset()
# optimize
y = optimize_target(y)
# split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# run hill climb
yhat, mses = hill_climb_testset(X_test, y_test, 1)
# plot the mses vs iterations
pyplot.plot(mses)
pyplot.show()
# regression
reg = LinearRegression().fit(X_test, yhat)
print(reg.coef_)
print(reg.intercept_)
# histogram
n, bins, patches = pyplot.hist(X[0])
pyplot.grid(True)
pyplot.show()
#n, bins, patches = pyplot.hist(yhat)
#pyplot.grid(True)
#pyplot.show()
