Change `MyPassword` to any secret password (8 characters max!) and execute this to setup nginx:

```
sudo sh -c "printf \"admin:$(openssl passwd -crypt 5dAJiLe2)\n\" > /etc/nginx/irsexpress2_passwd"
sudo ln -s /opt/irsexpress/config/nginx/irsexpress2.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/irsexpress2.conf /etc/nginx/sites-enabled/
```

Then restart nginx.
