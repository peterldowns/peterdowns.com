Title: iTerm2 Finder Tools
Author: Peter Downs
Date: Sunday, August 14, 2016

# iTerm2 Finder Tools

My [post on opening iTerm2 from the Finder](/posts/open-iterm-finder-service.html) is now four and a half (!) years old. It's one of the two posts that drive traffic to this blog (the other is [this pypi tutorial](/posts/first-time-with-pypi.html)), which is pretty cool – I never expected it to get so much exposure. To everyone who's written to me, thank you! It's really cool to hear from other people who are using my code. And thank you especially to those who sent me improvements and bugfixes.

Recently (ok, not that recently, I'm playing catchup here) iTerm2 changed their Applescript API and my old scripts stopped working. I immediately started receiving mail telling me so; many of these emails even included code changes to fix it! But when I thought about updating that same blog post yet again, I decided that it was time to finally get around to making this code properly open source. It's what I do [for my other projects](https://github.com/peterldowns), so why not this one?

I'm happy to announce the first release (1.0.0) of [iTerm2 Finder Tools](https://github.com/peterldowns/iterm2-finder-tools).

There are three main improvements compared to the old system:

* A new build script so you don't ever have to open Automator.
* The build script checks which version of iTerm2 you have installed and builds the service and application with the appropriate Applescript code.
* The code is now on Github, so I can accept changes and contributions much more easily.

So go check it out, and if you find it useful, give it a star and/or send me an email! I'm also starting to use Twitter again, you can [follow me as @peterldowns](https://twitter.com/peterldowns).
