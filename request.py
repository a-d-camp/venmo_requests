from venmo_api import Client
from dotenv import load_dotenv
from wonderwords import RandomWord
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv()

access_token = os.environ.get('VENMO_ACCESS_TOKEN')
a_id = os.environ.get('A_FRIEND_ID')
b_id = os.environ.get('B_FRIEND_ID')

r = RandomWord()
memo_a = r.word(include_parts_of_speech=["adjectives"])
memo_b = r.word(include_parts_of_speech=["adjectives"])

client = Client(access_token=access_token)
client.payment.request_money(5.85, memo_a, a_id)
client.payment.request_money(5.85, memo_b, b_id)
