# coding: utf-8
import os.path
from copy import (copy)

from state import (State)
from context import (Context)
from rendering import (render)
from loading import (load_file, load_template)
from utils import (make_unicode, html_escape)

template_globals = {}

def template(relative_path, *args, **kwargs):
    """
    A decorator for easily rendering templates.
    Use as follows:

    main.py: 
        from pystache import (template)

        @template('../tests/static/say_hello.html')
        def index():
            context = {'name' : 'world'}
            partials = {}
            return context, partials

        if __name__=="__main__":
            print index()
    
    static/say_hello.html:

        <h1> Hello, {{name}}! </h1>

    from the command line:
        
        > python main.py
        <h1> Hello, world! </h1>
    """
    directory, filename = os.path.split(relative_path)
    
    partials_dir = os.path.abspath(directory)
    name, ext = os.path.splitext(filename)

    state = State(partials_dir=directory, extension=ext, *args, **kwargs)
    template = load_template(name, directory, ext, state.encoding, state.encoding_error)

    def wrapper(fn):
        def render_template(*args, **kwargs):
            new_context, partials = fn(*args, **kwargs)
            context = copy(template_globals)
            context.update(new_context)
            return render(template, context, partials, state)
        return render_template
    return wrapper

if __name__ == "__main__":
    @template('../tests/static/say_hello.html')
    def greeter(name='world'):
        context = {'name' : name}
        partials = {}
        return context, partials
    
    print greeter(name='you awesome person, you')
