# dokku-flask
This guide shows the most simple, fast, cheap and idiomatic way i found to deploy multiple Python applications to yourdomain.tld

[PLEASE READ IF YOU DONT KNOW HOW DNS WORKS](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-host-name-with-digitalocean)<br>
[PLEASE READ IF YOU DONT KNOW HOW SSH AND DIGITALOCEAN WORKS](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-keys-with-digitalocean-droplets)<br>

1. [Create your Dokku droplet](https://cloud.digitalocean.com/droplets/new?image=dokku-16-04)
2. When your Droplet is up and running visit ip address of your Droplet in your web-browser and finish setup (you can just click finish if you follow this guide)<br>
( [Warning](http://dokku.viewdocs.io/dokku/getting-started/installation/#3-deploy-your-first-application): If you don't complete setup via the web installer (even if you set up SSH keys and virtual hosts otherwise) your Dokku installation will remain vulnerable to anyone finding the setup page and inserting their key.)
3. SSH into your Droplet: `ssh root@yourdroplet_ip_address`

Now you are set, next steps can be reproduced for each new application:

1. Your domain name DNS record A should point to your_droplet_ip_address.
1. Create your application: `dokku apps:create appname` (your appname can be your domain name)
2. Add your domain name to application: `dokku domains:add appname yourdomain.tld`
3. [(Install git first)](https://git-scm.com/downloads) cd into your flask application folder and run:
- `git init .` (creates your git repository)
- `git add .`  (adds all files and folders in current dir to your repository)
- `git commit` (commits changes)
- `git remote add dokku dokku@your_droplet_ip_address:appname` (adds a remote named dokku)
- `git push dokku master` (pushes your application to your droplet)
4. You are done. Try to visit yourdomain.tld in your browser now.
5. If you need SSL [look here](https://github.com/dokku/dokku-letsencrypt).


Default flask application can be found in example_app folder. Nginx config is configured to redirect www version to non-www version.

You need only 3 files (nginx.conf.sigil is [optional](http://dokku.viewdocs.io/dokku/configuration/nginx/) and configured to redirect "www" to "non-www"):
- [Procfile](https://devcenter.heroku.com/articles/procfile)
- [runtime.txt](https://devcenter.heroku.com/articles/python-support#supported-python-runtimes)
- requirements.txt

Make sure your SERVER_NAME in flask app config == yourdomain.tld