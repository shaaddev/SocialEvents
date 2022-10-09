<h1 style="text-align: center;">Social Events</h1>
<h3 style="text-align: center">Preview<h3/>

<img src="static/images/preview.png" alt="preview"/>

#

# 🛠 Setup

<h3>Install virtual environment</h3>

MacOS:

```
$ python3 -m venv <folder-name>
```

Windows Command Shell:

```
pip install virtualenv
```

#

<h3>Create and Start virtual environment</h3>

MacOS:

```
$ source <folder-name>/bin/activate
```

Windows Command Shell:

```
virtualenv <folder-name>

<folder-name>\Scripts\activate

```

# 💻 Install Django and other requirements

global command:

```
$ pip install -r requirements.txt
```


# ⚙️ Build and run production

Make Migrations

*please look at forms.py in the posts folder before migrating*

#
```
python3 manage.py makemigrations

python3 manage.py migrate
```

Start up Django Server

```
python3 manage.py runserver
```