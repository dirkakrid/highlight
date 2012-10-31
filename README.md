# highlight

## A simple web app that highlights Python code

I've found a [script](http://code.activestate.com/recipes/578178-colorize-python-sourcecode-syntax-highlighting/) that 
colors python code in the same way that IDLE does.

The script is named *highlight.py* and is part of this repository.
You run it like this:

	>> python highlight.py -b code.py

It will open up a browser window with a highlighted version of the code from *code.py*.
The highlighting is the same as in IDLE, and you can copy paste it to *PowerPoint*, *Word*, etc..
In *PowerPoint* you might need to click the small clipboard icon after pasting and choose *Keep source formatting*.
Also, some of the newlines get lost.

If you want to do it all in the browser, you can clone [this repo](http://github.com/yoavram/highlight/), 
install [Flask](http://flask.pocoo.org/), and run 

	>> python server.py

and then open [localhost:5000](http://localhost:5000) in your browser. 
In your browser window you'll be able to paste code and click *Highlight*, at which point you'll get a highlighted version of your code.

## License

CC BY-SA 3.0

