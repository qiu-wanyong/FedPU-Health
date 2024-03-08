# FedPU-Health
The Code of Abnormal Heart Sound Detection from Multi-federated Care Institutions with Only Positive and Unlabelled Data.

Article Title: “Federated Abnormal Heart Sound Detection with Weak to No Labels”

## Abstract
Cardiovascular diseases are a prominent cause of mortality, emphasising the need for early prevention and diagnosis. Utilising artificial intelligence (AI) models, the analysis of heart sounds emerges as a non-invasive and universally applicable approach to assessing cardiovascular health conditions. Yet, real-world medical data is dispersed across institutions, forming "data islands" due to limiting data sharing for security reasons. To this end, federated learning (FL) has been extensively employed in the medical field, which can effectively model across multiple institutions. Additionally, conventional supervised binary classification methods necessitate two completely labelled data classes, such as positive and negative samples. Nevertheless, the process of labelling healthcare data is time-consuming and labor-intensive, leading to the possibility of mislabelling negative samples. In this study, we introduce a naive positive-unlabelled (PU) learning strategy into the FL framework. The constructed semi-supervised FL model can directly learn from a limited set of positive samples and an extensive pool of unlabelled samples. Our emphasis is on vertical FL to enhance collaboration among institutions with diverse feature spaces. Additionally, our contribution extends to the analysis of feature importance, where we explore six methods and offer practical recommendations for detecting abnormal heart sounds. The study demonstrated an impressive accuracy of 84%, comparable to outcomes in supervised learning, thereby advancing the application of FL in abnormal heart sound detection.  

#### Index Terms— Federated learning, Heart sound, positive-unlabelled, semi-supervised, Privacy protection

## Data
Preparation and Analysis of the Signals for [PhysioNet/CinC Challenge Dataset.](https://physionet.org/content/challenge-2016/1.0.0/) Common acoustic signal features are extracted through the openSMILE toolkit and are used for FL models.

<div align="center">
<img src="/Fig1_data_pre.png" width="600" height="300">
</div>
<div align="center">Fig.1 Illustration of pre-processing for heart sound recordings.</div>

## Files
``Configuration file in FATE:`` Related configuration files in FATE.

``Feature_analysis:`` We applied six distinct feature importance analysis methods—`gain`, `total_gain`, `cover`, `total_cover`, `weight`, and `SHAP`—to assess their respective contributions to the model.

``Merge.py, xgFeature.py:`` We set up a set of baseline models based on data-centralised learning.

``Vertically_split.py:`` We vertically partition the preprocessed dataset, gearing up for the vertical-SecureBoost model with PU learning.

## Remarks

The classifier's objective is to label the unlabelled samples within the masked segment and accurately classify the unmasked positive samples.

## Contact

Please contact the authors of this work if you have any questions or comments.

## Cite As
Wanyong Qiu, Chen Quan, Yongzi Yu, Eda Kara, Kun Qian*, Bin Hu*, Bjoern W. Schuller and Yoshiharu Yamamoto, “Federated Abnormal Heart Sound Detection with Weak to No Labels”, Cyborg and Bionic Systems, pp. 1-22, Submitted, October 2023.
