# Image-Processing-Project-1

This program stitches multiple images together to create a panorama.

Similar to Google Photos' panorama feature or OpenCV's stitching module, this project aims to implement image stitching from scratch using OpenCV's image processing capabilities.

Will explore how to detect and match keypoints between images, estimate homography, and blend images seamlessly from scratch.

## Contributors

- [Mae](https://github.com/cadrianmae), [Blog](https://imc21348423.wordpress.com/)
- [Noura](https://github.com/nrn5), [Blog](https://c22388271.wordpress.com/)
- [Seán](), [Blog]()

## Prerequisites

- Python 3.13.7 or higher
- pip
- virtualenv (recommended)
- Git (for cloning the repository)
- Git-LFS (for handling large files)
  <https://git-lfs.com/>

## Pipeline Overview

- Load images
- Detect keypoints and compute descriptors using algorithms like SIFT, ORB, etc.
- Match keypoints between images using methods like FLANN or BFMatcher
- Estimate homography using RANSAC to filter outliers
- Warp images based on the estimated homography
- Blend images to create a seamless panorama

## Build Instructions

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/nrn5/Image-Processing-Project-1
   cd Image-Processing-Project-1
   ```
3. Create python virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate # Linux/Mac
   # ./venv/bin/Activate.ps1 # Powershell
   ```
4. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```

## Sources

* [OpenCV\: Introduction to SIFT \(Scale\-Invariant Feature Transform\)](https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html "OpenCV: Introduction to SIFT \(Scale-Invariant Feature Transform\)")
* [OpenCV\: ORB \(Oriented FAST and Rotated BRIEF\)](https://docs.opencv.org/4.x/d1/d89/tutorial_py_orb.html "OpenCV: ORB \(Oriented FAST and Rotated BRIEF\)")
* [OpenCV\: Feature Matching](https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html "OpenCV: Feature Matching")
* [OpenCV\: Feature Matching \+ Homography to find Objects](https://docs.opencv.org/3.4/d1/de0/tutorial_py_feature_homography.html "OpenCV: Feature Matching + Homography to find Objects")
* [OpenCV\: Basic concepts of the homography explained with code](https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html "OpenCV: Basic concepts of the homography explained with code")
