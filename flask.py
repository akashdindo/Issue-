from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return 'Welcome to the Flask application!'

# About page route
@app.route('/about')
def about():
    return 'This is a simple Flask application example.'

# Greeting page route with a parameter
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}! Welcome to the Flask application.'

# Dynamic HTML template example
@app.route('/template')
def template():
    name = request.args.get('name', 'Guest')
    html = """
    <html>
        <body>
            <h1>Hello, {{ name }}!</h1>
            <p>Welcome to the Flask application with a template.</p>
        </body>
    </html>
    """
    return render_template_string(html, name=name)

if __name__ == '__main__':
    app.run(debug=True)
