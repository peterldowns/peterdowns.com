from bottle import route, request, view, static_file, default_app, debug, run
debug(True)
import json

class static_files():
	@route('/static/:path#.+#')
	def serve(path):
		return static_file(path, root='./static')

class website():
	@route('/')
	@view('blog')
	def blog():
		return {"posts" : [] }
	
	@route('/recent', 'GET')
	# AJAX endpoint for recent post titles
	def recentPosts():
		return {"recent_posts" : []}

	@route('/:title#.+#')
	@view('blog')
	def viewPost(title):
		posts = None
		with open("posts.json") as fin:
			posts = json.loads(fin.read())
			""" Posts should be a dict: title : path """
		try:
			with open(posts[title]) as article:
				post_html = article.read()
				return {"posts" : [post_html]}
		except Exception as e:
			print e
			return {"posts" : []}

	@route('/projects')
	@view('projects')
	def projects():
		return {}
	
if __name__ == "__main__":
	run(host='localhost', port=8080)
else:
	application = default_app()
