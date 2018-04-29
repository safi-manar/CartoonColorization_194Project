# 194Project


### Training With the pre-built model

Using the [Tensorflow pix2pix implementation](https://github.com/affinelayer/pix2pix-tensorflow), we train via:

```
python pix2pix.py   --mode train   --output_dir cartoons_train_large   --max_epochs 200   --input_dir cartoons/AB_combined/train/train   --which_direction BtoA
```

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


----

4. On your local computer in a new terminal, create an SSH tunnel from your computer to the compute node.

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


5. Again, on your local computer, open your browser, and go to: `localhost:6006`.



[1]. https://gist.github.com/mcburton/d80e4395cd82737d3677c570aa31ee40
[2]. https://stackoverflow.com/questions/40106949/unable-to-open-tensorboard-in-browser
