
"""

For this app to work, two environment variables need to be set:
`QFAP_SERVER`: The endpoint leading to the MongoDB server.
`QFAP_SECRET`: A secret key used by Flask.

"""

import os

import qfap

from flask import Flask, render_template, session


app = Flask(__name__)

# Set Flask secret
secret_env_var = 'QFAP_SECRET'
secret = os.getenv(secret_env_var)
if not secret:
    raise ValueError(f'{secret_env_var} environment variable is not set')
app.secret_key = secret.encode()


db = qfap.Database(database_name='QFAP', collection_name='dataset')


@app.route('/')
def home():
    return render_template('index.html', db=db)


@app.route('/event/<identifier>')
def unique_event(identifier: int):
    event = db.get_unique_event_by_id(identifier)
    return render_template('event.html', db=db, event=event)


if __name__ == '__main__':
    app.run(debug=True)