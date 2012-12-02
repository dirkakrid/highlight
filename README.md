# highlight

## A simple Python web app that highlights Python code

The app highlights [Python] source code with the same color scheme as *IDLE*, the default [Python] IDE. The purpose of this project was three-fold, but more purposes emerged later on:

  1. Display code in educational presentations with the same coloring scheme used by the IDE begginers normally use.
  1. Showcase the quick development (<30 mins) of a [Flask] web app.
  1. Learn how to deploy web apps to [Heroku]. Turns out it's *easier* then I thought.
  1. Learn how to do AJAX with [jQuery] and [Flask].
  
## Use online

The app runs at [highlight.yoavram.com](http://highlight.yoavram.com/) and can be freely used by anyone.

## Use on localhost

If you want to, you can clone [this repo](http://github.com/yoavram/highlight/), 
install [Flask](http://flask.pocoo.org/), and run 

	>> python server.py

Then open [localhost:5000](http://localhost:5000) in your browser, and you'll be able to paste code, click *Highlight*, and get a highlighted version of your code.

## Run from command line

The script is named [highlight.py](https://raw.github.com/yoavram/highlight/master/highlight.py) and is part of this repository.
You can run it from the command line:

	>> python highlight.py -b code.py

It will open up a browser window with a highlighted version of the code from *code.py*.
It can also output *LaTeX* and *PDF* (via *pdflatex*).

## Use with PowerPoint

I've added a *PowerPoint fix* - if you want to paste to *PowerPoint*, you need to check the checkbox before clicking *Highlight*, then copy the code, and when you paste it in *PowerPoint* click the small clipboard icon after pasting and choose *Keep source formatting*. The fix is neccesarry to avoid losing new lines and indentation - it replaces newlines with `<br>` elements and tabs with HTML space elements.

## Credits and License

The app is written in [Python], uses the wonderful [Flask] web microframework and is deployed on [Heroku]. It also uses [jQuery] for showing the highlighted code side by side with the user input.

The highlighting is done using a [script](http://code.activestate.com/recipes/578178-colorize-python-sourcecode-syntax-highlighting/) by *Raymond Hettinger* I found online. The highlighter itself is licensed under the [MIT License](http://en.wikipedia.org/wiki/MIT_License)

The web app was developed by [Yoav Ram] and is licensed under [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/).

[![CC BY-NC-SA 3.0](http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png)](http://creativecommons.org/licenses/by-nc-sa/3.0/)

[Python]: http://python.org/
[Flask]: http://flask.pocoo.org/
[Heroku]: http://www.heroku.com/
[jQuery]: http://jquery.com/
[Yoav Ram]: http://www.yoavram.com/