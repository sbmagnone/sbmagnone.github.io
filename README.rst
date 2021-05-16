================
Sophia's Website
================

This is the code for Sophia's website!


Installation
------------

1. Download this repository. Open a terminal window, navigate to the parent folder you want this to live in, and ``git clone https://github.com/sbmagnone/sbmagnone.github.io.git``
2. Make sure you've downloaded a recent(ish) version of `Python 3 <http://www.python.org>`_.
3. Install the python dependencies: ``pip3 install -r requirements.txt``

And that should be it!


Development
-----------

To start a local development server, make sure you're in this directory and run ``make devserver``. You'll then be able to see your page at `http://localhost:8000 <http://localhost:8000>`_. Whenever you modify and save a file, you should be to reload the local webpage and see the changes take effect.

To modify or add content, change the files in the ``content`` directory. Blog posts are in ``content/blog/``, while all other (undated) pages are just at the root of ``content``. Non-blog pages will have simple urls like ``/about/`` and, if given an ``order`` parameter, will show up in the main menu navigation. Blog posts will have urls like ``/blog/2021/05/15/cool-stuff/``.


Deployment
----------

When you're satisfied with the changes you've made,

1. kill the development server (``ctrl-c``);
2. regenerate the page using publication settings: ``make publish``; and
3. commit the changes to git. This last one takes a few quick steps:

    a. ``git add .`` to add all unstaged changes
    b. ``git commit -m "description of changes"`` (the commit message can be whatever you want, but is handy to keep track of your work)
    c. ``git push`` to push your changes up to github

Once deployed, you should be able to view your site at `https://sbmagnone.github.io <https://sbmagnone.github.io>`_. (we'll get a custom domain name for it later).
