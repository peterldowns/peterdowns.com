#!/usr/bin/env python
# coding: utf-8
from mustache import template
_enc_errors = 'xmlcharrefreplace' # How to treat unicode characters when writing
                                  # HTML content.
_index = './index.html'   # file at which to store the homepage / archive


@template('templates/index.html')
def render_index():
  return {'index': True}, {}


def _write(f, html):
    f.write(unicode(html).encode(errors=_enc_errors))


def main():
  print 'Writing homepage -> {}'.format(_index)
  with open(_index, 'w') as fout:
    _write(fout, render_index())


if __name__=='__main__':
  main()
