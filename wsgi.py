from bottle import route, request, view, static_file, default_app, debug, run, redirect
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
	@view('index')
	def allPosts():
		allposts = allPosts()
		return {
			"posts" : [allposts[p] for p in allposts],
			"view" : "archive",
		}

	@route('/posts/:title#.+#')
	@view('index')
	def viewPost(title):
		try:
			post = getPost(title)
			return {
				"posts" : [post],
				"view" : "post"
			}
		except Exception as e:
			print e
			redirect("/")

if __name__ == "__main__":
	run(host='localhost', port=8080)
else:
	application = default_app()
