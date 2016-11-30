Image Labels
============
We consider images to be one of the two following labels (with integer
matching):

    - negative (0): True negative HT associated image
    - positive (1): True positive HT associated image

The above integers are used with Caffe for integer labels when training.

The ``eval/labels.txt`` file shows the above semantic names in
index order. This would be used by the ``IndexLabelClassifier`` in SMQTK, or
when otherwise interpreting the ``prob`` layer in resulting Caffe-trained CNN
output.

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

Configuration File tweaks
-------------------------
The "solver.prototxt" and "train_val.prototxt" files should be tweaked based
on your machine specifics (e.g. what GPU, if any, is available) and where files
are actually located.

In the "train_val.prototxt":

    - ``batch_size`` should be changed to something appropriate for the task
      and for what your GPU RAM can handle.
    - ``mean_file``, in both TRAIN and TEST data layers, should be changed to
      the image mean binaryproto file to use.
    - ``source``, for both TRAIN and TEST data layers, should be changed to
      correctly point to the files genereted from the jupyter notebooks
      parallel to this README.

In the solver.prototxt:

    - ``test_iter`` should be changed to an integer that, when multiplied by
      the ``batch_size`` parameter above, is less than or equal to the total
      number of TEST phase data provided
    - ``snapshot`` may be changed depending on how often trained model
      snapshots should be taken. For CPU or weaker GPUs, this may be lower and
      for strong GPUs, this may be higher.
    - ``snapshot_prefix`` may be changed if the desired snapshot files should
      be named differently.

Evaluation
==========
The ``eval`` directory contains additional notebooks for evaluating trained
models on new image data. We assume that the new image data has run through
the ``00.data_prep`` notebook in order to generate the ``CP1_data.csv`` file
comtaining the cluster/ad/image relationships.
