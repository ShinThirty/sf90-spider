from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view
    '''
    places = {}
    places["locationA"] = "A great place for hiking!!"
    places["locationB"] = "A somewhat good place for hiking!"
    places["locationC"] = "A not-so good place for hiking"
    places["locationD"] = "A bad good place for hiking.."
    return render_template('index.html', places=places)


@core.route('/add')
def add():
    return render_template('add.html')