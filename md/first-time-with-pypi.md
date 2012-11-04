Title: How to submit to PyPI
Author: Peter Downs
Date: Saturday, November 3, 2012

The other month a coworker of mine wanted to distribute
[a small wrapper](http://pypi.python.org/pypi/locu/0.1)
he'd written for the [Locu API](http://dev.locu.com/).
Instead of forcing developers to clone his repository, he
wanted them to be able install with a single command:
`pip install locu`. He wasn't sure how to go about this so
I wrote up a quick guide, which I'm publishing below
because I haven't found any other guides for this particular
use case (python library hosted on github).





# What is PyPi?

> **PyPI** -- the Python Package Index
> The Python Package Index is a repository of software for the
> Python programming language.




It was a pain in the ass and didn't work for whatever reason.

0. Figuring out .tar.gz link on github (solution: use tags)
1. ~/.pypirc
2. python setup.py register -r pypi
3. python setup.py sidst upload -r pypi
