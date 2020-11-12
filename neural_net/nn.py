from neural_net.construct import constructor


input_list = [1,2,3]
hidden_nodes = 2
output_nodes = 1

new_nn = constructor(input_list, hidden_nodes, output_nodes)

new_nn.weight_sum_ih()

new_nn.weight_sum_oh()

print('hidden_layer : ', new_nn.hidden_layer)
print('output : ', new_nn.output)

