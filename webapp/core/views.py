from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view
    '''
    return render_template('index.html')


@core.route('/add')
def add():
    return render_template('add.html')