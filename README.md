bazaar
======
------

## Installation and configuration

1.  Install Python, virtualenv and npm.

2.  Make, enter and activate a virtualenv:

        $ virtualenv bazaar --no-site-packages
        New python executable in clientes/bin/python
        Installing setuptools............done.
        $ cd bazaar/
        $ . bin/activate

2.  Clone this repo into a sub-directory of the new virtualenv:

        $ git clone <path/url>
        $ cd app/

3.  Go through the following files, editing as necessary (you can probably skip this):

        `settings/testing.py`
        `settings/development.py`

4.  Symlink the project directory into the virtualenv's `site-packages`:

        $ ln -s `pwd` ../lib/python2.7/site-packages/bazaar

    Replace `python2.7` with the installed version of Python on your machine.

5.  Set the `DJANGO_SETTINGS_MODULE` environment variable now, and on every
    virtualenv activation:

        $ export DJANGO_SETTINGS_MODULE=bazaar.settings.development
        $ echo "!!" >> ../bin/activate

6.  Install the basic project requirements:

        $ easy_install pip
        $ pip install -r requirements/DEVELOPMENT
        $ pip install -r requirements/TESTING
        $ npm install
        $ bower install

    As you edit your `REQUIREMENTS` files, you can run those last commands again;
    `pip` will realise which packages you've added and will ignore those already
    installed.

7. In two terminal instances, run compass watch to compile SASS files on-the-fly, and run the django server:

        $ compass watch

        $ python manage.py runserver
