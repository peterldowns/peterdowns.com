Title: How to submit a package to PyPI
Author: Peter Downs
Date: Saturday, November 3, 2012

# How to submit a package to PyPI
-------------------------------

The other month a coworker of mine wanted to distribute
[a small wrapper](http://pypi.python.org/pypi/locu/0.1)
he'd written for the [Locu API](http://dev.locu.com/).
Instead of forcing developers to clone his repository, he
wanted them to be able install with a single command:
`pip install locu`. He wasn't sure how to go about this so
I wrote up a quick guide, which I'm publishing below
because I haven't found any other guides for this particular
use case (python library hosted on github).

## What is [PyPi](pypi.python.org)?

From the official website:

> **PyPI** -- the Python Package Index
> 
> The Python Package Index is a repository of software for the
> Python programming language.

Written something cool? Want others to be able to install it with
`easy_install` or `pip`? Put your code on PyPi. It's a big list of
python packages that you absolutely *must* submit your package to
for it to be easily one-line installable.


## Instructions

The good news is that submitting to PyPi is simple in theory:
just sign up and upload your code, all for free. The bad news
is that in practice it's a little bit more complicated than that.
The *other* good news is that I've written this guide, and that
if you're stuck, you can always refer to
[the official documentation](http://wiki.python.org/moin/CheeseShopTutorial#Submitting_Packages_to_the_Package_Index).

I've written this guide with the following assumptions:

* The module/library/package that you're submitting is called `mypackage`.
* `mypackage` is hosted on [github](http://github.com).

Cool? Cool.

### Creating your account

On [PyPi Live](http://pypi.python.org/pypi?%3Aaction=register_form) and also
on [PyPi Test](http://testpypi.python.org/pypi?%3Aaction=register_form). You must create an
account in order to be able to upload your code. I recommend using the same email/password for
both accounts, just to make your life easier when it comes time to push.

### Create a `.pypirc` configuration file

This config file holds your information for authenticating with PyPi.

		[distutils] # this tells distutils what package indexes you can push to
		index-servers =
			pypi # the live PyPi
			pypi-test # test PyPi
		
		[pypi] # authentication details for live PyPi
		repository: https://pypi.python.org/pypi
		username: {{your_username}}
		password: {{your_password}}
	
		[pypi-test] # authentication details for test PyPi
		repository: https://testpypi.python.org/pypi
		username: {{your_username}}

this is just to make your life easier, so that when it comes time to
upload you don't have to type/remember your username and password

### Prepare your package

Every package on PyPi needs to have a file called `setup.py` at
the root of the directory. If your'e using a markdown-formatted read me file
you'll also need a `setup.cfg` file. Also, you'll want a `LICENSE.txt` file
describing what can be done with your code. So if I've been working on a
library called `my-lib`,  my directory structure would look like this:

		locu-python/ 	# arbitrary working directory name
			setup.py
			setup.cfg
			LICENSE.txt
			README.md
			locu-python/ 		# this is your module_name: see below
				__init__.py
				foo.py
				bar.py
				baz.py

Here's a breakdown of what goes in which file:  

* **setup.py** This is metadata about your library. Here's an example for a logging library I wrote:
	
			from distutils.core import setup
			setup(
				name = 'lggr',
				packages = ['lggr'], # this must be the same as your module_name from above
				version = '0.1',
				description = 'Python Logging For Humans',
				author = 'Peter Downs',
				author_email = 'peterldowns@gmail.com',
				url = 'https://github.com/peterldowns/lggr',	# use the URL to the github repo
				download_url = 'https://github.com/peterldowns/lggr/tarball/0.1', # I'll explain this in a second
				keywords = ['logging', 'log', 'coroutine'], # arbitrary keywords
				classifiers = [],  
			)
	The `download_url` is a link to a hosted file where people actually get the
  code from your library. Github will host this for you, but only if you
  create a "tag" in git. In your git repo, type: `git tag 0.1 -m "Adds a
  tag so that we can put this on pypi"`. Then, type `git tag` to show a
  list of tags -- you should see `0.1` in the list. Then, type `git push --tags origin master`.
  Github sees your tag and automatically packages your code, available for download at
  `https://github.com/{username}/{module_name}/tarball/{tag}`.

* **setup.cfg** tells PyPi where your README file is.
		
		[metadata]
		description-file = README.md
	
* **LICENSE.txt** whatever license you want your code to have. It doesn't really matter, anything can be in here. I use the MIT license myself.
	
### Register your package

in your directory, run the command `python setup.py register -r pypi-test`

### Upload your package

##### Test that it will work
in your directory, run the command `python setup.py sdist upload -r pypi-test`

##### Do it for real

repeat steps 4 and 5, using `pypi` instead of `pypi-test`.
	
	
			

				
				
				
				
				
				



