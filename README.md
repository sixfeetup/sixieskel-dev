This is the development environment for sixieskel.

If you want to use sixieskel, you can create a virtual and then use pip:

    $ mkvirtualenv sixieskel
    (sixieskel)$ pip install --pre sixieskel --find-links=http://dist.sixfeetup.com/public/

This makes the `templer` command available:

    (sixieskel)$ templer sfu_buildout project-buildout

Development Version
===================

If you want to do some work on sixieskel, you will need to install this dev env:

    $ git clone git@github.com:sixfeetup/sixieskel-dev.git
    $ cd sixieskel-dev
    $ virtualenv env
    $ env/bin/pip install zc.buildout==2.4.0
    $ env/bin/pip install setuptools==18.4
    $ env/bin/buildout

Now templer will be available in the bin directory. If you change an entry_point, you will have to re-run buildout.

An easy way to use the included templer is to source the included addpath.sh script

    $ source addpath.sh
    $ which templer
    /home/clayton/sixfeetup/projects/sixieskel/sixieskel-dev/bin/templer

Now you can use templer as you normally would to test changes to the templates.

    $ cd ~/Desktop
    $ templer sfu_buildout

Pushing Changes
===============

The buildout has a fabfile. Deploy using:

    $ fab deploy

Then update the sixieskel egg with the new versions that were just released, in the setup.py

    install_requires=[
        "sixieskel.policy>=1.1.0",
        "sixieskel.buildout>=1.2.0",
        "sixieskel.theme>=1.1.0",
        "sixieskel.karl>=1.0",
    ],

This will allow for an update of the sixieskel egg to pull down your new changes.

Run fab once more after updating the sixieskel egg to release it.

    $ fab deploy
