from igramscraper.instagram import Instagram
from time import sleep
import re

class IGScrapper:

    def __init__(self, word, jml_data):
        self.word = word
        self.jml_data = jml_data

    def get_account_by_username(self):
        instagram = Instagram()
        account = instagram.get_account(self.word)
        return account

    def get_account_followers_by_username(self):
        instagram = Instagram()
        account = instagram.get_account(self.word).followed_by_count
        return account

    def get_account_following(self):
        instagram = Instagram()
        following = []
        account = instagram.get_account(self.word)
        sleep(1)
        following = instagram.get_following(account.identifier, 150, 100, delayed=True)
        for following_user in following['accounts']:
            print(following_user)


    def get_medias_by_tag(self):
        instagram = Instagram()
        medias = instagram.get_medias_by_tag(self.word, count=self.jml_data)

        dataMedia = []
        try:
            for x in range(0, self.jml_data):
                dataMedia.append({
                    'linkInstagram': 'http://www.instagram.com/p/' + medias[x].short_code,
                    'numberOfLikes': medias[x].likes_count,
                    'numberOfComments': medias[x].comments_count,
                    'hashtags': re.findall(r"#(\w+)", str(medias[x].caption)),
                    'caption': medias[x].caption
                })
        except IndexError as x:
            pass

        return dataMedia

    def get_account_medias_by_username(self):
        instagram = Instagram()
        dataMedia = list()
        medias = instagram.get_medias(self.word, self.jml_data)

        try:
            for x in range(0, self.jml_data):
                dataMedia.append({
                    'linkInstagram': 'http://www.instagram.com/p/' + medias[x].short_code,
                    'numberOfLikes': medias[x].likes_count,
                    'numberOfComments': medias[x].comments_count,
                    'hashtags': re.findall(r"#(\w+)", str(medias[x].caption)),
                    'caption': medias[x].caption
                })
        except IndexError as x:
            pass

        return dataMedia