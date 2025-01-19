## Running

### Install
We implement SSA-Co-DETR using [MMDetection V2.25.3](https://github.com/open-mmlab/mmdetection/releases/tag/v2.25.3) and [MMCV V1.5.0](https://github.com/open-mmlab/mmcv/releases/tag/v1.5.0).
The source code of MMdetection has been included in this repo and you only need to build MMCV following [official instructions](https://github.com/open-mmlab/mmcv/tree/v1.5.0#installation).
We test our models under ```python=3.7.11,pytorch=1.11.0,cuda=11.3```. Other versions may not be compatible. 

### Data
Checkpoints: Coming Soon.

Solar Radio Burst Dataset: Coming Soon. We are addressing the long-tail issue of the dataset in our next steps, and the dataset will be made publicly available upon completion (original data source: https://www.e-callisto.org/index.html).

The COCO dataset should be organized as:
```

── annotations
    ├── instances_train2017.json
    │      └── instances_val2017.json
    │── train2017
    └── val2017
      
```

### Training
Train SSA_co_deformable_detr + ResNet-50 with 8 GPUs:
```shell
sh tools/dist_train.sh projects/configs/SSA_co_deformable_detr/SSA_co_deformable_detr_r50_1x_coco.py 8 path_to_exp
```
test:
```shell
sh tools/dist_test.sh projects/configs/SSA_co_deformable_detr/SSA_co_deformable_detr_r50_1x_coco.py 8 path_to_exp
```

