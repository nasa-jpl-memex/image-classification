Image Labels
============
We consider images to be one of the two following labels (with integer
matching):

    - negative (0): True negative HT associated image
    - positive (1): True positive HT associated image

The above integers are used with Caffe for integer labels when training.

Caffe Finetuning
================
Copy the "alexnet_adam" directory into your workspace.
This directory contains the configuration files for Caffe.

A base model will be required as a base to fine-tune from.
The "alexnet_adam" configuration files included want to use the "bvlc_alexnet"
model that can be retrieved from the standard Caffe model-zoo or from
"caffe/src/models/bvlc_alexnet/bvlc_alexnet.caffemodel".
The model file used may also be a previously fine-tuned model in order to fine-
tune even further.

This configuration also specified the use of an image mean.
The "alexnet_adam" configuration should use the the
"caffe/src/ilsvrc12/imagenet_mean.binaryproto" image mean (set to the next to
the "train_val.prototxt" file).
