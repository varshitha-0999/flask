from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data to store reviews
reviews = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/reviews', methods=['GET', 'POST'])
def movie_reviews():
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        experience = request.form['experience']
        rating = request.form['rating']
        reviews.append({'movie_name': movie_name, 'experience': experience, 'rating': rating})
        return redirect(url_for('movie_reviews'))

    return render_template('reviews.html', reviews=reviews)


if __name__ == '__main__':
    app.run(debug=True)