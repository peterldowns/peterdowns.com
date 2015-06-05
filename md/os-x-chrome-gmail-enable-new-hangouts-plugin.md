Title: How To Get The New Hangouts In Gmail On Chrome OS X
Author: Peter Downs
Date: Thursday, June 4, 2015

# How To Get The New Hangouts In Gmail On Chrome OS X

Recently, my friend Anvita tried sending me a chat message over Google's
Hangouts, using the chat box that shows up in Gmail. While I was able to
respond to her messages, she always appeared offline to me, and I to her. We
noticed that I was still on Google Talk, not Google Hangouts, which ended up
being the issue. Should be a simple fix: follow [the instructions in this
Google support note](https://support.google.com/hangouts/answer/3115176), click
on a "Try the new Hangouts" link, and be done.

!["Try the new Hangouts"](/static/img/try_hangouts_cnet.png)

### The problem

But that button didn't appear for me; googling (ha) turned up that a few other
people were having the same issue. After some debugging, here's the
explanation: the latest versions of chrome disable the [NPAPI
interface](https://www.chromium.org/developers/npapi-deprecation). This should
be fine, since the Hangout plugin shouldn't use that deprecated API, but
apparently it does. And even though I had the old Google Voice and Video plugin
installed, it wasn't being used, since NPAPI was deprecated. I'm pretty sure
this is the bug because when I tried Safari, I was prompted to allow the Google
Voice and Video plugin, and once I did the "Try the new Hangouts" link showed
up and everything worked perfectly.

### The solution

All hope is not lost: for now, the solution is to go to
[chrome://flags](chrome://flags/) and enable the "Enable NPAPI" option.

![Enable NPAPI](/static/img/enable_npapi.jpg)

I say for now, because this option will be removed with Chrome 45. Hopefully
this helps someone out in the meantime.
