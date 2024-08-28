# URL bilgilerinin bulunduğu alan
# Buradan çeşitli adreslere routing işlemi yapabilirsiniz

from flask import Blueprint
from controllers.Controller import controller_userlist, controller_index, controller_insertexample

pclist = Blueprint('pclist', __name__)
pclist.route('/', methods=['GET'])(controller_index)
pclist.route('/main/iexampleuser', methods=['GET'])(controller_insertexample)
pclist.route('/main/listuser', methods=['GET'])(controller_userlist)