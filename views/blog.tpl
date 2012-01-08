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
				<h1> Peter Downs </h1>
				<p> Student, Hacker, Human </p>
				<div id="nav">
				<ul>
					<li><a href="#"> Projects </a></li>
					<li><a href="#"> Blog </a></li>
					<li><a href="#"> Contact </a></li>
				</ul>
				</div>
			</div>
		</div>
		<div class="row">
			<div id="sidebar-left" class="threecol">
				<h1> This is my website </h1>
				<p> It's not really for anyone but me, but you're welcome to enjoy it, too. </p>
			</div>
			<div id="content" class="sixcol last">
			%for post in posts:
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
		</div>
	</div>
</body>
</doctype>
