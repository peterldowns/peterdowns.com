<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Bootstrap, from Twitter</title>
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le styles -->
    <link href="static/bootstrap.min.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 60px;
      }
    </style>
  </head>

  <body style="background: url(static/project-paper.png) repeat">
    <div class="topbar">
      <div class="topbar-inner">
        <div class="container-fluid">
          <a class="brand" href="#">peterdowns.com</a>
          <ul class="nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="blog">Blog</a></li>
            <li><a href="projects">Projects</a></li>
			<li><a href="resume">Resume</a></li>
          </ul>
          <p class="pull-right">Search is forthcoming</p>
        </div>
      </div>
    </div>

	<div class="sidebar" style="position: absolute; left: 0; border: 2px solid #000; border-left: none; height: 300px; width: 250px; top: 25%; bottom: 25%">
	  <div class="sidebar-text" style="position: absolute; left: 0; top: 0; bottom: 0; right: 10px; padding: 10px;">
		<h5>About</5>
		<p> Welcome. My name is Peter Downs. This is my website. </p>
		<h5>Contact</h5>
		<p> You can email me at
		  <a href="mailto:peterldowns@gmail.com">peterldowns@gmail</a>.
		  <br>
		  I have a
		  <a href="http://twitter.com/#!/peterldowns">twitter</a>.
		  <br>
		  You may not phone me.
		  <br>
		  I also have profiles at 
	        <a href="http://github.com/peterldowns">github</a>,
			<a href="http://news.ycombinator.com/user?id=peter_l_downs">hacker news</a>, and
			<a href="http://stackoverflow.com/users/829926/peter-downs">stackoverflow</a>.
		</p>
      </div>
	  <div class="sidebar-hider" style="position: absolute; right: 0; top: 0; bottom: 0; background-color: #000; width: 10px;">
	  </div>
    </div>
	<div class="content" style="position: absolute; left: 200px; min-width: 400px; right: 0; margin: 80px; top:40px; bottom: 0">
      <div class="content">
        <!-- Main hero unit for a primary marketing message or call to action -->
        <div class="hero-unit" style="height: 80% auto">
          <h1>Hello, world!</h1>
		  <p>My name is Peter Downs. You're on my website.</p>
		  <br>
		  <p>Why are you here?</p>
          <p><a class="btn primary large">Tell me&raquo;</a></p>
        </div>
        <footer>
          <p>&copy; Peter Downs 2012</p>
        </footer>
      </div>
    </div>

  </body>
</html>
