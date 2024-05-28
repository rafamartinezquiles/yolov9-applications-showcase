# YOLOv9 aplications showcase
Using YOLOv9 along with cutting-edge machine learning frameworks such as Ultralytics, PyTorch, TensorFlow, and OpenCV, and utilizing NVIDIA's CUDA for accelerated computing, to explore various applications including object detection, image segmentation, and real-time video analysis.
![](images/yolo_v9.png)

## Object Detection

```bash
conda create -n <environment_name>
``` 

```bash
conda activate <environment_name>
``` 

```bash
python yolov9_object_detection.py -v path/to/your/video.mp4 -m yolov9e.pt
```

webcam
```bash
python yolov9_object_detection.py -v 0 -m yolov9e.pt
```







## References
- OpenCV: https://opencv.org/
- Ultralytics: https://github.com/ultralytics/ultralytics
- Chien-Yao Wang and Hong-Yuan Mark Liao. YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information. In arXiv preprint arXiv:2402.13616, 2024.
