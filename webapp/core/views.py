from flask import render_template,request,Blueprint
from webapp.core.forms import AddSpotForm
from webapp.core.forms import *

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view
    '''
    places = []
    places.append(["locationA", "A great place for hiking!!", "image1"])
    places.append(["locationB", "A somewhat good place for hiking!", "image2"])
    places.append(["locationC", "A not-so good place for hiking", "image3"])
    places.append(["locationD", "A not-so good place for hiking", "image4"])
    return render_template('index.html', places=places)


@core.route('/add', methods=['GET', 'POST'])
def add():
    form = AddSpotForm()
    if form.validate_on_submit():
        print("submitted!\naddress:{}\nlength:{}\ndesc:{}".format(\
            form.address.data,\
            get_lenth_range(form.length_selection.data),\
            form.desc.data))
    return render_template('add.html', form=form)