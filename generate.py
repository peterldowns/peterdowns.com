""" Given a list of .md files, creates html output
	in ./posts with the same titles and a 'posts.json'
	information file """
import os
import sys
import json
import markdown

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
		"url" : "/posts/{}".format(title),
		"path" : filename,
		"html" : markdown.markdown(md_content),
		"title" : " ".join(map(str.capitalize, title.split('-'))),
		"timestamp" : timestamp
	}
	posts[title] = post

# Write it to file
with open('posts.json', 'w') as fout:
	fout.write(json.dumps(posts, sort_keys=True, indent=4))

print "Done."
