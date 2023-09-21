# RERN: Rich Edge Features Refinement Detection Network for Polycrystalline Solar Cell Defect Segmentation

# Citations

If you are using the code/model/data provided here in a publication, please consider citing:

   ```
   @ARTICLE{10125018,
   author={Wang, Chuhan and Chen, Haiyong and Zhao, Shenshen},
   journal={IEEE Transactions on Industrial Informatics}, 
   title={RERN: Rich Edge Features Refinement Detection Network for Polycrystalline Solar Cell Defect Segmentation}, 
   year={2023},
   volume={},
   number={},
   pages={1-12},
   doi={10.1109/TII.2023.3275705}
 } 

```


# PSCDE-Dataset
## Download
You can download the dataset from the following link:

Google drive：

https://drive.google.com/drive/folders/10rFp-gw_dk__c1oPw-wcb4MOYCLvTNL8?usp=drive_link

Baidu drive：

https://pan.baidu.com/s/1sxf-WwjJzDTC_CAuNMHG-A?pwd=3ess 

Extraction code：3ess


**Please note that we own the copyrights to part of original solar cell images and all annotated maps. Their use is RESTRICTED to non-commercial research and educational purposes.**

## Dataset Instructions:
Dataset is crucial for deep learning, and a high-quality dataset can improve the quality of model training and prediction accuracy. Therefore, we aim to construct a high-quality segmentation dataset to promote the high-quality manufacturing of polycrystalline solar cells.

  We construct a polycrystalline solar cell defect edge (PSCDE) dataset, which is the first high-quality solar cell segmentation dataset. We adopt the electroluminescence imaging technique collecting 700 challenging defect images with 512×512 resolution, such as multi-scale defects, occlusion defects, dense tiny defects, low contrast defects, and combination defects. Furthermore, it is a comprehensive dataset containing the main defect categories, including linear cracks, star cracks, scratches, finger interruptions, black cores, fragments, and corners. Moreover, we meticulously annotate all defective edges with the help of multiple experts. The ground truth of PSCDE includes two categories: edge and non-edge. We randomly divide PSCDE into 280 images for the training set, 140 images for the validation set, and 280 images for the testing set and guarantee that each set contains all kinds of defects.








![image](https://github.com/wch313/PSCDE-Dataset/blob/main/PSCDE.jpg)

![image](https://github.com/wch313/PSCDE-Dataset/blob/main/Figure1.jpg)

# News!
## We updated the binary mask label for the PSCDE dataset.

![image](https://github.com/wch313/PSCDE-Dataset/blob/main/Figure2.png)







**If you have any questions, please contact me without hesitation.**
