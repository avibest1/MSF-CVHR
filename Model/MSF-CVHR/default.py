

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from yacs.config import CfgNode as CN

_C = CN()

# common params for NETWORK
_C.MODEL = CN()
_C.MODEL.NAME = 'seg_msffnet'   #'seg_msffnet'
_C.MODEL.PRETRAINED = ''
_C.MODEL.EXTRA = CN(new_allowed=True)

def update_config(cfg, args):
    cfg.defrost()
    cfg.merge_from_file(args)
    cfg.freeze()

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'w') as f:
        print(_C, file=f)

