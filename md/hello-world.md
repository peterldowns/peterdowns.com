# Hi
Hello. As you can see in the side bar, my name is Peter. I like to read, run, and program, but now I'm starting to write, too. This is my blog. I'm going to try to update it pretty often; for the past year I've been keeping a list of ideas about which I'd like to write.

### Why?
I've been meaning to start a blog for a while. I haven't gone through with it -- I never really liked tumblr, or blogger, or any other blogging system. I think that writing is important, and that I should start contributing something online instead of just reading posts on [hacker news](http://news.ycombinator.com) and [boingboing](http://boingboing.net). Plus, writing is fun, and I want to become better at it.

So, here's the blog.

### How?

I'm using [bottle.py](http://bottlepy.org) to deal with `HTTP` requests. CSS3 and the [1140px grid](cssgrid.net) make the layout pretty simple. 

The posts are all written in Markdown and converted using the python [markdown module](http://www.freewisdom.org/projects/python-markdown/) on pypi. The HTML for each post is stored in one large JSON dictionary which is queried when you come to the site. I thought about using a database but really there's no reason to do so.

If you'd like to look at it (or even contribute a post!), [all of the code is available on my github](https://github.com/peterldowns/website).

