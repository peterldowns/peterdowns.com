<doctype HTML>
<head>
	<!-- Mou Stylesheet -->
	<link rel="stylesheet" type="text/css" href="/static/md.css" />
	<!-- My stylesheets -->
	<link rel="stylesheet" type="text/css" href="/static/blog.css" />
	<! -- 1140px Grid -->
	<link rel="stylesheet" type="text/css" href="/static/1140.css" media="screen" />
	<!--[if lte IE 9]><link rel="stylesheet" href="/static/ie.css" type="text/css" media="screen" /><![endif]-->

<body>
	<div class="container">
		<div class="row">
			<div class="onecol">
			</div>
			<div id="header" class="tencol">
				<a href="/"><h1> Peter Downs </h1></a>
				<p> Student / Hacker / Human </p>
			</div>
			<div class="onecol last">
			</div>
		</div>
		<div class="row">
			<div class="onecol">
			</div>
			<div class="threecol">
				<div id="sidebar-left" class="shadow">
					<h3 style="text-align: center; text-decoration: underline;"> About </h3>
					<p> I'm <b>Peter Downs</b>. I'm a highschool (going on university) student in the US.
					I like to read, run, and program. This blog is my experiment with writing. </p>
				
					<h3 style="text-align: center; text-decoration: underline;"> Contact </h3>
					<p>&mdash; peter.l.downs@gmail.com</p>
					<p>&mdash; <a href="https://twitter.com/peterldowns">@peterldowns</a></p>
					<p>&mdash; <a href="https://github.com/peterldowns">@ Github</a></p>
					<p>&mdash; <a href="http://stackoverflow.com/users/829926/peter-downs">@ Stack Overflow</a></p>
					<p>&mdash; <a href="https://facebook.com/peter.downs">@ Facebook</a></p>
				</div>
			</div>

			<div id="content" class="sevencol">
			%if view == "archive":
				<div class="archives" style="text-align: center;">
				<h1> All Posts </h1>
				%for post in posts:
					<a href="{{post['url']}}"> {{post['title']}} </a>
				%end
				</div>
		
			%elif view == "post":
				<div class="post">
					<div class="info">
					%if post['timestamp']:
						<p style="font-weight: 1000000; text-decoration: underline; text-align: center;">{{post['timestamp']}}</p>
					%end
					</div>
					{{!post['html']}}
				</div>
				
				<div class="divider">
				</div>
			%end
			</div>
			
			<div class="onecol last">
			</div>
		</div>
	</div>
</body>
</doctype>
