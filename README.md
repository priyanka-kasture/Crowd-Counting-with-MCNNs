# Crowd Counting with MCNNs - MindSpark Hackathon 2018
</br>
Crowd counting on the ShanghaiTech dataset, using multi-column convolutional neural networks.</br>

This is an unofficial implementation of CVPR 2016 paper "Single Image Crowd Counting via Multi Column Convolutional Neural Network". </br>

# Installation
- Install Tensorflow and Keras </br>
- Install OpenCV </br>
- Clone this repository (in case you don't want train the model and want to use the pre-trained one).</br>

# Data Setup

Download ShanghaiTech Dataset from: </br>
- Dropbox: https://www.dropbox.com/s/fipgjqxl7uj8hd5/ShanghaiTech.zip?dl=0 </br>
- Baidu Disk: http://pan.baidu.com/s/1nuAYslz </br>
</br>
Create a folder: ROOT/data/original/shanghaitech/ </br>
</br>
Here ROOT is the folder conatining all files, it's the main folder. (Don't create a folder called ROOT!)</br>

- Save "part_A" under ROOT/data/original/shanghaitech/</br>
- Save "part_B" under ROOT/data/original/shanghaitech/</br>
- Got to ROOT/data_preparation/ </br>
- There, run create_gt_test_set_shtech.m in matlab/octave to create ground truth files for test data. </br>
- Then go to ROOT/data_preparation/ again.</br>
- run create_training_set_shtech.m in matlab to create training and validataion set along with ground truth files. </br>
</br>
- Save the ground truth csv files in ROOT/data/</br>
That completes data-setup!
</br>

# Test

- Follow steps 1, 2, 3, 4 and 5 from Data-Setup. </br>
- Download pre-trained model files: </br>
[Shanghai Tech A] : https://www.dropbox.com/s/8bxwvr4cj4bh5d8/mcnn_shtechA_660.h5?dl=0 </br>
[Shanghai Tech B] : https://www.dropbox.com/s/kqqkl0exfshsw8v/mcnn_shtechB_110.h5?dl=0 </br>
</br>
- Save the model files under: ROOT/final_models
</br>
- Finally run: test.py </br>
</br>

# Train

- Not recommended unless you have a great processor, or a GPU, because training takes a lot of time. Load the pre-trained model and test it on the test set instead. </br>

- For tensorflow: </br>
run from prompt: python3 train.py A(or B) </br>
Model is saved to modelA/ or modelB/. </br>

- For keras:
run: python3 keras_train.py B </br>
model is saved to keras_modelB/ </br>
