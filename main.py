from flask import Flask

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/')
@app.route('/promotion')
def promotion():
    a = ["Человечество вырастает из детства.", 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(a)


@app.route('/')
@app.route('/image_mars')
def img_mars():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/MARS.png" alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')