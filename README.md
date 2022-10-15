# ObjectTracker

## Why I made this
For my senior design project, I am developing a camera system that automatically tracks moving objects and responds to other stimuli like sound and voice commands. The program here is the base for object tracking: it identifies the countour of the largest moving object within the camera frame, draws a box around it, and identifies the centroid of the contoured region. Here's a GIF of the camera following me:

![openCVDemo](https://user-images.githubusercontent.com/56314395/195998302-716a3b5b-f2f0-48c5-8b59-167a6ab00816.gif)

## How to Run
You'll need OpenCV and Numpy in order to run the code. Once you've downloaded the repository, run the following commands in your conda environment

```
pip install opencv-python
pip install numpy
```

From there, you should be able to run the code. Press `esc` to end the program
