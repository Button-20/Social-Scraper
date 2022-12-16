from fastapi import FastAPI
import instaloader as instagram

app = FastAPI()

@app.get('/')
def home_page():
    data_set = {
        'message': 'Uhh 😰!!!!! You are lost!'
    }
    # json_dump = json.dumps(data_set)

    return data_set

@app.get('/instagram/{username}')
def getInstagramProfile(username: str):
    try:
        #Create an instance of Instaloader class
        insta = instagram.Instaloader({
            'quiet': True,
        })
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
        return data
    except:
        data_set = {
            'message': 'Error Occured!'
        }
        return data_set

