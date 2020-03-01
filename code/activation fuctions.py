# 1.sigmoid function:
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 2.softmax function
def softmax(self, X):
    exps = np.exp(X)
    return exps / np.sum(exps, axis=1).reshape(-1,1)
