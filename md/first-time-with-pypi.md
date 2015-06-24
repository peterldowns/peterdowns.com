Title: How to submit a package to PyPI
Author: Peter Downs
Date: Saturday, November 3, 2012

# How to submit a package to PyPI
-------------------------------

The other month a coworker of mine wanted to distribute
[a small wrapper](http://PyPI.python.org/PyPI/locu/0.1)
he'd written for the [Locu API](http://dev.locu.com/).
Instead of forcing developers to clone his repository, he
wanted them to be able install with a single command:
`pip install locu`. He wasn't sure how to go about this so
I wrote up a quick guide, which I'm publishing below
because I haven't found any other guides for this particular
use case (python library hosted on github).

## What is [PyPI](http://pypi.python.org)?

From the official website:

> **PyPI** — the Python Package Index
> 
> The Python Package Index is a repository of software for the
> Python programming language.

Written something cool? Want others to be able to install it with
`easy_install` or `pip`? Put your code on PyPI. It's a big list of
python packages that you absolutely *must* submit your package to
for it to be easily one-line installable.


## Instructions

The good news is that submitting to PyPI is simple in theory:
just sign up and upload your code, all for free. The bad news
is that in practice it's a little bit more complicated than that.
The *other* good news is that I've written this guide, and that
if you're stuck, you can always refer to
[the official documentation](http://wiki.python.org/moin/CheeseShopTutorial#Submitting_Packages_to_the_Package_Index).

I've written this guide with the following assumptions:

* The module/library/package that you're submitting is called `mypackage`.
* `mypackage` is hosted on [github](http://github.com).

### Create your accounts

On [PyPI Live](http://pypi.python.org/pypi?%3Aaction=register_form) and also
on [PyPI Test](http://testpypi.python.org/pypi?%3Aaction=register_form). You must create an
account in order to be able to upload your code. I recommend using the same email/password for
both accounts, just to make your life easier when it comes time to push.

### Create a `.pypirc` configuration file

This file holds your information for authenticating with PyPI, both the live and the test versions.

```
[distutils] # this tells distutils what package indexes you can push to
index-servers =
  pypi
  pypitest

[pypi]
repository: https://pypi.python.org/pypi
username: {{your_username}}
password: {{your_password}}

[pypitest]
repository: https://testpypi.python.org/pypi
username: {{your_username}}
```

This is just to make your life easier, so that when it comes time to upload you
don't have to type/remember your username and password. Make sure to put this
file in your home folder – its path should be `~/.pypirc`.

*Thanks to [Charlie Hack](https://twitter.com/c_hack) for his feedback on this
section.*

### Prepare your package

Every package on PyPI needs to have a file called `setup.py` at
the root of the directory. If your'e using a markdown-formatted read me file
you'll also need a `setup.cfg` file. Also, you'll want a `LICENSE.txt` file
describing what can be done with your code. So if I've been working on a
library called `mypackage`,  my directory structure would look like this:

```
root-dir/ 	# arbitrary working directory name
  setup.py
  setup.cfg
  LICENSE.txt
  README.md
  mypackage/
    __init__.py
    foo.py
    bar.py
    baz.py
```

Here's a breakdown of what goes in which file:

#### `setup.py`

This is metadata about your library.

```
from distutils.core import setup
setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'A random test lib',
  author = 'Peter Downs',
  author_email = 'peterldowns@gmail.com',
  url = 'https://github.com/peterldowns/mypackage',	# use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)
```

The `download_url` is a link to a hosted file with your repository's code.
Github will host this for you, but only if you
create a [`git tag`](http://git-scm.com/book/en/Git-Basics-Tagging). In your
repository, type: `git tag 0.1 -m "Adds a
tag so that we can put this on PyPI."`. Then, type `git tag` to show a
list of tags — you should see `0.1` in the list. Type `git push --tags origin
master` to update your code on Github with the latest tag information. Github
creates tarballs for download at `https://github.com/{username}/{module_name}/tarball/{tag}`.

#### `setup.cfg`

This tells PyPI where your README file is.
		
```
[metadata]
description-file = README.md
```

This is necessary if you're using a markdown readme file. At upload time, you
may still get some errors about the lack of a readme — don't worry about it.
If you don't **have** to use a markdown README file, I would recommend using
[reStructuredText (REST)](http://sphinx-doc.org/rest.html) instead.
	
#### `LICENSE.txt`

This file will contain whichver license you want your code to have. I tend to
use the [MIT license](http://opensource.org/licenses/MIT).
	
### Upload your package to PyPI Test

Run:

```bash
python setup.py register -r pypitest
```

This will attempt to register your package against PyPI's test server, just to make sure you've
set up everything correctly.

Then, run:

```bash
python setup.py sdist upload -r pypitest
```

You should get no errors, and should also now be able to see your library in the
[test PyPI repository](https://testpypi.python.org/pypi).

### Upload to PyPI Live

Once you've successfully uploaded to PyPI Test, perform the same steps but point to
the live PyPI server instead. To register, run:

```bash
python setup.py register -r pypi
```

Then, run:

```bash
python setup.py sdist upload -r pypi
```

and you're done! Congratulations on successfully publishing your first package!
