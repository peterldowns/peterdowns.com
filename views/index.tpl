<doctype HTML>
<head>
	<!-- Fonts -->
	<link href='http://fonts.googleapis.com/css?family=Lato:700italic,400,400italic,700' rel='stylesheet' type='text/css'>
	<! -- 1140px Grid -->
	<link rel="stylesheet" type="text/css" href="/static/css/1140/1140.css" media="screen" />
	<!--[if lte IE 9]><link rel="stylesheet" href="/static/css/1140/ie.css" type="text/css" media="screen" /><![endif]-->
	<!--<link rel="stylesheet" type="text/css" href="/static/css/mou/clearness_dark.css" />
	<link rel="stylesheet" type="text/css" href="/static/css/mou/github.css" />-->
	<link rel="stylesheet" type="text/css" href="/static/css/mou/clearness.css" />
	<!-- My stylesheets -->
	<link rel="stylesheet" type="text/css" href="/static/css/index.css" />
	<title> Peter Downs - Student / Hacker / Human </title>
</head>

<body>
	<div id="sidebar" class="sidebar">
		<div id="header">
			<a href="/"><h1> Peter Downs </h1></a>
			<p> Student / Hacker / Human </p>
		</div>
		<div id="sidebar-inner" class="shadow">
			<h3> About </h3>
			<p> I'm <b>Peter Downs</b>. I'm a highschool (going on university) student in the US.  I like to read, run, and program. This blog is my experiment with writing. </p>
			<h3> Contact </h3>
			<p>&mdash; peter.l.downs@gmail.com</p>
			<p>&mdash; <a href="https://twitter.com/peterldowns">@peterldowns </a></p>
			<p>&mdash; <a href="https://github.com/peterldowns"> Github </a></p>
			<p>&mdash; <a href="http://stackoverflow.com/users/829926/peter-downs"> Stack Overflow </a></p>
			<p>&mdash; <a href="https://facebook.com/peter.downs"> Facebook </a></p>
		</div>
	</div>
	<div id="content" class="content">
		<div id="content-inner" class="shadow">
		%if view == "archive":
			<div class="archives" style="text-align: center;">
				<h1> All Posts </h1>
			%for post in posts:
				<h4><a href="{{post['HTMLpath']}}">{{post['title']}}</a></h4>
				<br />
			%end
			</div>
		</div>

		%elif view == "post":
			<div class="post">
				<div class="info">
				%if post['date']:
					<p style="font-weight: 1000000; text-decoration: underline; text-align: center;">{{post['date']}}</p>
				%end
				</div>
				{{!post['html']}}
			</div>
		%end
		</div>
	</div>
</body>
</doctype>
