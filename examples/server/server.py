from phe import paillier
import json
from random import *
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import logging

app = FlaskAPI(__name__)


# Set the log level (optional, defaults to WARNING)
app.logger.setLevel(logging.DEBUG)

# Create a FileHandler to log to a file (optional)
file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)

@app.route("/", methods=['POST'])
def process():

    if request.method == 'POST':
       app.logger.debug('This is a debug message:%s',request.data)
       received_dict = json.loads(request.data)
       print(received_dict)
       public_key_rec = paillier.PaillierPublicKey(n=int(received_dict['public_key']['n']))
       enc_nums_rec = [paillier.EncryptedNumber(public_key_rec, int(x[0]), int(x[1])) for x in received_dict['values']]
       x = randint(1, 10) 
       result  = {}
       result['values'] = [(str(enc_num.ciphertext()), enc_num.exponent) for enc_num in [(num * x)for num in enc_nums_rec]]

       return json.dumps(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
