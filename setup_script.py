from venmo_api import Client
from utils import Venmo

access_token = Client.get_access_token(username='',
                                       password='')
venmo = Venmo(access_token)
userId = venmo.get_user_id_by_username("")
