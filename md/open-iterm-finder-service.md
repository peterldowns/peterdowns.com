Title: Opening iTerm From a Finder Directory
Author: Peter Downs
Date: Wednesday, March 14, 2012  

# Opening iTerm From a Finder Directory

If, like me, you work mostly from OS X, you've probably already discovered
[iTerm2][1]. If you haven't: it's an incredibly good replacement for the
default Terminal application. Combined with the [solarized][2] color scheme, it
does what all software should: it fades away and lets me get my work done
without an issue.

If you're like me in another way, you will occasionally use the Finder to
browse through your files. The problem is that it's difficult to open an iTerm
window set to the current Finder directory.

A couple of different people have come up with solutions. [Simon Dorfman][3]
came up with [an Applescript][4] to keep in the Finder sidebar or your dock; it
opens iTerm tabs in any directory dropped on it. [Ben Alman][5] wrote [a
similar script][6] that does the same thing. But both of these require you to
drag and drop an item onto a script that takes up space in your sidebar or
dock.

I didn't want to clutter up my dock or Finder sidebar with a droppable script,
so I adapted [Lance E Sloan][7]'s [script][8] and turned it into a Finder
service.  Here's the script:

	on run {input, parameters}
		tell application "Finder"
			set dir_path to "\"" & (POSIX path of (input as string)) & "\""
				-- display dialog dir_path
		end tell
		CD_to(dir_path)
	end run
	
	on CD_to(theDir)
		tell application "iTerm"
			activate
			try
				set t to the last terminal
			on error
				set t to (make new terminal)
			end try
			tell t
				launch session "Default Session"
				tell the last session
					write text "cd " & theDir & ";clear;ls"
				end tell
			end tell
		end tell
	end CD_to

Using Automator, create a new "Service" that accepts folders in Finder.

![setting up the service][9]

Add a "Run Applescript" action and paste in the above code.  Save it as
whatever you'd like - I saved mine as "open_iterm". Now, you can just
right-click any folder from within Finder to open an iTerm tab there. Cool.

![the service in action][10]

### Update &mdash; June 24, 2013

I just got a great email from [Eric Hu](https://github.com/eric-hu) describing
a modified version of this script that can be run on files, not just folders.
[Check it out here](https://gist.github.com/eric-hu/5846890) &mdash; thanks,
Eric!

[1]: http://www.iterm2.com/#/section/home
[2]: http://ethanschoonover.com/solarized
[3]: http://snippets.dzone.com/user/SimonDorfman
[4]: http://snippets.dzone.com/posts/show/961
[5]: http://benalman.com/
[6]: https://gist.github.com/905546
[7]: https://github.com/lsloan
[8]: https://gist.github.com/1265327
[9]: /static/img/applescript_service.jpeg "Setting up the service"
[10]: /static/img/applescript_service_in_action.jpeg "Using the new service"
