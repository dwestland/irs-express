#!/bin/bash

date

cmd=$1; ! [ -z "$cmd" ] && shift
param1=$1; ! [ -z "$param1" ] && shift

DB_CRED_FILE=/usr/local/etc/db_irsexpress2.conf
BCK_CRED_FILE=/usr/local/etc/backupcred_irsexpress2.conf

TMP_DIR=/mnt/documents/tmp
DOCUMENTS_DIR=/mnt/documents/documents

# source $DB_CRED_FILE
# this provides variables $DBURI, $BACKUP_DIR and $BACKUP_FILE
. $DB_CRED_FILE

# source $BCK_CRED_FILE
# this provides variables $BSERVER, $BUSER, $BPASS, $SFTP_KEY, $BSRVDIR
. $BCK_CRED_FILE


local_db_backup() {
    # just make db dump and store it locally
    echo Backup: $BACKUP_FILE.sql.gz
    # echo pg_dump $DBURI | gzip > $BACKUP_FILE.sql.gz
    pg_dump $DBURI | gzip > $BACKUP_FILE.sql.gz
}

upload_backup() {
    # make backup of DB+all documents and upload
    
    local_db_backup
    
    # pack documents
    BDATE=`date "+%Y-%m-%d-%H-%M"`
        DOCUMENTS_BACKUP=""
    if [ "$1" = "daily" ]; then
        DOCUMENTS_BACKUP=""
    else
        DOCUMENTS_BACKUP=$TMP_DIR/documents-$BDATE.tar.gz
        tar -czf $DOCUMENTS_BACKUP $DOCUMENTS_DIR
    fi
    echo DOCUMENTS_BACKUP: $DOCUMENTS_BACKUP

    KEY=""
    SSHPASS=""
    [ -z $SFTP_KEY ] && SSHPASS="sshpass -p $BPASS"
    [ -z $SFTP_KEY ] || KEY="-i $SFTP_KEY"

    SDATE=`date "+%Y/%m"`
    RMPATH=""
    if [ "$1" = "daily" ]; then
        # SDATE=`date "+%Y/%m"`
        SDATE=`date "+%Y/week_%U"`
        RMPATH=`date -d "-2 weeks" "+%Y/week_%U"`
    elif [ "$1" = "weekly" ]; then
        SDATE=`date "+%Y/%m"`
        RMPATH=`date -d "-3 months" "+%Y/%m"`
    elif [ "$1" = "monthly" ]; then
        SDATE=`date "+%Y/monthly"`
        RMPATH=`date -d "-1 years -6 months" "+%Y/monthly"`
    fi
    SRV_BACKUP_DIR=$BSRVDIR/$SDATE
    [ -z $RMPATH ] || RMPATH=$BSRVDIR/$RMPATH
    echo SRV_BACKUP_DIR: $SRV_BACKUP_DIR
    echo RMPATH: $RMPATH

    # transfer new files
    SFTP_CMD="$SSHPASS sftp -oBatchMode=no -b - -oStrictHostKeyChecking=no $KEY $BUSER@$BSERVER"
    echo mkdir `dirname $SRV_BACKUP_DIR` | $SFTP_CMD
    echo mkdir $SRV_BACKUP_DIR | $SFTP_CMD
    if [ -z $DOCUMENTS_BACKUP ]; then
        # put only db backup
        $SFTP_CMD <<_EOF_
cd $SRV_BACKUP_DIR
put $BACKUP_FILE.sql.gz
bye
_EOF_
    else
        # put documents and db backup
        $SFTP_CMD <<_EOF_
cd $SRV_BACKUP_DIR
put $DOCUMENTS_BACKUP
put $BACKUP_FILE.sql.gz
bye
_EOF_
    fi

    # remove old outdated backups
    if [ -z $RMPATH ]; then
        echo "do not delete"
    else
        echo rmdir $RMPATH | $SFTP_CMD
    fi

    # remove local backup
    [ -z $DOCUMENTS_BACKUP ] || rm $DOCUMENTS_BACKUP
}


case $cmd in
    dblocal)
        local_db_backup
        ;;
    upload_daily)
        upload_backup daily
        ;;
    upload_weekly)
        upload_backup weekly
        ;;
    upload_monthly)
        upload_backup monthly
        ;;
    *)
        echo "ERROR, wrong parameter"
        exit 1
esac
