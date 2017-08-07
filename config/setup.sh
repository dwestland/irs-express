#!/bin/sh

# for automatic run use this line
CUR_DIR=$(dirname $(readlink -f $0))
# this line for manual run only!
CUR_DIR=`pwd`
BASE_DIR=/opt/irsexpress2
LOG_DIR=/var/log/irsexpress2
CFGDIR=/usr/local/etc/
CFGFILE="irsexpress2.yaml"
# PROJ_USER=irs
PROJ_USER=irsexpress
PYTHON=python3
PIP=pip3

sudo adduser $PROJ_USER
sudo adduser $PROJ_USER sudo

# directories/permissions
sudo mkdir -p $BASE_DIR
sudo chown -R $PROJ_USER: $BASE_DIR
sudo chmod -R a+rwX $BASE_DIR
sudo chmod -R -t $BASE_DIR

sudo chmod a+rwX /tmp
sudo chmod -t /tmp

sudo mkdir -p $LOG_DIR
sudo chown -R $PROJ_USER: $LOG_DIR
sudo chmod -R a+rwX $LOG_DIR
sudo chmod -R -t $LOG_DIR

sudo service apache2 stop
sudo update-rc.d -f apache2 disable

sudo apt-get update
sudo apt-get install -y git nginx mc htop
sudo apt-get install -y python3 python3-dev python3-yaml

cd /tmp/
wget https://bootstrap.pypa.io/get-pip.py
sudo $PYTHON get-pip.py
cd -

sudo pip3 install ipython
sudo apt-get install -y libxml2-dev libxslt-dev libjpeg-dev libpng12-dev libfreetype6-dev zlibc zlib1g-dev python3-lxml
sudo apt-get install -y libpq-dev

sudo sh -c "echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' > /etc/apt/sources.list.d/pgdg.list"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y postgresql-client-9.4 postgresql-client-common

sudo apt-get install -y pdftk
sudo apt-get install -y sshpass

cd $BASE_DIR
git clone git@bitbucket.org:irsexpress2develpment/irsexpress2.git ./

# For development server install also:
# sass
# coffee
# npm install

sudo pip3 install -r config/pip/requirements.txt

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s $BASE_DIR/config/nginx/irsexpress2_passwd /etc/nginx/

# Use one of available files depending on server type:

# Development (allowed HTTP):
# sudo ln -s $BASE_DIR/config/nginx/irsexpress2_dev.conf /etc/nginx/sites-available/irsexpress2.conf

# Staging
# sudo ln -s $BASE_DIR/config/nginx/irsexpress2_stage.conf /etc/nginx/sites-available/irsexpress2.conf

# Production
sudo ln -s $BASE_DIR/config/nginx/irsexpress2_prod.conf /etc/nginx/sites-available/irsexpress2.conf


sudo ln -s /etc/nginx/sites-available/irsexpress2.conf /etc/nginx/sites-enabled/

sudo mkdir /etc/nginx/irsexpress2

# HERE: PUT YOUR certificate and its key file in the folder /etc/nginx/irsexpress2
# Certificate should be named: /etc/nginx/irsexpress2/app.irsexpress.com.crt
# Certificate's key should be named: /etc/nginx/irsexpress2/app.irsexpress.com.key

# fix permissions if were broken
sudo chown -R $PROJ_USER: $BASE_DIR
sudo chmod -R a+rwX $BASE_DIR
sudo chmod -R -t $BASE_DIR

# HERE we copy default config file to /usr/local/etc/ - EDIT IT and set correct local settings!
sudo cp $BASE_DIR/config/$CFGFILE $CFGDIR
sudo chown $PROJ_USER: $CFGDIR/$CFGFILE
sudo chmod 660 $CFGDIR/$CFGFILE

echo "from .production import *" > irsexpress2/settings/local.py

# create startup script
sudo ln -s $BASE_DIR/config/init.d/irsexpress2.conf /etc/init.d/irsexpress2
sudo chmod a+x /etc/init.d/irsexpress2
sudo chown root: /etc/init.d/irsexpress2

# The next line - only for development server (uncomment there)
# gulp build

# HERE do *MANUAL* setup your database - create schema, user, permissions
# See ./postgres/db_setup.sh

sudo cp $BASE_DIR/config/backup/db_irsexpress2.conf $CFGDIR/
sudo chown $PROJ_USER: $CFGDIR/db_irsexpress2.conf
sudo chmod 660 $CFGDIR/db_irsexpress2.conf
# HERE: EDIT the file /usr/local/etc/db_irsexpress2.conf !!!
# Set correct credentials for the database!

# HERE execute this command and paste the contents of the file ./crontab/backup to the end in the editor
sudo -u $PROJ_USER sh -c "crontab -e"

sudo -u $PROJ_USER python3 ./manage.py syncdb
sudo -u $PROJ_USER python3 ./manage.py collectstatic --noinput

sudo service nginx restart
sudo service irsexpress2 start

# initially create documents
sudo -u $PROJ_USER python3 ./manage.py update_repos
