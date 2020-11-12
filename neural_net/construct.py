import numpy as np

class constructor:
    def __init__(self,input_list, hidden_nodes, output_nodes):
        self.input_list = input_list
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        #initialize weight as all ones matrix with bias
        self.weights_ih = np.random.rand(hidden_nodes, len(input_list))*2 -1
        self.weights_ho = np.random.rand(output_nodes, hidden_nodes)*2 -1
        self.bias_ih = np.ones((hidden_nodes,1))
        self.bias_ho = np.ones((output_nodes,1))

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

        return 1/(1 + np.exp(-x))