import os
import math

from typing import Any, Callable, Optional, Tuple, List
from pycocotools.coco import COCO
import cv2

# import glob
import numpy as np

from operator import itemgetter


from PIL import Image
import torch
from torch.utils import data
import torch.distributed as dist
import torch.nn.functional as F
from . import transforms as T
import copy


def build_train_loader(cfg):

    train_transforms = make_transforms(cfg, split='train')
    train_data = CocoDetection(cfg=cfg, split='train', transforms=train_transforms)

    if dist.is_initialized():
        from torch.utils.data.distributed import DistributedSampler
        sampler = DistributedSampler(train_data)
    else:
        sampler =  None

    data_loader = torch.utils.data.DataLoader(train_data,
                        num_workers= cfg.SYS.WORKERS,
                        batch_size=cfg.TRAIN.BATCH_SIZE//len(cfg.SYS.GPUS),
                        collate_fn=collate_fn,
                        shuffle=cfg.DATA.SHUFFLE,
                        pin_memory=cfg.SYS.PIN_MEMORY,
                        drop_last=cfg.DATA.DROP_LAST,
                        sampler=sampler)

    return data_loader

def build_val_loader(cfg):

    val_transforms = make_transforms(cfg,split='val')
    val_data = CocoDetection(cfg=cfg, split='val', transforms=val_transforms)

    if dist.is_initialized():
        from torch.utils.data.distributed import DistributedSampler
        sampler = DistributedSampler(val_data)
    else:
        sampler =  None

    data_loader = torch.utils.data.DataLoader(val_data,
                        num_workers=cfg.SYS.WORKERS,
                        batch_size=cfg.TRAIN.BATCH_SIZE_VAL//len(cfg.SYS.GPUS),
                        collate_fn=collate_fn,
                        shuffle=cfg.DATA.SHUFFLE,
                        pin_memory=cfg.SYS.PIN_MEMORY,
                        sampler=sampler)
    return data_loader

def build_test_loader(cfg):

    val_transforms = make_transforms(cfg,split='val')
    val_data = CocoDetection(cfg=cfg, split='val', transforms=val_transforms)

    if dist.is_initialized():
        from torch.utils.data.distributed import DistributedSampler
        sampler = DistributedSampler(val_data)
    else:
        sampler =  None

    data_loader = torch.utils.data.DataLoader(val_data,
                        num_workers=4,
                        batch_size=2,
                        collate_fn=collate_fn,
                        shuffle=False,)
    return data_loader




def collate_fn(batch):
    """
    Since each image may have a different number of objects, we need a collate function (to be passed to the DataLoader).
    This describes how to combine these tensors of different sizes. We use lists.
    :params 
        batch: an iterable of N sets from __getitem__() // list of N  from __getitem__()
                list of N samples ( tuples( getitem[0], getitem[1], ...) )
    :return: 
        a tensor of images, lists of varying-size tensors of bounding boxes, labels, and difficulties
    """
    batch = list(zip(*batch))
    batch[0] = torch.stack(batch[0], dim=0)
    batch[1] = torch.stack(batch[1], dim=0)

    
    return tuple(batch)