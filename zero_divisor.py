import tweepy
import os
import inspect
import json
import botometer

mashape_key = os.environ.get('MASHAPE_KEY')

twitter_app_auth = {
    'consumer_key': os.environ.get('CONSUMER_KEY'),
    'consumer_secret': os.environ.get('CONSUMER_SECRET'),
    'access_token': os.environ.get('ACCESS_TOKEN'),
    'access_token_secret': os.environ.get('ACCESS_TOKEN_SECRET'),
}

auth = tweepy.OAuthHandler(twitter_app_auth['consumer_key'], twitter_app_auth['consumer_secret'])
auth.set_access_token(twitter_app_auth['access_token'], twitter_app_auth['access_token_secret'])

api = tweepy.API(auth)

bom = botometer.Botometer(
    wait_on_ratelimit=True,
    mashape_key=mashape_key,
    **twitter_app_auth
)

def get_input():
    print('What user would you like to see?')
    return input()

input = get_input()

user = api.get_user(input)

manual_statuses_count = 0
retweets_count = 0

for tweet in tweepy.Cursor(api.user_timeline, screen_name=input, tweet_mode='extended').items():
    manual_statuses_count += 1
    if tweet.retweeted or 'RT @' in tweet.full_text:
        retweets_count += 1

print('statuses count:', user.statuses_count)
print('retweets ratio (within last ' + str(manual_statuses_count) + ' tweets):', retweets_count / manual_statuses_count)
print('followers count:', user.followers_count)
print('favorites count:', user.favourites_count)
print('creation date:', user.created_at)
print('default profile image?', user.default_profile_image)
print('botometer results:', bom.check_account(input))
print('friends count:', user.friends_count)

print('friends:')
friends = user.friends()

for friend in friends:
    print(friend.screen_name)



# 'contributors_enabled'
# 'created_at'
# 'default_profile'
# 'default_profile_image'
# 'description'
# 'entities'
# 'favourites_count'
# 'follow'
# 'follow_request_sent'
# 'followers'
# 'followers_count'
# 'followers_ids'
# 'following'
# 'friends'
# 'friends_count'
# 'geo_enabled'
# 'has_extended_profile'
# 'id'
# 'id_str'
# 'is_translation_enabled'
# 'is_translator'
# 'lang'
# 'listed_count'
# 'lists'
# 'lists_memberships'
# 'lists_subscriptions'
# 'location'
# 'name'
# 'notifications'
# 'parse'
# 'parse_list'
# 'profile_background_color'
# 'profile_background_image_url'
# 'profile_background_image_url_https'
# 'profile_background_tile'
# 'profile_banner_url'
# 'profile_image_url'
# 'profile_image_url_https'
# 'profile_link_color'
# 'profile_location'
# 'profile_sidebar_border_color'
# 'profile_sidebar_fill_color'
# 'profile_text_color'
# 'profile_use_background_image'
# 'protected'
# 'screen_name'
# 'status'
# 'statuses_count'
# 'time_zone'
# 'timeline'
# 'translator_type'
# 'unfollow'
# 'url'
# 'utc_offset'
# 'verified'
