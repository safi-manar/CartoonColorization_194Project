# 194Project


-----
## Tips for Training


### Training With the pre-built model (with default L1 loss)

Using the [Tensorflow pix2pix implementation](https://github.com/affinelayer/pix2pix-tensorflow), we train via:

First, make sure you are in the right directory.
`cd $SCRATCH/pix2pix`

Then run the following:

```
python pix2pix.py   --mode train   --output_dir cartoons_train_large   --max_epochs 200   --input_dir cartoons/AB_combined/train/train   --which_direction BtoA
```

### Training With the pre-built model for L2 Loss.

First, make sure you are in the right directory.
`cd $SCRATCH/pix2pix`

Then run the following:

```
python pix2pix_L2.py   --mode train   --output_dir L2_results/cartoons_train_large_L2   --max_epochs 200   --input_dir cartoons/AB_combined/train/train   --which_direction BtoA
```

To test:

```
python pix2pix_L2.py   --mode test   --output_dir L2_results/cartoons_test_large_L2   --input_dir cartoons/AB_combined/val/   --checkpoint L2_results/cartoons_train_large_L2
```

### Training With the Squeezed modified model

First, make sure you are in the right directory.
`cd $SCRATCH/pix2pix`

Then run the following:

```
python pix2pix_squeezed.py   --mode train   --output_dir squeezed_results/cartoons_train_large_squeezed   --max_epochs 200   --input_dir cartoons/AB_combined/train/train   --which_direction BtoA
```

To test:

```
python pix2pix_squeezed.py   --mode test   --output_dir squeezed_results/cartoons_test_large_squeezed   --input_dir cartoons/AB_combined/val/   --checkpoint squeezed_results/cartoons_train_large_squeezed
```

### Continue training from previous checkpoint

To continue training, add the checkpoint flag, like:
```
--checkpoint cartoons_train_large
```

-----
## Generalizables


### Create generalizables

1. Put all `256x256` images in `$SCRATCH/pix2pix/generalizables`, original images in A/ and sketches in B/.
2. Run `python combine_A_and_B_modified.py --fold_A A/ --fold_B B/ --fold_AB AB/`


### Test each model above on generalizables.

Test with default (L1) model:
```
python pix2pix.py   --mode test   --output_dir L1_results/generalized_L1   --input_dir generalizables/AB/test/   --checkpoint cartoons_train_large
```

Test with L2:
```
python pix2pix_L2.py   --mode test   --output_dir L2_results/generalized_L2   --input_dir generalizables/AB/test/   --checkpoint L2_results/cartoons_train_large_L2
```

Test with Squeezed:
```
python pix2pix_squeezed.py   --mode test   --output_dir squeezed_results/generalized_squeezed   --input_dir generalizables/AB/test/   --checkpoint squeezed_results/cartoons_train_large_squeezed
```


-----


## Run TensorBoard remotely on Bridges


1. First, connect to bridges, get into the $SCRATCH directory, and get an interactive compute node.
```
[and@br005 ~]$ cd $SCRATCH/pix2pix
[and@br005 pix2pix]$ interact

A command prompt will appear when your session begins
"Ctrl+d" or "exit" will end your session

[and@r003 pix2pix]$ 
```


2. Then, activate the virtualenv, and get the hostname for this compute node.
```
[and@r003 pix2pix]$ source activate hershal
(hershal) [and@r003 pix2pix]$ 
(hershal) [and@r003 pix2pix]$  hostname
r003.pvt.bridges.psc.edu
```

3. Record the output of the `hostname` command. In my case, it was `r003.pvt.bridges.psc.edu` .


4. Run Tensorboard on the compute node.

```
(hershal) [and@r003 pix2pix]$ tensorboard --logdir=cartoons_train_large/
2018-04-29 18:24:31.276787: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
TensorBoard 1.7.0 at http://r746.pvt.bridges.psc.edu:6006 (Press CTRL+C to quit)
W0429 18:25:02.395599 Reloader tf_logging.py:121] Found more than one graph event per run, or there was a metagraph containing a graph_def, as well as one or more graph events.  Overwriting the graph with the newest event.
W0429 18:25:02.408288 Reloader tf_logging.py:121] Found more than one metagraph event per run. Overwriting the metagraph with the newest event.
W0429 18:25:03.202126 Reloader tf_logging.py:121] Detected out of order event.step likely caused by a TensorFlow restart. Purging 81050 expired tensor events from Tensorboard display between the previous step: 99999 (timestamp: 1524960007.7093787) and current step: 0 (timestamp: 1524961108.1180243).
W0429 18:25:03.283502 Reloader tf_logging.py:121] Found more than one graph event per run, or there was a metagraph containing a graph_def, as well as one or more graph events.  Overwriting the graph with the newest event.
W0429 18:25:03.306437 Reloader tf_logging.py:121] Found more than one metagraph event per run. Overwriting the metagraph with the newest event.
W0429 18:25:04.907786 Reloader tf_logging.py:121] Found more than one graph event per run, or there was a metagraph containing a graph_def, as well as one or more graph events.  Overwriting the graph with the newest event.
W0429 18:25:04.920300 Reloader tf_logging.py:121] Found more than one metagraph event per run. Overwriting the metagraph with the newest event.
W0429 18:25:04.962739 Reloader tf_logging.py:121] Detected out of order event.step likely caused by a TensorFlow restart. Purging 7900 expired tensor events from Tensorboard display between the previous step: 99999 (timestamp: 1524961604.805753) and current step: 0 (timestamp: 1524962102.1517944).
```

----

5. On your local computer in a new terminal, create an SSH tunnel from your computer to the compute node. Edit the command to use the hostname you recorded above.

```
Manars-MacBook-Pro:~ manar$ ssh -L 6006:r003.pvt.bridges.psc.edu:6006 bridges.psc.edu -l and
and@bridges.psc.edu's password: 
Last login: Sun Apr 29 17:41:15 2018 from c-67-169-127-187.hsd1.ca.comcast.net
********************************* W A R N I N G ********************************
You have connected to br006.pvt.bridges.psc.edu 

This computing resource is the property of the Pittsburgh Supercomputing Center. 
It is for authorized use only.  By using this system, all users acknowledge 
notice of, and agree to comply with, PSC polices including the Resource Use 
Policy, available at http://www.psc.edu/index.php/policies. Unauthorized or 
improper use of this system may result in administrative disciplinary action, 
civil charges/criminal penalties, and/or other sanctions as set forth in PSC 
policies. By continuing to use this system you indicate your awareness of and 
consent to these terms and conditions of use.

LOG OFF IMMEDIATELY if you do not agree to the conditions stated in this warning

 

Please contact remarks@psc.edu with any comments/concerns.

********************************* W A R N I N G ********************************
[and@br006 ~]$ 

```

This will open up a new SSH window. Do not close it.


6. Again, on your local computer, open your browser, and go to: `localhost:6006`.



[1]. https://gist.github.com/mcburton/d80e4395cd82737d3677c570aa31ee40

[2]. https://stackoverflow.com/questions/40106949/unable-to-open-tensorboard-in-browser
