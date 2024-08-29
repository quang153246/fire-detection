# Fire Detection
This repo is a PoC for using Jetson Nano and camera to detect fire. It follow the guideline https://github.com/dusty-nv/jetson-inference

# Prerequisites
- Hardware: Jetson nano, camera
- Software: python 3.6.9, torch 1.6.0

# Dataset
- Labeling and annotating on Roboflow https://roboflow.com/
- Export to VOC format (refer dataset.rar)

# Training
- Clone the repo at : https://github.com/dusty-nv/jetson-inference
- cd "jetson-inference/python/training/detection/ssd"
- Add dataset folder
- Run: "python3 train_ssd.py --dataset-type=voc --dataset=data/fire --model-dir=models/fire"
After completing the traning process, the model will be stored at models/fire
- Export onnx: "python3 onnx_export.py --model-dir=models/fire"
- Inference with live camera: python3 ssd_inference.py


# Training process
![image](https://github.com/user-attachments/assets/74b9357e-62fc-4dc8-a583-1128365de1db)


# Inference with live cam
![image](https://github.com/user-attachments/assets/2b34a44d-b7f6-4e02-9ec5-9924c6dd70b6)




