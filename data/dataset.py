import os
from glob import glob
import numpy as np
import random
import torch
from torch.utils import data


class Dataset(data.Dataset):
    def __init__(self, cfg):
        '''
        set variables for dataset
            ex) list of dataset file path, augmentation, ... 
        '''
        
        self.cfg = cfg
        self.filenames = []


    def len(self):
        '''
        return length of this dataset
        Dataset.len() = number of dataset for 1 epoch
        '''
        return len(self.filenames)


    def __getitem__(self, index):
        '''
        return input, target
            input: [B, C, H, W]
            target: [B, shape of target]
        '''
        return 1