#!/bin/bash

CUR_DIR=$(dirname $(readlink -f $0))
WORK_DIR=$CUR_DIR
PROJ_NAME=irsexpress2
LOGDIR=/var/log/irsexpress2
# USER=irs
USER=irsexpress
# debug: user 'irs' was used. Use 'irsexpress' for production
id -u $USER >/dev/null 2>/dev/null
[ $? -eq 0 ] || USER=irs
PYTHON=/usr/bin/python3
CELERY=/usr/local/bin/celery
GUNICORN=/usr/local/bin/gunicorn
GITUSER=ubuntu

# init sudo
sudo echo "" > /dev/null

# create the user if not exists
# [ `id -u $USER 2>/dev/null` ] || echo "$USER:pass123$USER:::::/usr/sbin/nologin" | sudo newusers

cmd=$1; ! [ -z "$cmd" ] && shift
param1=$1; ! [ -z "$param1" ] && shift

checkps=`ps ax | grep gunicorn | grep -v grep | grep -v sudo`
checkdaemons=`ps ax | grep celery | grep -v grep | grep -v sudo`

initsudoecho() {
    # init sudo
    sudo echo "" > /dev/null
}

setup() {
    initsudoecho

    sudo chown -R $USER: $WORK_DIR

    # creating log dir and force set permissions
    [ -d "$LOGDIR" ] && sudo mkdir -p $LOGDIR
    sudo chown -R $USER: $LOGDIR
    sudo chmod -R a+rwX $LOGDIR
    sudo chown -R $GITUSER: $WORK_DIR/.git

    # compile the CoffeeScript files to JavaScript (if possible)
    # which coffee && coffee --compile $WORK_DIR/
}

case $cmd in
    setup)
        setup
        ;;
    start)
        if [ -n "$checkps" ]; then
            echo "gunicorn seems to be already running"
            exit 133
        fi
        setup

        sudo -u $USER sh -c "cd $WORK_DIR; $PYTHON $WORK_DIR/manage.py collectstatic --noinput"
        DAEMONFLAG="-D"
        STARTMSG="daemon"
        [ "$param1" = "--debug" ] && DAEMONFLAG="" && STARTMSG="interactive"
        sudo -u $USER sh -c "cd $WORK_DIR; $PYTHON -W ignore $GUNICORN -c $CUR_DIR/config/gunicorn/gunicorn.conf.py --chdir $WORK_DIR $PROJ_NAME.wsgi:application $DAEMONFLAG"
        if [ $? -ne 0 ]; then
            echo "ERROR starting gunicorn"
            exit 127
        else
            echo "Started $STARTMSG"
        fi
        sudo -u $USER sh -c "cd $WORK_DIR; $CELERY worker -A $PROJ_NAME.settings -D --concurrency=3 --logfile=/var/log/$PROJ_NAME/celery.log --pidfile=/tmp/celery.pid"
        sudo service nginx restart
        ;;
    stop)
        if [ -z "$checkps" ]; then
            echo "gunicorn seems to be already stopped"
            # exit 132
        else
            initsudoecho
            ps ax | grep gunicorn | grep -v grep | grep -v sudo | awk '{print $1}' | xargs -r sudo kill -9
            echo "gunicorn killed"
        fi
        if [ -z "$checkdaemons" ]; then
            echo "Daemons seem to be already stopped"
        else
            initsudoecho
            ps ax | grep celery | grep -v grep | grep -v sudo | awk '{print $1}' | xargs -r sudo kill -9
            echo "Celery processes killed"
        fi
        ;;
    reload)
        ps ax | grep gunicorn | grep -v grep | grep -v sudo | awk '{print $1}' | xargs -r sudo kill -s HUP
        sudo service nginx reload
        ;;
    *)
        echo "ERROR, wrong parameter"
        exit 1
esac
