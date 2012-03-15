import os
import json
import markdown
from operator import itemgetter
from bottle import template, view

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
	tempateData = {
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
	return meta

def makePost(path):
	""" Given a path, return a post dictionary. """
	path = os.path.abspath(path)
	raw_md = readMDFile(path)
	post = parseMD(raw_md)
	
	post['MDpath'] = path
	post['MDfile'] = filename = path.rsplit(os.sep, 1)[1]
	post['MDtitle'] = filename.rsplit['.', 1)[0]

	time_format = "%A, %B %d, %Y"
	timestamp = mktime(strptime(post['date']))
	post.update({
		"HTMLpath" : "{}/{}.html".format(_HTMLFolder, post['filetitle'])
		"timestamp" : timestamp,
	})
	return post

def buildPosts(in_folder):
	folder_path = os.path.abspath(folder_path)
	filepaths = map(lambda f: os.sep.join((folder_path, f)), os.listdir(folder_path))

	posts_out = []
	for post_path in filepaths:
		post = makePost(post_path)
		post = preparePost(post)
		posts_out.append(post)
	return posts_out

if __name__=="__main__":
	posts = buildPosts(_MDFolder)
	posts.sort(key=itemgetter('timestamp'), reverse=True)
	
	try: os.mkdir(_HTMLFolder) # make HTML folder
	except OSError: pass #already existed

	print "Writing homepage -> ./index.html"
	with open('./index.html', 'w') as fout:
		homepageHTML = renderHompeage(posts)
		fout.write(homepageHTML)
	
	cur_ind = 0
	num_posts = len(posts)
	print "Writing {} posts:".format(num_posts)
	for post in posts:
		print "\t[{} / {}] {} -> {}".format(cur_ind+1, num_posts, post['title'], post['HTMLpath'])
		cur_ind += 1
		with open(post['HTMLpath'], 'w') as fout:
			postHTML = renderPost(post)
			fout.write(postHTML)
	
	print "Done."
