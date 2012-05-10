#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import markdown
from operator import itemgetter
from bottle import template, view
from time import mktime, strptime

_MDFolder = "./md"
_HTMLFolder = "./posts"
_Parser = markdown.Markdown(extensions=['meta'])

@view('index.tpl')
def renderHomepage(posts):
	templateData = {
		"posts" : posts,
		"view" : "archive",
	}
	return templateData

@view('index.tpl')
def renderPost(post):
	templateData = {
		"post" : post,
		"view" : "post"
	}
	return templateData

def readMD(fpath):
	poststr = ""
	with open(fpath, 'r') as post:
		poststr = post.read()
	return poststr

def parseMD(fstr):
	""" Parse a raw markdown string with optional metadata
		included. """
	html = _Parser.convert(fstr)
	meta = _Parser.Meta
	meta['html'] = html
	
	meta['date'] = meta['date'][0]
	meta['title'] = meta['title'][0]
	meta['author'] = meta['author'][0]

	return meta

def makePost(path):
	""" Given a path, return a post dictionary. """
	path = os.path.abspath(path)
	raw_md = readMD(path)
	post = parseMD(raw_md)
	
	post['MDpath'] = path
	post['MDfile'] = filename = path.rsplit(os.sep, 1)[1]
	post['MDtitle'] = filename.rsplit('.', 1)[0]

	time_format = "%A, %B %d, %Y"
	timestamp = mktime(strptime(post['date'], time_format))
	post.update({
		"HTMLpath" : "{}/{}.html".format(_HTMLFolder, post['MDtitle']),
		"timestamp" : timestamp,
	})
	return post

def buildPosts(in_folder):
	in_folder = os.path.abspath(in_folder)
	filepaths = map(lambda f: os.sep.join((in_folder, f)), os.listdir(in_folder))

	posts_out = []
	for post_path in filepaths:
		post = makePost(post_path)
		posts_out.append(post)
	return posts_out

if __name__=="__main__":
	posts = buildPosts(_MDFolder)
	posts.sort(key=itemgetter('timestamp'), reverse=True)
	
	try: os.mkdir(_HTMLFolder) # make HTML folder
	except OSError: pass #already existed

	print "Writing homepage -> ./index.html"
	with open('./index.html', 'w') as fout:
		homepageHTML = renderHomepage(posts)
		fout.write(homepageHTML)
	
	cur_ind = 0
	num_posts = len(posts)
	print "Writing {} posts:".format(num_posts)
	for post in posts:
		print "\t[{} / {}] {} -> {}".format(cur_ind+1, num_posts, post['MDpath'], post['HTMLpath'])
		cur_ind += 1
		with open(post['HTMLpath'], 'w') as fout:
			postHTML = renderPost(post)
			fout.write(postHTML)
	
	print "Done."
