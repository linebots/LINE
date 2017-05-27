LINE
----

[![Join the chat at https://gitter.im/carpedm20/LINE](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/carpedm20/LINE?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

- Documentation : [http://carpedm20.github.io/line/](http://carpedm20.github.io/line/)
- Developer Mailing List: [Google Group](https://groups.google.com/forum/#!forum/line-python-developer)

*May the LINE be with you...*


Installation
------------

**2017.05.27

Install Python:

This project requires Python 2. It will not run under the latest Python 3. If you have Python 3 installed, it's not a problem. You may have multiple versions installed side-by-side. The latest version of Python 2 can be downloaded for all platforms [here](https://www.python.org/downloads/).

Linux users installing Python from a repository should be sure to install the `pip` package. Typically something like `python27` and `python27-pip`.


Install LINE from repository:

The LINE library has a number of dependencies. The easiest way to install them is through the use of a Python package manager such as `pip` or `easy_install`.

    pip install LINE


Install LINE from source:

Alternatively, you may wish to install the LINE library from the source files.

    git clone https://github.com/Nilpo/LINE.git
    cd LINE
    python config.py
    python setup.py install


Uninstall Newer Versions of Apache Thrift:

Whichever method you used to install LINE, you will have installed Apache Thrift as a dependency. The current version Thrift 0.10.0 is unsupported and needs to be downgraded to Thrift 0.9.3.

    pip uninstall thrift
    pip install thrift==0.9.3


Update
------

**2015.05.28**

`sendImage` and `sendImageWithURL` is fixed.

To send an Image:

    >>> contact = client.contacts[0]
    >>> contact.sendImage('./image.jpg')

Or use:

    >>> contact = client.contacts[0]
    >>> contact.sendImageWithURL('https://avatars3.githubusercontent.com/u/3346407?v=3&s=460')


**2015.03.31**

authToken expiration [issue](https://github.com/carpedm20/LINE/issues/9) solved.

update authToken **automatically**:

    $ pip install line --upgrade

There is nothing to change in your original code.

update authToken **manually**:

    $ pip install line --upgrade
    $ python
    >>> from line import LineClient, LineGroup, LineContact
    >>> client = LineClient("ID", "PASSWORD")
    >>> client.updateAuthToken() # manual update
    True


**2014.08.08**

Some codes are removed because of the request of LINE corporation. You can use library only with `authToken` login.


Screenshot
----------

![alt_tag](http://3.bp.blogspot.com/-FX3ONLEKBBY/U9xJD8JkJbI/AAAAAAAAF2Q/1E7VXOkvYAI/s1600/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2014-08-02+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+10.47.15.png)


Author
------

Taehoon Kim / [@carpedm20](http://carpedm20.github.io/about/)
