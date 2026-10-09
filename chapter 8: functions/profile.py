#8-13. User Profile: Start with a copy of
#user_profile.py from page 148.
#Build a profile of yourself by calling build_profile(), using your first and last
#names and three other key-value pairs that describe you.

def build_profile(first, last, **info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in info.items():
        profile[key] = value
    return profile

my_profile = build_profile('elia', 'ghazal', location='new york', field='computer science')
