# RERN: Rich Edge Features Refinement Detection Network for Polycrystalline Solar Cell Defect Segmentation

# Citations

If you are using the code/model/data provided here in a publication, please consider citing:

   ```
   @ARTICLE{10125018,
  author={Wang, Chuhan and Chen, Haiyong and Zhao, Shenshen},
  journal={IEEE Transactions on Industrial Informatics}, 
  title={RERN: Rich Edge Features Refinement Detection Network for Polycrystalline Solar Cell Defect Segmentation}, 
  year={2024},
  volume={20},
  number={2},
  pages={1408-1419},
  keywords={Image edge detection;Photovoltaic cells;Feature extraction;Semantic segmentation;Manufacturing;Informatics;Strips;Attention;defect segmentation;edge detection;solar cell defect edge dataset},
  doi={10.1109/TII.2023.3275705}}

@ARTICLE{10439979,
  author={Wang, Chuhan and Chen, Haiyong and Zhao, Shenshen and Wang, Yining and Cao, Zhen},
  journal={IEEE Internet of Things Journal}, 
  title={A Low-Cost Defect Segmentation System Based On IoT for Large-Scale Photovoltaic Manufacturing}, 
  year={2024},
  volume={},
  number={},
  pages={1-1},
  keywords={Production;Solar power generation;Photovoltaic systems;Image edge detection;Computational modeling;Edge computing;Photovoltaic cells;IoT;AI;Large-Scale Photovoltaic Manufacturing;Efficient Defect Segmentation Model},
  doi={10.1109/JIOT.2024.3366945}}
```

# Update
We have updated the binary mask defect data set based on the defect edge data set. We will upload the evaluated miou indicators later.
## PSCDE_Mask-Dataset
You can download the dataset from the following link:

Google drive：https://drive.google.com/file/d/1DZ9h-nOT0IwaR4TAvogvXvWbHGPoIVSA/view?usp=sharing

Baidu drive：https://pan.baidu.com/s/1u-_m7IoR-s2vQ6SXTnVTdQ?pwd=dhy3 

Extraction code： dhy3


# PSCDE-Dataset
## Download
You can download the dataset from the following link:

Google drive：

https://drive.google.com/file/d/191-lPslUTW4lJeBSF2pAWbYlH8LwhbQ5/view?usp=drive_link

Baidu drive：

https://pan.baidu.com/s/198k79Y7G_Nh5Eo4aT69v_w?pwd=znyb 

Extraction code：znyb 


**Please note that we own the copyrights to part of original solar cell images and all annotated maps. Their use is RESTRICTED to non-commercial research and educational purposes.**

## Dataset Instructions:
Dataset is crucial for deep learning, and a high-quality dataset can improve the quality of model training and prediction accuracy. Therefore, we aim to construct a high-quality segmentation dataset to promote the high-quality manufacturing of polycrystalline solar cells.

  We construct a polycrystalline solar cell defect edge (PSCDE) dataset, which is the first high-quality solar cell segmentation dataset. We adopt the electroluminescence imaging technique collecting 700 challenging defect images with 512×512 resolution, such as multi-scale defects, occlusion defects, dense tiny defects, low contrast defects, and combination defects. Furthermore, it is a comprehensive dataset containing the main defect categories, including linear cracks, star cracks, scratches, finger interruptions, black cores, fragments, and corners. Moreover, we meticulously annotate all defective edges with the help of multiple experts. The ground truth of PSCDE includes two categories: edge and non-edge. We randomly divide PSCDE into 280 images for the training set, 140 images for the validation set, and 280 images for the testing set and guarantee that each set contains all kinds of defects.


![image](https://github.com/wch313/PSCDE-Dataset/blob/main/PSCDE.jpg)

![image](https://github.com/wch313/PSCDE-Dataset/blob/main/Figure1.jpg)









**If you have any questions, please contact me without hesitation.**
