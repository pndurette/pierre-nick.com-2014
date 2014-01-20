from instagram.client import InstagramAPI
import os, json, simplejson, random

class MyInstagram:
    # Ex.: { 'instagrams' : [{ 'media_id': '474834340988151412_10974184', 'img_url': '', 'link_url': '', 'title': ''}, ... ]}
    DATA_FILE_LOC = os.path.join(os.path.dirname(__file__), "../data/instagrams.json")
    ACCESS_TOKEN = ""
    
    def __init__(self):
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
        api = InstagramAPI(access_token=MyInstagram.ACCESS_TOKEN)
        for i in self._instagrams_list:
            if not i['img_url'] or not i['link_url']:
                # Only do actual api query if we are missing something (ex: new entries)
                media = api.media(i['media_id'])
                i['title'] = media.caption.text if media.caption else ""
                i['img_url'] = media.images['standard_resolution'].url
                i['link_url'] = media.link
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
