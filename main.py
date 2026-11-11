from flask import Flask, render_template, request

app = Flask(__name__)  



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/vzhled')
def vzhled():
    color_theme = request.args.get("theme", "light")
    if color_theme not in ["light", "dark"]:
        color_theme = "light"
        font_size = request.args.get("font_size", 12)
        try:
            font_size = int(font_size)
            if font_size < 10 or font_size > 30:
                font_size = 12
        except ValueError:
            font_size = 12
        font_color = request.args.get("font_color", "black")
        if font_color not in ["red", "white", "green", "blue", "black"]:
            font_color = "black"
    
    return render_template('vzhled.html', color_theme=color_theme, font_size=font_size)

if __name__ == '__main__':
    app.run(debug=True)

