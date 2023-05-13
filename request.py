from venmo_api import Client
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv()

access_token = os.environ.get('VENMO_ACCESS_TOKEN')
a_id = os.environ.get('A_FRIEND_ID')
b_id = os.environ.get('B_FRIEND_ID')

client = Client(access_token=access_token)
client.payment.request_money(5.85, "spotify", a_id)
client.payment.request_money(5.85, "spotify", b_id)