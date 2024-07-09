'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2024-07-06 21:36:37
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2024-07-08 18:14:16
FilePath: /6dpose/GSPose/config/inference_cfg.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
cosim_topk = -1
refer_view_num = 8
DINO_PATCH_SIZE = 14
zoom_image_margin = 0
zoom_image_scale = 224
query_longside_scale = 672
query_shortside_scale = query_longside_scale * 3 // 4

coarse_threshold = 0.05
coarse_bbox_padding = 1.25
finer_threshold = 0.5
finer_bbox_padding = 1.5
enable_fine_detection = True

save_reference_mask = True
#### configure for 3D-GS-Refiner  ####
ROT_TOPK = 1   # single rotation proposal

WARMUP = 10
END_LR = 1e-6
START_LR = 5e-3
# MAX_STEPS = 100
MAX_STEPS = 1000
GS_RENDER_SIZE = 224
EARLY_STOP_MIN_STEPS = 5
EARLY_STOP_LOSS_GRAD_NORM = 1e-4

USE_SSIM = True
USE_MS_SSIM = True

BINARIZE_MASK = False
USE_YOLO_BBOX = True
USE_ALLOCENTRIC = True
APPLY_ZOOM_AND_CROP = True
CC_INCLUDE_SUPMASK = False

