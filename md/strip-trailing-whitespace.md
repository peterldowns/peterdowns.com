Title: How to Strip Trailing Whitespace
Author: Peter Downs
Date: Sunday, July 14, 2013

# How to Strip Trailing Whitespace

I've been thinking about coding style recently, and while reviewing
a lot of old code I noticed that I'd left trailing whitespace across
plenty of files. Because this whitespace is meaningless, I went about
removing it, which took some time. If you don't like trailing whitespace,
here's how to automatically remove trailing whitespace when saving files:

### Emacs (add to ~/.emacsrc)

    (add-hook 'before-save-hook 'delete-trailing-whitespace)

### VIM (add to ~/.vimrc)

    autocmd BufWritePre <buffer> :%s/\s\+$//e

### SublimeText (add to Preferences / Settings - User)

    { "trim_trailing_white_space_on_save": true }


Once nice addition to this is to limit this to certain file types &mdash; in Markdown,
for example, trailing whitespace can be meaningful. In VIM, use

    autocmd FileType javascript,python autocmd BufWritePre <buffer> :%s/\s\+$//e

I'm not sure how to get similar functionality in Emacs or SublimeText. If you do, 
let me know and I'll be sure to update this post!

