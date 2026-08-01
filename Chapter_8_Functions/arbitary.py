def build_profile(first_name,last_name,**user_info):
    return first_name,last_name,user_info

user_profile = build_profile('alice','north',location = 'paris',field='cs')

print(user_profile)