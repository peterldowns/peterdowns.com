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
service that you can access by right-clicking on a folder.  Here's the script:

```applescript
on run {input, parameters}
  tell application "Finder"
    set dir_path to quoted form of (POSIX path of (input as alias))
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
        write text "cd " & theDir & ";clear;"
      end tell
    end tell
  end tell
end CD_to
```

Using Automator, create a new "Service" that accepts folders in Finder.

![setting up the service][9]

Add a "Run Applescript" action and paste in the above code.  Save it as
whatever you'd like - I saved mine as `open_iterm`. Now, you can just
right-click any folder from within Finder to open an iTerm tab there. Cool.

![the service in action][10]

### Update – June 24, 2013

I just got a great email from [Eric Hu][11] describing
a modified version of this script that can be run on files, not just folders.
[Check it out here](https://gist.github.com/eric-hu/5846890) &mdash; thanks,
Eric!

### Update – May 15, 2014

[John Kokkinidis](http://sudoplz.eu/) was kind enough to write in with a
solution I like even more than the Finder service presented above. His version
is designed to be run with a single click from the Finder, once you've
navigated to the folder that you'd like to open. If you take his script:

```applescript
on run {input, parameters}
  tell application "Finder"
    set dir_path to quoted form of (POSIX path of (folder of the front window as alias))
  end tell
  CD_to(dir_path)
end run

on CD_to(theDir)
  tell application "iTerm"
    activate

    try
      set sesh to current session of current terminal
    on error
      set term to (make new terminal)
      tell term
        launch session "Default"
        set sesh to current session
      end tell
    end try

    tell sesh
      write text "cd " & theDir & ";clear;"
    end tell
  end tell
end CD_to
```

create an "Application" in Automator:

![setting up the application][12]

and drag it onto the Finder window while holding the command key (in Yosemite,
the command and option keys. Thanks [Peter](https://github.com/pjvandehaar)!)

![installing the application][13]

You can then click that icon any time you're in the Finder to get a new iTerm
shell at that location. Thanks, John! Also, thanks to [Eryan
Cobham](http://eryancobham.com/) and [Adam
Mclain](https://twitter.com/adammclain) for both writing in with the same
suggestion: to use `quoted form of (POSIX path of ...)` instead of `POSIX path
of ...`, allowing the script to work with directories including spaces. And a
big thanks to Peter Scott for writing in to suggest a fix for a problem where
two windows were being created. He points to [CtWise's efforts
here](http://www.alfredforum.com/topic/721-executing-iterm2-terminal-commands-in-current-shell/?hl=iterm)
as his inspiration.

[1]: http://www.iterm2.com/#/section/home
[2]: http://ethanschoonover.com/solarized
[3]: http://snippets.dzone.com/user/SimonDorfman
[4]: http://snippets.dzone.com/posts/show/961
[5]: http://benalman.com/
[6]: https://gist.github.com/905546
[7]: https://github.com/lsloan
[8]: https://gist.github.com/1265327
[9]: /static/img/applescript_service.jpg "Setting up the service"
[10]: /static/img/applescript_service_in_action.jpg "Using the new service"
[11]: https://github.com/eric-hu
[12]: /static/img/applescript_kokkinidis_application.jpg "Setting up the application"
[13]: /static/img/applescript_kokkinidis_install.gif "Installing the application"
