Downloading and installing `conda` and installing (the awesome) `jupyterlab`.

```
sudo yum update; sudo yum install bzip2; sudo yum install wget;
cd /tmp;
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh ## probably to be replaced
sh Anaconda3-5.1.0-Linux-x86_64.sh 
source ~/.bashrc
conda update -n base conda
conda install -c conda-forge jupyterlab
jupyter notebook --generate-config
```

Installing `tensorflow`, `keras`, `scikit-learn`and `matplotlib`

```
conda install -c conda-forge keras
conda install -c anaconda tensorflow 
conda install -c anaconda scikit-learn
conda install -c anaconda matplotlib
```
  
Editing ``~/.jupyter/jupyter_notebook_config.py``
```
## Accept all IPs to access to the server
c.NotebookApp.allow_origin = '*'
c.NotebookApp.notebook_dir = '/home/$username$/notebooks/'

## This is not secure but ensure a quick login
## In my case I alway turn off my GCloud instance after usage
c.NotebookApp.password_required = False
c.NotebookApp.token = 'pwd'
```

Launch jupyter lab on startup, by appending in `/etc/rc.d/rc.local`:

```
su - $username$ -c "/home/maxence_prevost/anaconda3/bin/jupyter lab --no-browser"
```
