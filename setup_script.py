from venmo_api import Client
from utils import Venmo

access_token = Client.get_access_token(username='Andrew-D-Camp',
                                       password='Oligarchy7!')
venmo = Venmo(access_token)
userId = venmo.get_user_id_by_username("Andrew-D-Camp")