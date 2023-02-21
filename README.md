# Django User Account and Project Template

A Django project which implements a custom user model, environment variable configuration (.env), django and auth logging, and a basic project layout.

This allows you to get a Django project up and running quickly, with some recommended features and best practices already configured and ready to use. The custom user model adds a couple of features to the base auth system: makes email a unique field and a minimum length validator for the username.

By default, MySQL is the pre-configured database engine. If your project uses a different database, such as PostgreSQL, you'll need to install any necessary Python packages and update the database settings prior to running the database migrate commands.  

## Features

* Custom User Model
  * Recommended when starting a new project using authentication
* django-environ
  * Settings are pre-configured to use the provided .env file
* django-extensions
  * Provides HTTPS support when running the development server
* Logging Configuration
  * By default, django and user authentication are logged to separate files
* PyMySQL
  * Using pymysql.install_as_MySQLdb() in place of mysqlclient
* Werkzeug
  * Provides enhanced debugging and HTTPS support for development purposes

See [usage](#usage) for details on project layout and resources.

## Getting Started

The following instructions will get you a new Django project up and running on your local machine for development purposes. See [deployment](#deployment) on how to deploy for a production system.

### Prerequisites

Basic knowledge of Linux/Unix systems and the Django web framework.

* Access to a Linux/Unix machine, with the following packages installed:
  * python3
  * pip3
  * openssl

### Installation

A setup script is provided for automatic installation. See [manual installation](#manual-installation) for specific installation steps. See [post installation](#post-installation) for steps to take after install.

Create two directories, one for cloning down the repo and one for your Django project.

```
$ mkdir django_user_account
$ mkdir my_project
$ cd django_user_account
$ git clone https://github.com/stiknine/django-user-account.git .
```

Run the setup script, passing in your Django project name and path to your project directory.

```
$ source setup.sh -n myproject -p /path/to/my_project
```

### Manual Installation

**Create project directories and clone the repo**

```
$ mkdir django_user_account
$ mkdir my_project
$ cd django_user_account
$ git clone https://github.com/stiknine/django-user-account.git .
```

**Create a Python virtual environment for your project**

```
$ cd /path/to/my_project
$ cp /path/to/django_user_account/requirements.txt .
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -U pip
(venv) $ pip3 install -r requirements.txt
(venv) $ deactivate
```

**Create a new Django project**

```
$ cd /path/to/my_project
$ source venv/bin/activate
(venv) $ django-admin startproject myproject
(venv) $ deactivate
```

**Copy over the project files from the repo**

```
$ cd myproject
$ cp -R /path/to/django_user_account/account/user .
$ cp -R /path/to/django_user_account/account/templates .
$ cp -R /path/to/django_user_account/account/static .
$ cp -R /path/to/django_user_account/account/.env.dist myproject/
$ cp -R /path/to/django_user_account/account/.env.dist myproject/.env
$ cp -R /path/to/django_user_account/account/urls.py myproject/
$ cp -R /path/to/django_user_account/account/settings.py myproject/
```

You'll need to modify the **settings.py** file and update the **ROOT_URLCONF** and **WSGI_APPLICATION** options.

**Change**:  
`ROOT_URLCONF = 'account.urls'` *to* `ROOT_URLCONF = 'myproject.urls'`

**Change**:  
`WSGI_APPLICATION = 'account.wsgi.application'` *to* `WSGI_APPLICATION = 'myproject.wsgi.application'`

### Post Installation

**Create a database for your project**

**NOTE**: If not using MySQL as your database engine, install any necessary python packages and update the **DATABASES** option in the **settings.py** file. Make these changes prior to running the migrate commands.

Modify the **myproject/.env** file with your configuration options.

**Run database migrations**

```
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

**Run development server**

```
(venv) $ python manage.py runserver_plus --cert-file cert.crt
```

## Usage

After install there will be a set of resources available to use in your projects or easily replaced. A basic layout with index, home, login and register pages. Some basic CSS styles for a clean looking layout, forms and messages.

**URL Routes**:

```
/ (index)
/home/ (home, redirected to after login)
/register/ (account registration)
/login/ (user login)
/admin/ (django admin site)
```

**Project Layout**:

```
├── myproject/
│   ├── myproject/
│   ├── static/
│   │   ├── css/style.css
│   │   ├── img/
│   │   └── js/
│   ├── templates/
│   │   ├── forms/errors.html
│   │   ├── registration/
│   │       ├── login.html
│   │       └── register.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── index.html
│   │   └── nav.html
│   ├── user/
│   └── manage.py
├── log/
│   ├── auth.log
│   └── django.log
├── venv/
├── requirements.txt
└── .gitignore
```

In your projects, you'll most likely have your own index, home and/or dashboard routes.

* Modify **user/views.py** and delete or move the **user/views.IndexView** and **user/views.HomeView** views.
* Modify the **user/urls.py** and delete the index and home URLs.
* Modify the **myproject/settings.py** and update the **LOGIN_REDIRECT_URL** and **LOGOUT_REDIRECT_URL** options.

## Tests

The project includes a few basic tests. To run them, first create a test database and modify the **.env** file to update the **DATABASE_TEST** option with your test database name.

**Run tests**

```
(venv) $ python manage.py test --keepdb
```

## Deployment

The following instructions will help you deploy your Python web application in a production environment.

### Apache and mod_wsgi

There is an example [Apache conf](server/apache/user-account-ssl.conf) provided in the repo. Skip any steps if you already have the packages installed and configured.

**Install Apache, mod_wsgi and Python packages**  

```
$ sudo apt install openssl
$ sudo apt install mysql-client
$ sudo apt install python3-dev python3-venv python3-distutils python3-pip net-tools
$ sudo apt install apache2 apache2-utils libapache2-mod-wsgi-py3 ssl-cert
```

**Allow Apache through the firewall**

```
$ sudo ufw app list
$ sudo ufw allow 'Apache Full'
```

**Enable Apache ssl and wsgi mods**

```
$ sudo a2enmod ssl
$ sudo a2enmod wsgi
```

**Set up and configure application**

```
$ sudo mkdir /var/www/my_project
$ sudo chown www-data:www-data /var/www/my_project
$ sudo chmod 770 /var/www/my_project
```

Copy over your application files, using whatever method available to you.

```
$ cp /path/to/application/* /var/www/my_project/
$ cd /var/www/my_project
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -U pip
(venv) $ pip3 install -r requirements.txt
(venv) $ cd myproject/
```

Modify the **myproject/.env** file with your configuration options.

**NOTE**: debug must to disabled, allow hosts needs to include your fully qualified domain name "FQDN", a secret key needs to be generated, static root needs to be set.

Run to generate a secret key.

```
(venv) $ python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

.env file.

```
DEBUG=False
ALLOWED_HOSTS='127.0.0.1,localhost,<FQDN>'
SECRET_KEY='<generated secret key>'
STATIC_ROOT='/var/www/my_project/static/'
```

Collect static files.

```
(venv) $ python manage.py collectstatic
(venv) $ deactivate
```

Configure Apache. Get a copy of the example [Apache conf](server/apache/user-account-ssl.conf) and modify it for your application.

```
ErrorLog ${APACHE_LOG_DIR}/myproject-error.log
CustomLog ${APACHE_LOG_DIR}/myproject-access.log combined

WSGIDaemonProcess myproject python-home=/var/www/my_project/venv python-path=/var/www/my_project/myproject processes=2 threads=5
WSGIScriptAlias / /var/www/my_project/myproject/myproject/wsgi.py
WSGIProcessGroup myproject

<Directory "/var/www/my_project/myproject/myproject">
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

Alias "/static/" "/var/www/my_project/static/"
<Directory "/var/www/my_project/static">
    Options -Indexes +FollowSymLinks +MultiViews
    Require all granted
</Directory>
```

Enable your application.

```
$ sudo cp /path/to/myproject-ssl.conf /etc/apache2/sites-available/
$ sudo a2ensite myproject-ssl.conf
$ sudo systemctl restart apache2
```

If everything worked as expected, your site should be running and available.

Log files located at:

* /var/log/apache2/
  * myproject-access.log
  * myproject-error.log
* /var/www/my_project/log/
  * auth.log
  * django.log

### Nginx and uWSGI

Instructions to come...

### Log Rotation

Instructions to come...

## Contributing

All contributions are welcome!  
Fork it, create feature branch, commit and push, create pull request.

## License

[0BSD](LICENSE.txt)

> Permission to use, copy, modify, and/or distribute this software for any
> purpose with or without fee is hereby granted.

## Acknowledgments

* [Custom user model for new projects](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
* [Implement a custom user model](https://learndjango.com/tutorials/django-custom-user-model)
* [Logging user access with signals](https://dbslusser.medium.com/logging-user-access-with-django-signals-dc4ddd3894a9)
