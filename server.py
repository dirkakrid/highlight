import highlight
from flask import Flask, request, render_template
import os

# add environment variables using 'heroku config:add VARIABLE_NAME=variable_name'
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
GOOGLE_ANALYTICS = os.environ.get('GOOGLE_ANALYTICS')

app = Flask(__name__)
app.config.from_object(__name__)  
app.config.from_pyfile('config.py', True)
if app.debug:
	print " * Running in debug mode"


def code_to_html(code):
	classified_text = highlight.analyze_python(code)
	html = highlight.html_highlight(classified_text)
	return html


def powerpoint_fix(html, start_pre='<pre class="python">', stop_pre='</pre>'):
	start = html.find(start_pre) + len(start_pre)
	stop = html.find(stop_pre, start)
	code = html[start:stop]
	code = code.replace("\n", "<br>")
	code = code.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
	code = code.replace("    ", "&nbsp;&nbsp;&nbsp;&nbsp;")
	return html[:start] + code + html[stop:]


@app.route("/",  methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		html = code_to_html(request.form['code'])
		if request.form['pptx'] == "true":
			html = powerpoint_fix(html)
		return html


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=app.debug)
