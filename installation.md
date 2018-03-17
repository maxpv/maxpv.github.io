Those are not instructions but notes for a quick Jupyter notebook setup on a server. I took advantage of the 300€ credit from GoogleCloud. I consider here that the VM instance is already created and configured: [static ip](https://console.cloud.google.com/networking/addresses/list) created (and [firewall rule](https://console.cloud.google.com/networking/firewalls/list?) added for Jupyter's port if you don't use Nginx as a proxy). 
I use here CentOS, if you prefer another distro mind the package manager (`yum` here) in the commands below.

-----

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

----

Nginx's proxy configuration in order to enable interactivity within the notebook:

```
upstream notebook {
    server localhost:8888;
}

server {
    listen       80 default_server;
    listen       [::]:80 default_server;
    server_name  _;
    root         /usr/share/nginx/html;

    location / {
        proxy_pass            http://notebook;
        proxy_set_header      Host $host;
    }
    
    location ~ /api/kernels/ {
        proxy_pass            http://notebook;
        proxy_set_header      Host $host;
        # websocket support
        proxy_http_version    1.1;
        proxy_set_header      Upgrade "websocket";
        proxy_set_header      Connection "Upgrade";
        proxy_read_timeout    86400;
    }
    
    location ~ /terminals/ {
        proxy_pass            http://notebook;
        proxy_set_header      Host $host;
        # websocket support
        proxy_http_version    1.1;
        proxy_set_header      Upgrade "websocket";
        proxy_set_header      Connection "Upgrade";
        proxy_read_timeout    86400;
    }
    
    error_page 404 /404.html;
        location = /40x.html {
    }
    error_page 500 502 503 504 /50x.html;
        location = /50x.html {
    }
}
    
    
```
