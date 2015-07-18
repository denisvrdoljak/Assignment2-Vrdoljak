from slistener import SListener
import time, tweepy, sys


auth_MODE = "Twitter"
UTILS_FOLDER = "DenisUtils"

#setConfigVars(loadConfigs(auth_MODE))
import getpass

username = getpass.getuser()
utils_path = "/users/" + username + "/" + UTILS_FOLDER
sys.path.append(utils_path)

import Keychain
keyfob = Keychain.Keychain()
#print "keysets available:", keyfob.get_config_options()
key_dictionary = keyfob.loadConfigs("Twitter")
print "Successful keys load? -->", keyfob.setConfigsGlobal(key_dictionary)
for key, val in key_dictionary.items():
    exec(key + "= '" + val + "'") in globals()
########################


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#api      = tweepy.API(auth)

def main():
    track = ['#Warriors',]
 
    listen = SListener(api, 'Warriors_JSON')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
