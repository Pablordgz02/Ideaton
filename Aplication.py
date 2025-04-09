from opengateway_sandbox_sdk import Simswap
from flask import Flask

phone_number = "+34689801354"
client_id = "39c642a2-377e-4b75-9e8d-a6177cb60b39"
client_secret = "2e418c55-fb17-437f-a0af-c6eea628728d"

simswap_client = Simswap(client_id, client_secret, phone_number)


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)