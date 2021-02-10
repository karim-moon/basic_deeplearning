import numpy as np


# this is the class for construct a simple neural network with 2 input and 2 hidden node and 2 output
class constructor:
    def __init__(self, input_list, label_list, hidden_nodes, output_nodes):
        self.input_list = input_list
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.label_mat = np.matrix(label_list).T
        # initialize weight as all ones matrix with bias
        self.weights_ih = np.random.rand(hidden_nodes, len(input_list)) * 2 - 1
        self.weights_ho = np.random.rand(output_nodes, hidden_nodes) * 2 - 1
        self.bias_ih = np.ones((hidden_nodes, 1))
        self.bias_ho = np.ones((output_nodes, 1))

    def weight_sum_ih(self):
        input_layer = np.matrix(self.input_list).T
        hidden_layer = self.weights_ih * input_layer + self.bias_ih
        hidden_layer = self.sigmoid(hidden_layer)

        self.hidden_layer = hidden_layer

        return hidden_layer

    def weight_sum_oh(self):
        output = self.weights_ho * self.hidden_layer + self.bias_ho

        output = self.sigmoid(output)
        self.output = output

        return output

    def sigmoid(self, x):

        return 1 / (1 + np.exp(-x))

    # To propagate backward, we should calculate the all error between the node

    def calc_error(self):
        error_mat = self.label_mat - self.output

        # Construct the size of hidden weights to contain the portion of single weight
        error_weight_ho = np.zeros(self.weights_ho.shape)


        for col in range(self.weights_ho.shape[1]):
            for row in range(self.weights_ho.shape[0]):
                error_weight_ho[row][col] = self.weights_ho.T[row][col] / sum(self.weights_ho.T[row])

        hidden_error = error_weight_ho * error_mat

        error_weight_ih = np.zeros((self.weights_ih.shape))

        for col in range(self.weights_ih.shape[1]):
            for row in range(self.weights_ih.shape[0]):
                error_weight_ih[row][col] = self.weights_ih.T[row][col] / sum(self.weights_ih.T[row])

        input_error = error_weight_ih * hidden_error

        return hidden_error, input_error


import
