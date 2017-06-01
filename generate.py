#!/usr/bin/env python
# coding: utf-8
import codecs
import json
import markdown
import os
import yaml
import pytz
from datetime import datetime
from lxml import html as lxhtml

from feedgen.feed import FeedGenerator
from mustache import template
from operator import itemgetter
from time import mktime, strptime

_parser = markdown.Markdown(extensions=[
  'meta',
  'markdown.extensions.fenced_code',
  'markdown.extensions.codehilite',
])

_ext = '.md' # The extension of posts to be treated as markdown content.
_md_in = './md' # The source directory for markdown posts (*.md).
_md_out = './posts' # The output directory for HTML posts.
_time_fmt = '%A, %B %d, %Y' # The format string for parsing time metadata.
_enc_errors = 'xmlcharrefreplace' # How to treat unicode characters when writing
                                  # HTML content.

_index = './index.html'   # file at which to store the homepage / archive
_posts_index = './posts/index.html'
_feeds_dir = './feeds'
_protocol = 'http://'
_domain = 'peterdowns.com'
_blog_root = '{}{}/posts'.format(_protocol, _domain)

@template('templates/posts.html')
def render_posts_index(posts):
  return {'posts': posts}, {}

@template('templates/index.html')
def render_index():
  return {'index': True}, {}

@template('templates/post.html')
def render_post(post):
  return {'post' : post}, {}

def _utcstrp(*args, **kwargs):
    dt = datetime.strptime(*args, **kwargs)
    return dt.replace(tzinfo=pytz.utc)

def write_feeds(posts):
    g = FeedGenerator()
    g.id('http://peterdowns.com/blog')
    g.link(href='http://peterdowns.com/blog')
    g.description('incredibly on-brand')
    g.title(u'Peter Downs — Posts')
    for post in posts:
        e = g.add_entry()
        post_url = os.path.join(_blog_root, post['html_path'])
        e.id(post_url)
        e.link(href=post_url, rel='alternate')
        e.title(post['title'])
        e.author(name=post['author'][0])
        e.published(_utcstrp(post['date'], _time_fmt))
        if post['updated'] is None:
            e.updated(e.published())
        else:
            e.updated(_utcstrp(post['updated'], _time_fmt))

    g.atom_file('{}/atom.xml'.format(_feeds_dir))
    g.rss_file('{}/rss.xml'.format(_feeds_dir))

def post_fixup(htmlstr):
  html = lxhtml.fromstring(htmlstr)
  p_tags = html.findall('p')
  for p_tag in p_tags:
    img = p_tag.findall('img')
    if img:
      class_str = p_tag.get('class')
      classes = class_str.split(' ') if class_str else []
      classes.append('wide-content')
      p_tag.set('class', ' '.join(classes))

  pre_tags = html.findall('pre')
  for pre_tag in pre_tags:
    class_str = pre_tag.get('class')
    classes = pre_tag.split(' ') if class_str else []
    classes.append('wide-content')
    pre_tag.set('class', ' '.join(classes))

  outer_div = html
  outer_div.set('class', 'post')
  return lxhtml.tostring(outer_div)

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
  html = post_fixup(_parser.convert(md))

  # Process metadata
  post = _parser.Meta # metadata from the last parse
  post['html'] = html
  post['date'] = post['date'][0]
  post['title'] = post['title'][0]
  post['updated'] = post.get('updated', [None])[0]
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

def main():
  """ Generate the website. """
  all_posts = load_posts(_md_in)
  sorted_posts = sorted(all_posts, key=itemgetter('timestamp'), reverse=True)
  sorted_posts = list(sorted_posts)

  try: os.mkdir(_md_out) # make the output folder
  except OSError: pass # already exists

  print 'Writing homepage -> {}'.format(_index)
  with open(_index, 'w') as fout:
    html = render_index()
    fout.write(unicode(html).encode(errors=_enc_errors))

  print 'Writing posts index -> {}'.format(_posts_index)
  with open(_posts_index, 'w') as fout:
    html = render_posts_index(sorted_posts)
    fout.write(unicode(html).encode(errors=_enc_errors))

  print 'Writing feeds => {}'.format(_feeds_dir)
  write_feeds(sorted_posts)

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

if __name__=='__main__':
  main()
