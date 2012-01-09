""" Given a list of .md files, creates html output
	in ./posts with the same titles and a 'posts.json'
	information file """
import os
import sys
import json
import markdown
from bottle import template, view

POSTS_FOLDER = 'posts'

# Build the JSON dict of posts and HTML
posts = {}
num_posts = len(sys.argv)-1
print "Building {} posts:".format(num_posts)
for num, filepath in enumerate(sys.argv[1:]):
	filename = filepath.split(os.sep)[-1]
	title = filename.split('.md')[0]
	print "\t[{} / {}] {} -> {}".format(num+1, num_posts, filepath, title)
	try:
		with open(filepath) as fin:
			md_content = fin.read()
	except Exception as e:
		print e
		md_content = ""
	timestamp, md_content = md_content.split('\n', 1)
	post = {
		"url" : "{}/{}.html".format(POSTS_FOLDER, title),
		"path" : filename,
		"html" : markdown.markdown(md_content),
		"title" : " ".join(map(str.capitalize, title.split('-'))),
		"timestamp" : timestamp
	}
	posts[title] = post

# Write it to file
with open('posts.json', 'w') as fout:
	fout.write(json.dumps(posts, sort_keys=True, indent=4))

from operator import itemgetter

# sort posts
posts = posts.values(); posts.sort(key=itemgetter('timestamp'), reverse=True)


# render archive page
print "Writing homepage -> index.html"
with open('index.html', 'w') as fout:
	@view('index.tpl')
	def renderArchive():
		return {
			"posts" : posts,
			"view" : "archive"
		}
	t = renderArchive()
	fout.write(t)

# make posts folder
try:
	os.mkdir(POSTS_FOLDER)
except OSError:
	pass

print "Writing {} posts:".format(num_posts)
# render each post
for post in posts:
	print "\t[{} / {}] {} -> {}".format(num+1, num_posts, title, post['url'])
	with open(post['url'], 'w') as fout: # url as path. IKR!?!?
		@view('index.tpl')
		def renderPost():
			return {
				"post" : post,
				"view" : "post"
			}
		t = renderPost()
		fout.write(t)

