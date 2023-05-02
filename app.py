from flask import Flask, jsonify, render_template, redirect, url_for

app = Flask(__name__)

Movies = [
    {
        'id': 1,
        'name': 'El Camino',
        'imdb': 7.3,
        'producer': 'Vince Gilligan',
        'image': 'https://www.indiewire.com/wp-content/uploads/2019/10/El-Camino-Jesse-Netflix.jpg?resize=1024,683',
        'status': 'active'
    },
    {
        'id': 2,
        'name': 'La La Land',
        'imdb': 8.0,
        'producer': 'Damien Chazelle',
        'image': 'https://static01.nyt.com/images/2016/09/19/arts/la-la-land-watching/19TORONTO-jumbo.jpg?quality=75&auto=webp',
        'status': 'active'
    },
    {
        'id': 3,
        'name': 'Truman Show',
        'imdb': 8.1,
        'producer': 'Peter Weir',
        'image': 'https://www.nzherald.co.nz/resizer/0x9wQwogrviXc0QVLSI-AZoWiDM=/1440x810/smart/filters:quality(70)/cloudfront-ap-southeast-2.images.arcpublishing.com/nzme/PF4ROLSNHJHNVTGQS4BJYQ4XSA.jpg',
        'status': 'active'
    },
    {
        'id': 4,
        'name': 'Midsommar',
        'imdb': 7.1,
        'producer': 'Ari Aster',
        'image': 'https://images.mubicdn.net/images/film/210029/cache-416486-1636971271/image-w1280.jpg?size=800x',
        'status': 'realased'
    },
    {
        'id': 5,
        'name': 'Interstellar',
        'imdb': 8.6,
        'producer': 'Christopher Nolan',
        'image': 'https://media.npr.org/assets/img/2014/11/13/fl-17895r_wide-d745edc663a75ddc961f66684631a621dc148566-s800-c85.webp',
        'status': 'active'
    }
]

@app.route('/movies/')
def movies():
    active_movies = [movie for movie in Movies if movie['status'] == 'active']
    return render_template('movies.html', movies=active_movies)


@app.route('/movie/<int:id>')
def movie(id):
    movie = [movie for movie in Movies if movie['id'] == id]
    if movie:
        return render_template('movie.html', movie_1 = movie)
    else:
        return 'Film yoxdur!'


