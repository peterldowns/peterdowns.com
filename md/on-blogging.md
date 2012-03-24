Title: On Blogging
Author: Peter Downs
Date: Friday, March 23, 2012

# On Blogging


In the past few days, there's been a lot of discussion on [HN](http://news.ycombinator.com) about different methods of blogging. It all started when [Dustin Curtis](http://dcurt.is/) [wrote about](http://dcurt.is/codename-svbtle) his blogging framework, which he calls "Svbtle".

If you didn't click over to his website, you should, because it's absolutely beautiful. It has some subtle animations and a clean color scheme, but the most important thing is that it presents his ideas with very little cruft. His blog does what every blog should aspire to do: let readers read what he writes, painlessly.

#### More than the readers

From his post about Svbtle:

> When I'm writing, I want to have no distractions, so I removed all of them.
> When I have control over the visual style of my posts, I tend to take it a bit too far, which hinders the quality of my actual writing and prevents me from publishing.
> So I removed all styling options; Markdown and some restricted HTML are the only tools for styling posts.
> One of my main goals for this new writing interface was to encourage myself to spend more time writing and less time presenting.

Svbtle is designed to let people write as naturally as possible, too. Why bother blogging if it's a pain in the ass? It's clean, it's sexy, and a lot of people would use it if they could. The reason this is such big news is that they can't: the [Svbtle Network](http://svbtle.com/) is invitation only.

This being the hacker community, it took under 24 hours for someone to come up with an open source alternative. You can read all about [Nate Wienert](http://natewienert.com)'s [Obtvse](http://natewienert.com/codename-obtvse) project over at his blog. And shortly after that, [Adrian Unger](http://staydecent.ca/) released his [_own_ take](http://staydecent.ca/bits/essence-of-blogging/) on minimal, efficient blogging software.

#### What's the fuss all about?

I don't know. These are all **awesome** ways to blog, but I would never use them. I have my own setup: write Markdown text with the editor of my choice (these days it's either [Mou](mouapp.com/) or [VIM](mouapp.com/)), then run it through a custom [static site generator](https://github.com/peterldowns/website/blob/master/generate.py). This is simple, and I have total control. I don't have to fiddle around with web interfaces, and I get the best draft management software around: the UNIX filesystem + git. It's clean, it's simple, it's totally customizable, and it works.

That's not to say that Svbtle, Obtvse, or Adrian's alternative are bad, because they aren't. They're really good, and they get blogging _right_. But I don't understand why anyone would blog with a workflow that isn't already that simple. Maybe Tumblr and Blogger offer free hosting and an easy setup, but the people who read Hacker News are more than capable of rolling their own methods of blogging (or using something like [Jekyll](http://jekyllrb.com/) or [Hyde](http://ringce.com/hyde) and a setup like mine). If you're not blogging simply, you're missing the point.

----
_Comments? [Hacker News thread](http://news.ycombinator.com/item?id=3748093)_ 