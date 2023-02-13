from flask import Flask, url_for, request
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


@app.route('/')
@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Варианты выбора!</title>
                  </head>
                  <body>
                    <h1>Мое предложение - это {planet_name}!</h1>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <div class="alert alert-dark" role="alert">
                      Классня
                    </div>
                    <div class="alert alert-success" role="alert">
                      Топовая
                    </div>
                    <div class="alert alert-light" role="alert">
                      Лучшая
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Пушка
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся к нам, го на {planet_name}
                    </div>
                  </body>
                </html>"""


@app.route('/')
@app.route('/promotion_image')
def fourth_task():
    a = ["Человечество вырастает из детства.", 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', "И начнем с Марса!", "Присоединяйся!"]
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/MARS.png" alt="здесь должна была быть картинка, но не нашлась">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-light" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/')
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <div>
                      Претендента под именем {nickname}:
                    </div>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div>
                      Составляет {rating}!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>"""


@app.route('/')
@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>МАРС ПРЕКРАСЕН</title>
                  </head>
                  <body>
                    <h1>МАРС (надо подождать чуть чуть)</h1>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <div id="carousel" class="carousel slide span12" data-ride="carousel">
                      <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                      </ol>
                      <div class="carousel-inner">
                        <div class="carousel-item active" data-interval="100">
                          <img class="img-fluid" src="/static/img/MARS.png" class="d-block w-100" alt="First slide">
                        </div>
                        <div class="carousel-item" data-interval="100">
                          <img class="img-fluid" src="/static/img/MARS2.png" class="d-block w-100" alt="Second slide">
                        </div>
                        <div class="carousel-item" data-interval="100">
                          <img class="img-fluid" src="/static/img/MARS3.png" class="d-block w-100" alt="Third slide">
                        </div>
                      </div>
                    </div>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
                  </body>
                </html>"""


@app.route('/')
@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="static/css/style1.css" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div id="main">
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="first_name" placeholder="Введите имя" name="first_name">
                                        <input type="text" class="form-control" id="second_name" placeholder="Введите фамилию" name="second_name">
                                        <br/>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Школота</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                         <p>Укажите основные профессии?</p>
                                         <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career" name="about">
                                            <label class="form-check-label" for="career">Инженер</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career2" name="about">
                                            <label class="form-check-label" for="career2">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career3" name="about">
                                            <label class="form-check-label" for="career3">Врач</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career4" name="about">
                                            <label class="form-check-label" for="career4">Биолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career5" name="about">
                                            <label class="form-check-label" for="career5">Экзобиолог</label>
                                        </div>
                                        <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="career6" name="about">
                                            <label class="form-check-label" for="career6">Метеоролог</label>
                                        </div>
                                        <br/>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <br/>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="4" name="reason"></textarea>
                                        </div>
                                        <br/>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br/>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br/>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['first_name'])
        print(request.form['second_name'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form.get('accept'))
        print(request.form['sex'])
        print(request.form['reason'])
        print(request.form)
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
