from bottle import route, request, view, static_file, default_app, debug, run
debug(True)
import json

class static_files():
	@route('/static/:path#.+#')
	def serve(path):
		return static_file(path, root='./static')

def allPosts(postsf="posts.json"):
	try:
		with open(postsf) as fin:
			posts = json.loads(fin.read())
			return posts
	except Exception as e:
		print e
		return []
def getPost(title, postsf="posts.json"):
	posts = allPosts(postsf)
	try:
		return posts[title]
	except:
		return None

class website():
	@route('/', 'GET')
	@view('blog')
	def recentPosts():
		allposts = allPosts()
		postns = allposts.keys()[0:5]
		posts = filter(lambda x: x, [getPost(p) for p in postns]) # only valid posts
		return {"posts" : posts}

	@route('/posts/:title#.+#')
	@view('blog')
	def viewPost(title):
		try:
			post = getPost(title)
			return {"posts" : [post] }
		except Exception as e:
			print e
			return {"posts" : []}

	@route('/projects')
	@view('projects')
	def projects():
		return {}

	@route('contact')
	@view('contact')
	def contact():
		return {}
	
if __name__ == "__main__":
	run(host='localhost', port=8080)
else:
	application = default_app()
