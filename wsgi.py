import json
from bottle import route, request, view, static_file, default_app, debug, run
debug(True)

class static_files():
	@route('/static/:path#.+#')
	def serve(path):
		return static_file(path, root='./static')

class website():
	@route('/')
	@view('home')
	def homepage():
		return {}
	
	@route('/blog')
	@view('blog')
	def blog():
		return {"posts" : None }
	
	@route('/blog/recent', 'GET')
	# AJAX endpoint for recent post titles
	def recentPosts():
		return {"recent_posts" : None}

	@route('/blog/:id#.+#')
	@view('blog')
	def viewPost(id):
		try:
			article = db.get(id)
			return {"posts" : article}
		except:
			return {"posts" : None}

	@route('/projects')
	@view('projects')
	def projects():
		return {}
	
	@route('/resume')
	@view('resume')
	def resume():
		return {}

if __name__ == "__main__":
	run(host='localhost', port=8080)
else:
	application = default_app()
