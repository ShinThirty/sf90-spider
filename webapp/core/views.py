from flask import render_template,request,Blueprint
from webapp.core.forms import AddSpotForm
from webapp.core.forms import *
from webapp import *
import json

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view
    '''
    global location_id

    places = []
    places.append(["locationA", "A great place for hiking!!", "image1"])
    places.append(["locationB", "A somewhat good place for hiking!", "image2"])
    places.append(["locationC", "A not-so good place for hiking", "image3"])
    places.append(["locationD", "A not-so good place for hiking", "image4"])
    # get all up to current highest location_id
    print("location-1", location_id)
    for i in range(location_id):
        loc_id = "location" + str(i)
        loc_entry = redis_store.get(loc_id)
        data = json.loads(loc_entry)
        places.append([data['address'], data['desc'], "NoImage"])
    return render_template('index.html', places=places)

@core.route('/add', methods=['GET', 'POST'])
def add():
    form = AddSpotForm()
    if form.validate_on_submit():
        print("submitted!\naddress:{}\nlength:{}\ndesc:{}".format(\
            form.address.data,\
            get_lenth_range(form.length_selection.data),\
            form.desc.data))
        new_id = "location" + str(location_id)

        new_entry = {}
        new_entry['address'] = form.address.data
        new_entry['length'] = get_lenth_range(form.length_selection.data)
        new_entry['desc'] = form.desc.data
        json_data = json.dumps(new_entry)

        redis_store.set(new_id, json_data)
        location_id += 1
    return render_template('add.html', form=form)