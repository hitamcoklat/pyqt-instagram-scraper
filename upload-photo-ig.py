from instapy_cli import client

username = 'gerai_hijab_murah'
password = 'sukagalih1234'
image = 'ubuntu-18.04-default-wallpaper-2.jpg'
text = 'This will be the caption of your photo.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

with client(username, password) as cli:
    cli.upload(image, text)