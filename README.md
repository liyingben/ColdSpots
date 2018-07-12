
<h1 align="center">Cold Spots</h1>

<p align="center">
<a href="https://sinai-survey.tk">
<img src="https://i.imgur.com/0ccpCe0.jpg" height="150" />
</a>
</p>

This repository contains all code necessary to reproduce cold spot results.

Clone the repository along with all submodules:

```
git clone --recursive https://github.com/ArnholdInstitute/ColdSpots.git
```

# Installation

```
virtualenv venv
source venv/bin/activate



pip install -r requirements.txt

# if the above gives you a certificate error execute
# curl https://bootstrap.pypa.io/get-pip.py | python

git submodule update --init --recursive


```




### Tensorbox

Build the C++ auxilary functions:

```
cd TensorBox/utils 
make 
make hungarian

### if the above throws an error, find the path of nsync_cv.h and nsync_mu.h inside the venv folder and find mutex.h
### (should be at /venv/local/lib/python2.7/site-packages/tensorflow/include/tensorflow/core/platform/default 
### or rather you can look at the error message). In the mutex.h folder you will see it says include nysnc_cv.h
### and nsync_mu.h. replace these with the appropriate file paths. Then do 'make hungarian'.


```

If you want to run on a GPU, you'll also need to `pip install tensorflow-gpu`.

# Inference

Below is an example of how to get the bounding boxes for each building within an image:

```
python .\demo.py
```

# Training

```
python .\train.py
```
# Model Description

```
This model is very unexpected. First the image is passed through google_net. Then the output
of one of the earlier layers is taken and input into a 5 step multi-level RNN. The outputs are 
supposed to be potential location of boxes and also confidences. The loss function is the hungarian 
loss. One could look for reference to this paper: https://arxiv.org/pdf/1506.04878.pdf
```
