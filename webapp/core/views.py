from flask import render_template,request,Blueprint
from webapp.core.forms import AddSpotForm
from webapp.core.forms import *
from webapp import *
import uuid
import os
from werkzeug.utils import secure_filename

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view
    '''
    global location_id

    places = []
    places.append(["locationA", "A great place for hiking!!", "image1.jpeg"])
    places.append(["locationB", "A somewhat good place for hiking!", "image2.jpeg"])
    places.append(["locationC", "A not-so good place for hiking", "image3.jpeg"])
    places.append(["locationD", "A not-so good place for hiking", "image4.jpeg"])
    # get all up to current highest location_id
    spots_ref = firestore_storedb.collection('spots_data')
    spots = spots_ref.stream()
    for spot in spots:
        spot_id = spot.id
        spot_data = spot.to_dict()
        image_name = spot_data.get("image", "NOTFOUND")
        print(spot_data)
        if image_name != "NOTFOUND":
            blob = storage.Blob(image_name, image_bucket)
            with open('webapp/static/pics/' + image_name, 'wb') as file_obj:
                storage_client.download_blob_to_file(blob, file_obj)
            print("downloaded a file:", image_name)
        data = [spot_data['address'], spot_data['desc'], image_name]
        places.append(data)
    return render_template('index.html', places=places)

@core.route('/add', methods=['GET', 'POST'])
def add():
    global location_id
    form = AddSpotForm()
    if form.validate_on_submit():
        print("submitted!\naddress:{}\nlength:{}\ndesc:{}".format(\
            form.address.data,\
            get_length_range(form.length_selection.data),\
            form.desc.data))
        new_id = "location" + str(location_id)

        new_entry = {}
        new_entry['address'] = form.address.data
        new_entry['length'] = get_length_range(form.length_selection.data)
        new_entry['desc'] = form.desc.data
        
        if form.image.data is not None:
            filename = "image-{}.jpeg".format(str(uuid.uuid4()))
            form.image.data.save(filename)
            blob = image_bucket.blob(filename)
            blob.upload_from_filename(filename)
            new_entry['image'] = filename
            os.remove(filename)

        spots_ref = firestore_storedb.collection('spots_data').document(form.address.data)
        spots_ref.set(new_entry)
        location_id += 1
        return render_template('add_confirm.html')
    return render_template('add.html', form=form)