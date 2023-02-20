# Django User Account and Project Template

A Django project which implements a custom user model, environment variable configuration (.env), django and auth logging, and a basic project layout.

This allows you to get a Django project up and running quickly, with some recommended features and best practices already configured and ready to use. The custom user model adds a couple of features to be base auth system, makes email a unique field and a minimum length validator for the username.

By default, MySQL is the pre-configured database engine. If your project uses a different database, such as PostgreSQL, you'll need to install any necessary Python packages and update the database settings prior to running the database migrate commands.  

## Features

___

* Custom User Model
  * Recommended when starting a new project with authentication
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

___

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
$ sh setup.sh -n myproject -p /path/to/my_project
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
$ pip3 install -U pip
$ pip3 install -r requirements.txt
$ deactivate
```

**Create a new Django project**

```
$ cd /path/to/my_project
$ source venv/bin/activate
$ django-admin startproject myproject
$ deactivate
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
# will auto create a cert file
(venv) $ python manage.py runserver_plus --cert-file cert.crt

# if created cert file with the setup script
(venv) $ python manage.py runserver_plus --cert-file local.crt --key-file local.key
```

## Usage

___

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

In your projects, you'll most likely have your own index, home and/or dashboard routes. Modify **user/views.py** and delete or move the **user/views.IndexView** and **user/views.HomeView** views. Modify the **user/urls.py** and delete the index and home URLs. Modify the **myproject/settings.py** and update the **LOGIN_REDIRECT_URL** and **LOGOUT_REDIRECT_URL** options.

## Deployment

___

TODO: deployment steps for running your Django project with Apache and mod_wsgi.

## Contributing

___

All contributions are welcome!  
Fork it, create feature branch, commit and push, create pull request.

## License

___

[0BSD](LICENSE.txt)

> Permission to use, copy, modify, and/or distribute this software for any
> purpose with or without fee is hereby granted.

## Acknowledgments

___

* [Custom user model for new projects](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
* [Implement a custom user model](https://learndjango.com/tutorials/django-custom-user-model)
* [Logging user access with signals](https://dbslusser.medium.com/logging-user-access-with-django-signals-dc4ddd3894a9)
