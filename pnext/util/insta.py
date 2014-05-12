from instagram.client import InstagramAPI
from colorweave import palette
import ConfigParser, os, json, simplejson, random

class MyInstagram:
    # Ex.: { 'instagrams' : [{ 'media_id': '474834340988151412_10974184', 'img_url': '', 'link_url': '', 'title': ''}, ... ]}
    DATA_FILE_LOC = os.path.join(os.path.dirname(__file__), "../data/instagrams.json")
    CONFIG_FILE_LOC = os.path.join(os.path.dirname(__file__), "../data/api.config")
    
    def __init__(self):
        # Load configuration
        config = ConfigParser.ConfigParser()
        config.readfp(open(MyInstagram.CONFIG_FILE_LOC))
        self._access_token = config.get('instagram', 'ACCESS_TOKEN') 

        self._instagrams_list = []
        self._load_data()
        self._augment_data()
        self._save_data()

    def _load_data(self):
        try:
            self._instagrams_list = json.load(open(MyInstagram.DATA_FILE_LOC))['instagrams']
        except Exception, e:
            print "Error loading file %s: %s" % (MyInstagram.DATA_FILE_LOC, str(e))

    def _augment_data(self):
        """ Populates any missing fields via api(media_id) """
        api = InstagramAPI(access_token=self._access_token)
        for i in self._instagrams_list:
            if not 'img_url' in i or not 'link_url' in i or not 'main_color' in i:
                # Only do actual api query if we are missing something (ex: new entries)
                media = api.media(i['media_id'])
                i['title'] = media.caption.text if media.caption else ""
                i['img_url'] = media.images['standard_resolution'].url
                i['link_url'] = media.link
                i['main_color'] = palette(url=i['img_url'], n=1)[0] # First in palette
                print "Loaded new media: '%s' (title: '%s')" % (i['media_id'], i['title'])

    def _save_data(self):
        try:
            print "Saving instagram file to: %s" % MyInstagram.DATA_FILE_LOC
            with open(MyInstagram.DATA_FILE_LOC, "w") as f:
                f.write(simplejson.dumps({"instagrams" : self._instagrams_list}, indent=4))
        except Exception, e:
            print "Error saving file: %s" % str(e)

    def get_random_img(self):
        return random.choice(self._instagrams_list)

    def get_random_img_list_of_size(self, size):
        return random.sample(self._instagrams_list, size)
