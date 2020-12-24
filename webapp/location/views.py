from flask import render_template,request,Blueprint

locations = Blueprint('locations', __name__)

@locations.route('/location/<location>')
def location_view(location):
    print("received:", location, type(location))
    comp = location.split('#')
    # TODO there must be a better to pass this arguments list
    # also, this doesn't work for favicon.ico. Although it does
    # not affect the functionality. But throwing errors in log
    location_id = comp[0]
    desc = comp[1]
    return render_template('location.html', location=location_id, desc=desc)