from venmo_api import Client
from dotenv import load_dotenv
import os
import pickle

# load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv()
access_token = os.environ.get('VENMO_ACCESS_TOKEN')

# load request info from file
with open('./request_data.pickle', 'rb') as handle:
    request_data = pickle.load(handle)

# initialize venmo client
client = Client(access_token=access_token)

# make requests
for id in request_data:
    friend_id = request_data[id]['friend_id']
    #name = request_data[id]['friend'].upper()
    #friend_id = os.environ.get(name)
    amount = request_data[id]['amount']
    memo = request_data[id]['reason']
    client.payment.request_money(amount, memo, friend_id)
