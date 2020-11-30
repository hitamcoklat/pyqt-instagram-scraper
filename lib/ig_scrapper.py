from igramscraper.instagram import Instagram
from time import sleep
import re

class IGScrapper:

    def get_account_by_username(username):
        instagram = Instagram()
        account = instagram.get_account(username)
        return account

    def get_account_followers_by_username(username):
        instagram = Instagram()
        account = instagram.get_account(username).followed_by_count
        return account

    def get_account_following(username):
        instagram = Instagram()
        following = []
        account = instagram.get_account(username)
        sleep(1)
        following = instagram.get_following(account.identifier, 150, 100, delayed=True)
        for following_user in following['accounts']:
            print(following_user)


    def get_medias_by_tag(tag_name, jmlData):
        instagram = Instagram()
        medias = instagram.get_medias_by_tag(tag_name, count=jmlData)

        dataMedia = []
        try:
            for x in range(0, jmlData):
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

    def get_account_medias_by_username(username, jmlData):
        instagram = Instagram()
        dataMedia = []
        medias = instagram.get_medias(username, jmlData)

        try:
            for x in range(0, jmlData):
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