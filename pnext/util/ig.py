from instagram.client import InstagramAPI
import os, json, random

class MyInstagram:
    MEDIA_IDS_FILE = os.path.join(os.path.dirname(__file__), "../data/instagrams.json")
    ACCESS_TOKEN = "10974184.1d5ac95.5478d52949e343b69a3d93997de90cd5"
    
    def __init__(self):
        self.__media_ids_list = json.load(open(MyInstagram.MEDIA_IDS_FILE))['media_ids']
        self.__img_dicts = self.__get_img_dicts(self.__media_ids_list) 

    def __get_img_dicts(self, medias_ids_list):
        api = InstagramAPI(access_token=MyInstagram.ACCESS_TOKEN)
        
        img_dicts = []
        for media_id in medias_ids_list:
            media = api.media(media_id)
            title = media.caption 
            img = media.images['standard_resolution'].url
            link = media.link
            img_dicts.append({"title": title, "img": img, "link": link})
        return img_dicts

    def get_random_img(self):
        return random.choice(self.__img_dicts)
