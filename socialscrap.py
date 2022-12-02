import json

import instaloader as instagram
from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {
        'message': 'Uhh 😰!!!!! You are lost!'
    }
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/instagram/', methods=['GET'])
def getInstagramProfile():
    try:
        #Create an instance of Instaloader class
        insta = instagram.Instaloader()
        username = str(request.args.get('username'))
        print(username)
        profile = instagram.Profile.from_username(insta.context, username)
        data = {
            "username": profile.username,
            "user_id": profile.userid,
            "number_of_posts": profile.mediacount,
            "followers_count": profile.followers,
            "following_count": profile.followees,
            "bio": profile.biography,
            "external_url": profile.external_url,
            "profile_pic_url": profile.profile_pic_url
        }
        json_dump = json.dumps(data)

        return json_dump
    except:
        data_set = {
            'message': 'Error Occured!'
        }
        json_dump = json.dumps(data_set)

if __name__ == '__main__':
    app.run()


