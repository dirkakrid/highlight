import highlight
from flask import Flask, request, render_template

DEBUG = True
app = Flask(__name__)

def code_to_html(code):
	classified_text = highlight.analyze_python(code)
	html = highlight.build_html_page(classified_text, title="Highlight your code")
	return html

@app.route("/",  methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		code = request.form['code']
		return code_to_html(code)


if __name__ == "__main__":
    app.run(debug=False)
