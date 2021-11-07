import os
from collections import defaultdict

import numpy as np
import torch
import os
import scipy.sparse as sp


class GenCoreDataset():
    def __init__(self, is_dict = False):
        self.core_dir_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cora")
        self.core_content = "cora.content"
        self.core_cites = "cora.cites"
        self.is_dict = is_dict

    def deal_label(self, all_label):
        all_label_set = set(all_label)
        label2num = {label: i for i, label in enumerate(all_label_set)}
        all_label = torch.tensor(list(map(label2num.get, all_label)))
        return label2num, all_label

    @staticmethod
    def normalization(matrix):
        matrix_sum = np.sum(matrix, axis=1)  # 可以理解为求度矩阵
        diag_vector = 1 / matrix_sum
        diag_vector[np.isinf(diag_vector)] = 0.
        diag_matrix = np.diag(diag_vector)
        matrix = np.dot(diag_matrix, matrix)
        return matrix

    def deal_feature(self, all_feature):
        all_feature = all_feature.astype(np.float)
        all_feature = self.normalization(all_feature)
        return all_feature

    def deal_vertex(self, all_vertex):
        vertex2num = {}
        for i, vertex in enumerate(all_vertex):
            assert vertex not in vertex2num
            vertex2num[vertex] = i
        return vertex2num

    def gen_content(self, file):
        content = np.genfromtxt(file, dtype=np.str)
        self.label2num, all_label = self.deal_label(content[:, -1])
        all_feature = self.deal_feature(content[:, 1:-1])
        self.vertex2num = self.deal_vertex(content[:, 0])

        all_feature = torch.FloatTensor(all_feature)
        all_label = torch.LongTensor(all_label)
        return all_feature, all_label

    def gen_adj_matrix(self, file, is_dict=False):
        cities = np.genfromtxt(file, dtype=np.str)
        # edge = [[self.vertex2num[vertex_i], self.vertex2num[vertex_j]]for vertex_i,vertex_j in cities]
        edge = np.array(list(map(self.vertex2num.get, cities.flatten()))).reshape(cities.shape)
        if not is_dict:
            edge_sp_matrix = sp.coo_matrix((np.ones(len(edge)), (edge[:, 0], edge[:, 1])),
                                           shape=(len(self.vertex2num), len(self.vertex2num)))
            edge_sp_matrix = edge_sp_matrix.toarray()
            edge_sp_matrix += np.eye(len(self.vertex2num))
            edge_sp_matrix = edge_sp_matrix + edge_sp_matrix.T * (edge_sp_matrix.T > edge_sp_matrix) - edge_sp_matrix * (
                        edge_sp_matrix.T > edge_sp_matrix)
            adj_matrix = self.normalization(edge_sp_matrix)

            adj_matrix = torch.FloatTensor(adj_matrix)
            return adj_matrix
        else:
            adj_dict = defaultdict(set)
            for v1, v2 in edge:
                adj_dict[v1].add(v2)
                adj_dict[v2].add(v1)
            return adj_dict

    def gen_index(self):
        idx_train = range(140)
        idx_val = range(200, 500)
        idx_test = range(500, 1500)

        idx_train = torch.LongTensor(idx_train)
        idx_val = torch.LongTensor(idx_val)
        idx_test = torch.LongTensor(idx_test)
        return idx_train, idx_val, idx_test

    def main_process(self):
        content_file_name = os.path.join(self.core_dir_name, self.core_content)
        all_feature, all_label = self.gen_content(content_file_name)

        cities_file_name = os.path.join(self.core_dir_name, self.core_cites)
        adj_matrix = self.gen_adj_matrix(cities_file_name, self.is_dict)

        idx_train, idx_val, idx_test = self.gen_index()

        return all_feature, all_label, adj_matrix, idx_train, idx_val, idx_test


if __name__ == '__main__':
    genCoreDataset = GenCoreDataset()
    all_feature, all_label, adj_matrix, idx_train, idx_val, idx_test = genCoreDataset.main_process()
