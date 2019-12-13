from igramscraper.instagram import Instagram
import csv


class Scraper():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.scraper = Instagram()
        self.scraper.with_credentials(username, password)
        self.scraper.login()
    
    def target_by_username(self, target_name, tweet_count=None):
        rows = [['username', 'full name', 'biography', 'prive', 'verfied', 'picture']]
        target  = self.scraper.get_account(target_name)
        if not tweet_count:
            tweet_count = target.follows_count
        followers = self.scraper.get_followers(target.identifier, tweet_count, 100, delayed=True)
        for item in followers['accounts']:
            rows.append([item.username, item.full_name, item.biography, item.is_private, item.is_verified, item.profile_pic_url])
        return rows
    