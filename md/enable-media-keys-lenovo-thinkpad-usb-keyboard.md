Title: Enabling Media Keys on a Lenovo Thinkpad USB Keyboard
Author: Peter Downs
Date: Thursday, October 16, 2014

# Enabling Media Keys on a Lenovo Thinkpad USB Keyboard

Some time in 2013 I switched to using a [Lenovo Thinkpad USB
Keyboard](http://www.amazon.com/ThinkPad-USB-Keyboard-with-TrackPoint/dp/B002ONCC6G) as my main programming
keyboard. I did so for a few reasons: its keys are simultaneously cushy and
responsive; it has a dedicated right-click button; and the [trackpoint
mouse](http://xkcd.com/243/) is extremely useful for making quick mousing
gestures without lifting my hands from the keyboard.

When I left my job in June 2014 I had to leave the keyboard at work.
Unfortunately, in my quest for a replacement I learned that it is now nearly
impossible to purchase one for a reasonable price. I was forced to buy [the
updated version](http://www.amazon.com/gp/product/B00F3U4TQS/), which has the
advantage of being simulatenously reasonably priced and easily purchasable via
Amazon (one of my all-time favorite combinations of attributes.)

The new model gets rid of the extended palm rests of the original and switches
to a chiclet-style keyboard that I have ended up liking (despite my initial
concerns) even more than the old-school keys on the first version. The only
downside is that there is no longer a dedicated way to send media keys
(previous, play/pause, forward) like there used to be. The original keyboard
would send media keys when you held the function key and pressed an arrow key.
This was great, I was happy, and the key events being sent worked just like the
dedicated keys on my Macbook Air's keyboard.

The solution is simple but non-obvious. First, install
[Karabiner](https://pqrs.org/osx/karabiner/). Open that up and
enable the setting below:

![Karabiner settings](/static/img/karabiner-settings.png)

There you go – now `F10`, `F11`, and `F12` will work as media keys.  I took a
look at adding a [custom key
definition](https://pqrs.org/osx/karabiner/xml.html.en) to change this to `fn
+ <arrow key>`, but I was unable to get it to work. Pressing a naked arrow key
sends `fn + <arrow key>` to the computer; holding `fn` and pressing
`<arrow key>` does not send *any* keys to the computer. Also strange: I was
unable to get the keyboard's `FnLk` setting to work, so each of the `F<1-12>`
keys are being sent to the computer as `fn + <F key>`. If you don't believe me
you can play around in the event viewer – if anyone has an explanation of this
or a workaround I'd be happy to share it here. In the meantime, I'm happy to
have *any* working media keys.
