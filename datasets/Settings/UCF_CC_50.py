from easydict import EasyDict as edict


# init
__C_UCF_CC_50 = edict()

cfg_data = __C_UCF_CC_50

__C_UCF_CC_50.TRAIN_SIZE = (512,1024)
__C_UCF_CC_50.DATA_PATH = '../ProcessedData/UCF_CC_50/'
__C_UCF_CC_50.TRAIN_LST = 'train.txt'
__C_UCF_CC_50.VAL_LST =  'val.txt'
__C_UCF_CC_50.VAL4EVAL = 'val_gt_loc.txt'

__C_UCF_CC_50.MEAN_STD = ([0.446139603853, 0.409515678883, 0.395083993673], [0.288205742836, 0.278144598007, 0.283502370119])

__C_UCF_CC_50.LABEL_FACTOR = 1
__C_UCF_CC_50.LOG_PARA = 1.
__C_UCF_CC_50.RESUME_MODEL = ''#model path
__C_UCF_CC_50.TRAIN_BATCH_SIZE = 12 #imgs

__C_UCF_CC_50.VAL_BATCH_SIZE = 1 # must be 1

