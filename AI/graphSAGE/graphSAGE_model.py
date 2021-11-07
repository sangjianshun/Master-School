import random

import torch
import torch.nn as nn
import torch.nn.functional as F


class GraphSAGE(nn.Module):
    def __init__(self, adj_dict):
        super(GraphSAGE, self).__init__()
        self.node2neighbor = adj_dict
        self.sample_neighbor([0,1,2])



    # def forward(self, batch_node,):
    #     graphConv1_output = self.graphConv1(input_x, adj_matrix)
    #     graphConv1_output = F.relu(graphConv1_output)
    #     graphConv2_output = self.graphConv2(graphConv1_output, adj_matrix)
    #     logit = F.log_softmax(graphConv2_output, dim=1)
    #     return logit

    def sample_neighbor(self, batch_node, num_sample = 10):
        neighbor_node = []
        for node in batch_node:
            all_neighbor = self.node2neighbor[node]
            if len(all_neighbor) <= num_sample:
                set(all_neighbor).add(node)
                neighbor_node.append(all_neighbor)
            else:
                all_neighbor = set(random.sample(all_neighbor, num_sample))
                all_neighbor.add(node)
                neighbor_node.append(all_neighbor)
        all_node = set.union(*neighbor_node)
        return neighbor_node, all_node

class SAGELayer(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(SAGELayer, self).__init__()
        self.weight = nn.Parameter(torch.randn((input_dim, output_dim)))
    def forward(self, input_x, adj_matrix):
        output = torch.mm(input_x, self.weight)
        output = torch.mm(adj_matrix, output)
        return output

