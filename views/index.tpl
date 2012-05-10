<doctype HTML>
<head>
	<link href='http://fonts.googleapis.com/css?family=Lato:700italic,400,400italic,700' rel='stylesheet' type='text/css'>

	<!--
	<link rel="stylesheet" type="text/css" href="/static/css/mou/clearness_dark.css" />
	<link rel="stylesheet" type="text/css" href="/static/css/mou/github.css" />
	<link rel="stylesheet" type="text/css" href="/static/css/mou/solarized_dark.css" />
	<link rel="stylesheet" type="text/css" href="/static/css/mou/solarized_light.css" />
	-->
	<link rel="stylesheet" type="text/css" href="/static/css/mou/clearness.css" />
	<link rel="stylesheet" type="text/css" href="/static/css/index.css" />
	%if view == "archive":
	<title> Peter Downs - Student / Hacker / Human </title>
  %elif view == "post":
	<title> Peter Downs - Student / Hacker / Human - {{post['title']}}</title>
  %end
	<meta name="viewport" content="width=device-width">
</head>

<body>
	<div id="sidebar">
		<div id="header">
			<a href="/"><h1> Peter Downs </h1></a>
			<p> Student / Hacker / Human </p>
		</div>
		<div id="sidebar-inner">
			<h3> About </h3>
			<p> I'm <b>Peter Downs</b>. I'm a highschool (going on university) student in the US.  I like to read, run, and program. This blog is my experiment with writing. </p>
			<h3> Contact </h3>
			<p>&mdash; peterldowns@gmail.com</p>
			<p>&mdash; <a href="https://twitter.com/peterldowns">@peterldowns </a></p>
			<p>&mdash; <a href="https://github.com/peterldowns"> Github </a></p>
			<p>&mdash; <a href="http://stackoverflow.com/users/829926/peter-downs"> Stack Overflow </a></p>
			<p>&mdash; <a href="https://facebook.com/peter.downs"> Facebook </a></p>
		</div>
	</div>
	<div id="content">
		<div id="content-inner">
		%if view == "archive":
			<div class="archives">
				<h1> All Posts </h1>
			%for post in posts:
				<h4><a href="{{post['HTMLpath']}}">{{post['title']}}</a></h4>
				<br />
			%end
			</div>
		</div>

		%elif view == "post":
			<div class="post">
				%if post['date']:
					<p style="font-weight: 1000000; text-decoration: underline;">{{post['date']}}</p>
				%end
				{{!post['html']}}
			</div>
		%end
		</div>
	</div>
</body>
</doctype>
