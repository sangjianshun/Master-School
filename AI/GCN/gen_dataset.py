import os
import numpy as np

class GenCoreDataset():
    def __init__(self):
        self.core_dir_name = "../GCN/dataset/cora"
        self.core_content = "cora.content"

    def gen_content(self, file):
        content = np.genfromtxt(file, dtype=np.dtype(str))

        print(1)

    def main_process(self):
        content_file_name = os.path.join(self.core_dir_name,self.core_content)
        self.gen_content(content_file_name)

if __name__ == '__main__':

    genCoreDataset = GenCoreDataset()
    genCoreDataset.main_process()