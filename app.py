from flask import Flask, render_template, redirect

app = Flask(__name__)

# Mock movie data function
def get_movies():
    return [
        {'title': 'Action Movie 1', 'category': 'action', 'image': 'static/action1.jpg', 'description': 'A thrilling action-packed movie.'},
        {'title': 'Action Movie 2', 'category': 'action', 'image': 'static/action2.jpg', 'description': 'An explosive blockbuster action movie.'},
        {'title': 'Comedy Movie 1', 'category': 'comedy', 'image': 'static/comedy1.jpg', 'description': 'A fun and lighthearted comedy.'},
        {'title': 'Comedy Movie 2', 'category': 'comedy', 'image': 'static/comedy2.jpg', 'description': 'A hilarious comedy movie that will make you laugh.'},
        {'title': 'Horror Movie 1', 'category': 'horror', 'image': 'static/horror1.jpg', 'description': 'A chilling and spooky horror movie.'},
        {'title': 'Horror Movie 2', 'category': 'horror', 'image': 'static/horror2.jpg', 'description': 'Get ready for scares in this horror movie.'}
    ]

# Filter by category
def get_movies_by_category(category):
    all_movies = get_movies()
    return [movie for movie in all_movies if movie['category'] == category]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/watch')
def watch():
    return redirect("/sponsor")

@app.route('/category/<category_name>')
def category(category_name):
    movies = get_movies_by_category(category_name)
    return render_template('category.html', category_name=category_name, movies=movies)


@app.route('/sponsor')
def sponsor():
    # Redirect to sponsor (Shotify) link
    return redirect("https://shrinkme.ink/epsilonmovies")

@app.route('/afterSponsor')
def after_sponsor():
    # Redirect to NetMirror after sponsor
    return redirect("https://netfree2.cc/login")

if __name__ == '__main__':
    app.run(debug=True)
