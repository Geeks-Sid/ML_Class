import numpy as np

class MLP:
    def __init__(self, X, y, layers, l1_neurons, l2_neurons, lr = 0.1):
        self.layers = layers
        self.l1_neurons = l1_neurons
        self.l2_neurons = l2_neurons
        self.lr = lr
        self.W = np.random.random((self.l2_neurons, self.l1_neurons+1))
        self.V = np.random.random((self.l1_neurons, np.array(X).shape[1]+1))
        self.X = X
        self.y = y
        
    def __augment_inputs(self, X):
        for x in X:
            x.insert(0,-1)
        return X
    
    def __activation(self, net, deriv = True):
        if deriv:
            return self.activation(net, deriv = False)/ (1 - self.activation(net, deriv = False))
        else:
            return 1 / (1 + np.e ** (-net))
    
    def __net_input(self, ip, weights):
        return np.dot(weights, ip)
    
    def train(self, total_epochs):
        print("Before Augmentation input pattern : ", self.X)
        self.X = self.__augment_inputs(self.X)
        print("Augmented input pattern : ", self.X)
        self.epoch_error = np.zeros(total_epochs)
        self.epoch = 0
        self.p = 0
        for self.epoch in range(total_epochs):
            print("EPOCH : ", self.epoch)
            current_cycle_error = 0
            for data, label in zip(self.X, self.y):
                
                #complete forward _ pass
                t = self.predict(data, self.V)
                t_augmented = np.insert(t, 0, -1)    
                o = self.predict(t_augmented, self.W)
                
                # compute del_o for output layer
                del_o = np.zeros(np.shape(o))
                count = 0
                for di, oi in zip(label, o):
                    del_o[count] = ((di-oi)*oi*(1-oi))
                    count += 1
                
                # compute del_t for hidden lauer
                del_t = np.zeros(t.shape[0])
                count = 0
                for oi in o:
                    for i in range(np.shape(self.W)[0]):
                        temp = 0
                        for j in range(len(self.W[i])):
                            temp += del_o * self.W[:,i]
                        del_t[count] = oi * (1 - oi) * temp
                    count += 1
                    
                #Compute W' = W + eta * d_o * t_prev
                for i in range(len(self.W)):
                    self.W[i] = self.W[i] + (self.lr * del_o[i] * t_augmented)
                    
                #Compute V' = V + ete * d_t * data
                delta_V = []
                for _ in del_t:
                    delta_V.append(self.lr * _ * np.array(data))
                self.V = self.V + np.array(delta_V)
                
                error = label - o
                
                #increment p
                self.p += 1
                current_cycle_error += np.linalg.norm(error)
            print("Epoch Error", current_cycle_error)
                
        print("Total Epochs required are {} .".format(self.epoch))        
        print("Total Steps required are {} .".format(self.p))
        
        return self
    
    def predict(self, ip, weights):
        net = self.__net_input(np.array(ip),weights)
        return self.__activation(net, deriv = False)
    
    
#%%
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
label = [[0], [1], [1], [0]]

mlp = MLP(X, label, 2, 2, 1, lr = 10)

mlp.train(1000000)
