""" Given a list of .md files, creates html output
	in ./posts with the same titles and a 'posts.json'
	information file """
import os
import sys
import json
import markdown

# Build the JSON dict of posts and HTML
posts = {}
for filepath in sys.argv[1:]:
	print filepath
	filename = filepath.split(os.sep)[-1]
	print filename
	title = filename.split('.md')[0]
	print title
	print ""
	try:
		with open(filepath) as fin:
			md_content = fin.read()
	except Exception as e:
		print e
		md_content = ""
	post = {
		"path" : filename,
		"html" : markdown.markdown(md_content)
	}
	posts[title] = post

# Write it to file
with open('posts.json', 'w') as fout:
	fout.write(json.dumps(posts, sort_keys=True, indent=4))

