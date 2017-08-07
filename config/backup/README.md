
Copy files `backupcred_irsexpress2.conf` and `db_irsexpress2.conf` to the folder `/usr/local/etc/` and edit to have correct values.

Generate SSH keypair to access SFTP.

```
sudo ssh-keygen -f /usr/local/etc/backupsftp_key -N ""
```

Add this file `/usr/local/etc/backupsftp_key.pub` to SFTP's `/home/<user>/.ssh/authorized_keys` file.
