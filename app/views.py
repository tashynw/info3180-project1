"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.forms import PropertyForm
from werkzeug.utils import secure_filename
from app.models import Property

###
# Routing for your application.
###


def format_price(price):
    return "${:,.2f}".format(price)


@app.route('/')
def home():
    return redirect(url_for('create_property'))


@app.route('/properties')
def properties():
    properties = db.session.execute(db.select(Property)).scalars().all()

    return render_template('properties.html', properties=properties, format_price=format_price)


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


@app.route('/properties/<propertyid>')
def get_property(propertyid):
    property = db.get_or_404(Property, propertyid)

    return render_template('property.html', property=property, format_price=format_price)


@app.route('/properties/create', methods=["POST", "GET"])
def create_property():
    form = PropertyForm()
    if form.validate_on_submit():
        file = form.photo.data
        filename = secure_filename(file.filename)

        file.save(os.path.join(
            app.config["UPLOAD_FOLDER"], filename
        ))

        property = Property(property_title=form.data["property_title"], rooms_number=form.data["rooms_number"], bathrooms_number=form.data["bathrooms_number"],
                            price=form.data["price"], property_type=form.data["property_type"], location=form.data["location"], description=form.data["description"], photo_filename=filename)
        db.session.add(property)
        db.session.commit()

        flash('Property was successfully added! ✅')
        return redirect(url_for('properties'))

    return render_template('create.html', form=form)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Tashyn Wallace")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


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
