from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    
  </head>
  <body>
    <h1>Hello from Flask!</h1>
  
  </body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
