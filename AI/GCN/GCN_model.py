import torch
import torch.nn as nn
import torch.nn.functional as F

class GCN(nn.Module):
    def __init__(self, feature_dim, hidden_dim, label_dim):
        super(GCN, self).__init__()
        self.graphConv1 = GraphConv(feature_dim, hidden_dim)
        self.graphConv2 = GraphConv(hidden_dim, label_dim)

    def forward(self, input_x, adj_matrix):
        graphConv1_output = self.graphConv1(input_x, adj_matrix)
        graphConv1_output = F.relu(graphConv1_output)
        graphConv2_output = self.graphConv2(graphConv1_output, adj_matrix)
        logit = F.log_softmax(graphConv2_output, dim=1)
        return logit

class GraphConv(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(GraphConv, self).__init__()
        self.weight = nn.Parameter(torch.randn((input_dim, output_dim)))
    def forward(self, input_x, adj_matrix):
        output = torch.mm(input_x, self.weight)
        output = torch.mm(adj_matrix, output)
        return output
