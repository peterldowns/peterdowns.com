#!/usr/bin/env python
# coding: utf-8
import codecs
import json
import markdown
import os
import yaml

from mustache import template
from operator import itemgetter
from time import mktime, strptime

_parser = markdown.Markdown(extensions=['meta'])

_ext = '.md' # The extension of posts to be treated as markdown content.
_md_in = './md' # The source directory for markdown posts (*.md).
_md_out = './posts' # The output directory for HTML posts.
_time_fmt = '%A, %B %d, %Y' # The format string for parsing time metadata.
_enc_errors = 'xmlcharrefreplace' # How to treat unicode characters when writing
                                  # HTML content.

_index = './index.html'   # file at which to store the homepage / archive
_about = './about.html'

@template('templates/index.html')
def render_homepage(posts):
  return {'posts' : posts}, {}

@template('templates/about.html')
def render_about():
  return {}, {}

@template('templates/post.html')
def render_post(post):
  return {'post' : post}, {}

def load_post(path):
  """ Given a path to a Markdown file, load its contents, parse them, add
  additional metadata, and then return a dict containing all of the necessary
  information.
  """
  # Read the Markdown file
  md = u''
  with codecs.open(path, 'rb', 'utf-8') as fin:
    md = unicode(fin.read())

  # Convert the Markdown to HTML
  html = _parser.convert(md)

  # Process metadata
  post = _parser.Meta # metadata from the last parse
  post['html'] = html
  post['date'] = post['date'][0]
  post['title'] = post['title'][0]
  post['md_path'] = path
  post['md_filename'] = filename = os.path.split(path)[1]
  post['slug'] = slug = os.path.splitext(filename)[0]
  post['timestamp'] = mktime(strptime(post['date'], _time_fmt))
  post['html_path'] = os.path.relpath(os.sep.join((_md_out, slug)) +
                                      os.path.extsep +
                                      'html')

  return post

def load_posts(folder):
  """ Given an input folder, load all of the Markdown posts within it and
  return them.
  """
  files = filter(lambda path: _ext in path, os.listdir(folder))
  rel_paths = map(lambda filename: os.path.join(folder, filename), files)

  for path in rel_paths:
    yield load_post(path)

if __name__=='__main__':
  all_posts = load_posts(_md_in)
  sorted_posts = sorted(all_posts, key=itemgetter('timestamp'), reverse=True)

  try: os.mkdir(_md_out) # make the output folder
  except OSError: pass # already exists

  print 'Writing homepage -> {}'.format(_index)
  with open(_index, 'w') as fout:
    html = render_homepage(sorted_posts)
    fout.write(unicode(html).encode(errors=_enc_errors))

  print 'Writing about -> {}'.format(_about)
  with open(_about, 'w') as fout:
    html = render_about()
    fout.write(unicode(html).encode(errors=_enc_errors))

  num_posts = len(sorted_posts)
  print 'Writing {} posts:'.format(num_posts)

  for i, post in enumerate(sorted_posts):
    md_path = post.get('md_path')
    html_path = post.get('html_path')

    print '\t[{} / {}] {} -> {}'.format(i+1, num_posts, md_path, html_path)

    with open(html_path, 'w') as fout:
      html = render_post(post)
      fout.write(unicode(html).encode(errors=_enc_errors))

  print 'Done.'
