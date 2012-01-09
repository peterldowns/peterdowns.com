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
			<div id="sidebar-left" class="threecol">
			</div>

			<div id="content" class="sixcol">
			
			%if view == "archive":
				<div class="archives" style="text-align: center;">
				<h1> All Posts </h1>
				%for post in posts:
					<a href="{{post['url']}}"> {{post['title']}} </a>
				%end
		
			%elif view == "post":
				<div class="post">
					<div class="info">
					%if post['timestamp']:
						<p style="font-weight: 1000000; text-decoration: underline;">{{post['timestamp']}}</p>
					%end
					</div>
					{{!post['html']}}
				</div>
				<div class="divider"></div>
			%end
			</div>
			<div id="sidebar-right" class="threecol last">
			</div>
		</div>
	</div>
</body>
</doctype>
