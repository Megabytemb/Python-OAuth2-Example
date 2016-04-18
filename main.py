from flask import Flask, jsonify, json, session, redirect, request, render_template
from oauth2client.contrib.flask_util import UserOAuth2

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'RandomAss2.0Key'

# By default, if you don't define a scope, it uses the 'email' scope
# Google Plus API required
oauth2 = UserOAuth2(app,
    client_secrets_file='client_secrets.json')

# The Key is to have access_type='online', this means you don't ask for a refresh token
@app.route('/')
@oauth2.required(access_type='online')
def index():
    resp, content = oauth2.http().request(
        'https://www.googleapis.com/plus/v1/people/me/openIdConnect')
    return jsonify(**json.loads(content))

@app.route('/logout')
def logout():
    # Delete the user's profile and the credentials stored by oauth2.
    session.clear()
    session.modified = True
    oauth2.storage.delete()
    return redirect(request.referrer or '/')

if __name__ == '__main__':
    app.run()