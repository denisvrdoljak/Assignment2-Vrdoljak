import ConfigParser
import getpass
#file loc/name, from /users/$USER/

class Keychain:
    def __init__(self,filename=None):
        self.__configData = {}
        self.__Config = ConfigParser.ConfigParser()
        self.__username = getpass.getuser()
        self.__config_path =  "/users/" + self.__username+"/"

        if filename and '/' in filename:
            self.__config_file = filename
        else:
            self.__config_filename = filename or "keychain.config"
            self.__config_file = self.__config_path + self.__config_filename

    def set_filepath(self, path=None):
        self.__config_file = path if path and '/' in path else self.__config_path + (path or self.__config_file)

    def get_config_options(self):
        return self.__Config.sections()
        

    def loadConfigs(self, selected_configs=None):
        try:
            Config = ConfigParser.ConfigParser()

            if self.__Config.read(self.__config_file):
                for section in self.__Config.sections():                   
                    if section == selected_configs:
                       for option in self.__Config.options(section):
                            self.__configData[option] = self.__Config.get(section,option)
                return self.__configData or False

            else:
                raise Exception("Failed to load Config file")

        except:
            pass
            return False

    def setConfigsGlobal(self, config_vars=None):
        config_vars = config_vars or self.__configData
        for key, val in config_vars.items():
            exec(key + "= '" + val + "'") in globals()
        return True

######## Sample Use ########
"""

keyfob = Keychain()
key_dictionary = keyfob.loadConfigs("AWS")
print "Successful load? -->", keyfob.setConfigsGlobal(key_dictionary)
print "keysets available:", keyfob.get_config_options()

"""
