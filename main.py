
from line_profiler import line_profiler
from flask import Flask, render_template, redirect, url_for, request, Response


app = Flask(__name__)


@app.route('/')
@line_profiler
def main():
    return render_template('nekit.html')


if __name__ == '__main__':
    app.run(debug=True)
