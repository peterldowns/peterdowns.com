Title: Handy Git Aliases
Author: Peter Downs
Date: Sunday, April 13, 2014

# Handy Git Aliases

Git is an integral part of my daily workflow, for my dayjob and for my own
hacking. I've noticed that quite a few people have defined their own set of
custom aliases and I figured I'd share mine. The system is quite simple: except
for a few exceptions, my most common commands get shorted as much as possible
while still remaining unique. For instance,

    git show --color

becomes

    gsh

Building off of that, a command I use often to show just the message of a given
commit

    git show --color -s

becomes

    gshs


The thing I like about this system is that it's very intuitive, and more often
than not I'm able to guess at the shortcuts that I use less often and haven't
memorized. Before I got used to my aliases I felt like git "slowed me down"
when I just wanted to get my damn changes commited and pushed. Now, I feel a
thousand times faster.

Without further ado, here are the rest of the aliases from my `.profile`:

<script src="https://gist.github.com/peterldowns/10621099.js"></script>
