## Running

### Install
We implement SSA-Co-DETR using [MMDetection V2.25.3](https://github.com/open-mmlab/mmdetection/releases/tag/v2.25.3) and [MMCV V1.5.0](https://github.com/open-mmlab/mmcv/releases/tag/v1.5.0).
The source code of MMdetection has been included in this repo and you only need to build MMCV following [official instructions](https://github.com/open-mmlab/mmcv/tree/v1.5.0#installation).
We test our models under ```python=3.7.11,pytorch=1.11.0,cuda=11.3```. Other versions may not be compatible. 

### Data
Checkpoints: https://drive.google.com/file/d/1WUSyoPWeNq98HH8me8kl5qTfW9_bnORN/view?usp=drive_link.

Solar Radio Burst Dataset: https://drive.google.com/file/d/1v3zkDgHatldortmoB8QE6Xw2NcyPOaU3/view?usp=drive_link. We are addressing the long-tail issue of the dataset in our next steps, and the dataset will be made publicly available upon completion (original data source: https://www.e-callisto.org/index.html).

The COCO dataset should be organized as:
```

── annotations
    ├── instances_train2017.json
    │      └── instances_val2017.json
    │── train2017
    └── val2017
      
```
###Get more data
In this article, we only collected solar radio bursts from August 2020 to August 2022. If you need more data, we provide a crawler script so that you can get more data.
Run the following code:
```shell
python spider/spider-1.py
```

### quick test
```shell
mkdir ck
cd ck
weget https://drive.google.com/file/d/1WUSyoPWeNq98HH8me8kl5qTfW9_bnORN/view?usp=drive_link.
python tools/train.py projects/configs/SSA_co_deformable_detr/SSA_co_deformable_detr_r50_1x_coco.py ck/SSA-Co-DETR.pth
```

### Training
Train SSA_co_deformable_detr + ResNet-50 :
```shell
python tools/train.py projects/configs/SSA_co_deformable_detr/SSA_co_deformable_detr_r50_1x_coco.py
```
test:
```shell
python tools/test.py projects/configs/SSA_co_deformable_detr/SSA_co_deformable_detr_r50_1x_coco.py
```

