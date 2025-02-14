# ------------------ Model Config ----------------------
from .yolov1_config import yolov1_cfg
from .yolov2_config import yolov2_cfg
from .yolov3_config import yolov3_cfg
from .yolov4_config import yolov4_cfg
from .yolov7_config import yolov7_cfg
from .yolov8_config import yolov8_cfg
from .yolox_config import yolox_cfg


def build_model_config(args):
    print('==============================')
    print('Model: {} ...'.format(args.model.upper()))
    # YOLOv1
    if args.model == 'yolov1':
        cfg = yolov1_cfg
    # YOLOv2
    elif args.model == 'yolov2':
        cfg = yolov2_cfg
    # YOLOv3
    elif args.model == 'yolov3':
        cfg = yolov3_cfg
    # YOLOv4
    elif args.model == 'yolov4':
        cfg = yolov4_cfg
    # YOLOv7
    elif args.model in ['yolov7_nano', 'yolov7_tiny', 'yolov7_large', 'yolov7_huge']:
        cfg = yolov7_cfg[args.model]
    # YOLOv8
    elif args.model in ['yolov8_nano', 'yolov8_small', 'yolov8_medium', 'yolov8_large', 'yolov8_huge']:
        cfg = yolov8_cfg[args.model]
    # YOLOX
    elif args.model == 'yolox':
        cfg = yolox_cfg

    return cfg


# ------------------ Transform Config ----------------------
from .transform_config import (
    yolov5_strong_trans_config, yolov5_weak_trans_config, yolov5_nano_trans_config,
    ssd_trans_config
)

def build_trans_config(trans_config='ssd'):
    print('==============================')
    print('Transform: {}-Style ...'.format(trans_config))
    # SSD-style transform 
    if trans_config == 'ssd':
        cfg = ssd_trans_config

    # YOLOv5-style transform 
    elif trans_config == 'yolov5_strong':
        cfg = yolov5_strong_trans_config
    elif trans_config == 'yolov5_weak':
        cfg = yolov5_weak_trans_config
    elif trans_config == 'yolov5_nano':
        cfg = yolov5_nano_trans_config
        
    return cfg
