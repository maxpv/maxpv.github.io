```
sudo yum update; sudo yum install bzip2; sudo yum install wget;
cd /tmp;
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
sh Anaconda3-5.1.0-Linux-x86_64.sh 
source ~/.bashrc
conda update -n base conda
conda install -c conda-forge jupyterlab
jupyter notebook --generate-config
```

Editing ``~/.jupyter/jupyter_notebook_config.py``

Launch jupyter lab on startup.
