from neural_net.construct import constructor


input_list = [1,2]
label_list = [0.7, 1.2]
hidden_nodes = 2
output_nodes = 2

new_nn = constructor(input_list, label_list, hidden_nodes, output_nodes)

new_nn.weight_sum_ih()

new_nn.weight_sum_oh()

hidden_node_e, input_node_e = new_nn.calc_error()

print('hidden_layer : \n', new_nn.hidden_layer,'\n')
print(new_nn.weights_ih)
print(hidden_node_e, input_node_e)

