"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, Flask,send_file
from app.forms import myform 
from app.models import userProfile
import datetime
import os
from werkzeug.utils import secure_filename
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/profiles') 
def profiles():
    allUsers = db.session.query(userProfile).all() #CHECK ALL USERPROFILE and change to db. check if it works first
    return render_template('profiles.html',allUsers=allUsers)

path = app.config['UPLOAD_FOLDER'] #check if this is the right path to the img folder
# this is where the images are stored

@app.route('/profile',methods=['GET', 'POST'])
def profile():
    form = myform()
    if request.method == 'POST' and form.validate_on_submit():
        img = form.image.data
        filename = secure_filename(img.filename)
        img.save(os.path.join(path,filename))
        
        #redirect(request.url)
        user = userProfile(
            firstname= request.form["firstname"], 
            lastname= request.form["lastname"], 
            email= request.form["email"], 
            gender= request.form["gender"] ,
            location= request.form["location"], 
            bio= request.form["bio"],
            image = filename,
            date=datetime.datetime.now().strftime("%B %d, %Y")
            
        )
            # if image not showing this may be the issue.
        
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('profiles'))
    return render_template('profile.html', form=form)


@app.route('/profile/<int:userid>')
def show_user(userid):
    user = db.session.query(userProfile).get(userid)
    return render_template('userProfile.html', user=user) #this show be link to the show profile button in profiles.html

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
