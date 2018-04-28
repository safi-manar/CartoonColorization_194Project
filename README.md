# 194Project


### Training With the pre-built model

Using the [Tensorflow pix2pix implementation](https://github.com/affinelayer/pix2pix-tensorflow), we train via:

```
python pix2pix.py   --mode train   --output_dir cartoons_train_large   --max_epochs 200   --input_dir cartoons/AB_combined/train/train   --which_direction BtoA
```

