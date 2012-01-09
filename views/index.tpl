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
			<div id="header" class="twelvecol last">
				<a href="/"><h1> Peter Downs </h1></a>
				<p> Student, Hacker, Human </p>
				<!--
				<div id="nav">
					<li><a href="/"> Blog </a></li>
				</ul>
				</div>
				-->
			</div>
		</div>
		<div class="row">
			<div class="threecol">
			<div id="sidebar-left">
				<h3>About</h3>
				<p>Hi. I'm Peter Downs. I'm a highschool student in the US, but I'll soon
				be heading off to university. I like reading, running, and programming; this
				blog is my experiment with writing.</p>
				<br />
				<h3>Things I like:</h3>
				<ul>
					<li>Python</li>
					<li>Winning 5k races</li>
					<li>"The Laughing Sutra"</li>
					<li>Intelligent discussion</li>
					<li>Fine suits</li>
					<li>Markdown</li>
					<li>Learning new things</li>
				</ul>
			</div>
			</div>

			<div id="content" class="sixcol">
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
			
			<div class="threecol last">
			<div id="sidebar-right">
				<h3> Contact </h3>
				<ul>
					<li> peter.l.downs@gmail.com </li>
					<li> <a href="https://twitter.com/peterldowns">@peterldowns</a> </li>
				</ul>
				<br />
				<h3> Profiles </h3>
				<ul>
					<li> <a href="https://github.com/peterldowns">github</a> </li>
					<li> <a href="http://stackoverflow.com/users/829926/peter-downs">stack overflow</a> </li>
					<li> <a href="https://facebook.com/peter.downs">facebook</a> </li>
				</ul>
			</div>
			</div>
		</div>
	</div>
</body>
</doctype>
