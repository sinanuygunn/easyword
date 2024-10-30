import os
import json

class ConfigManager:
    _configName = "config.json"
    _configPath = "./"
    _getConfigPath = str(_configPath + _configName )
    _defaultConfig = {
        "version": [1, 0],
        "words": {}
    }

    def checkConfig():
        if os.path.exists(ConfigManager._getConfigPath):
            return True
        else:
            return False
        
    def createConfigIfExists(exists:bool):
        if exists:
            return
        else:
            with open(ConfigManager._getConfigPath, 'w') as f:
                json.dump(ConfigManager._defaultConfig, f)

    def getConfig(whatToGet: str, configdef: dict = None) -> dict:
        '''
        if whattoget all then return the config
        else return the config[whattoget]
        '''
        if configdef is None:
            with open(ConfigManager._getConfigPath, 'r') as f:
                config = json.load(f)
            if whatToGet == "all":
                return config
            else:
                return config[whatToGet]
        else:
            if whatToGet == "all":
                return configdef
            else:
                return configdef[whatToGet]
            
    def writeConfig(whereToWrite: str, value):
        with open(ConfigManager._getConfigPath, 'r') as f:
            config = json.load(f)
        config[whereToWrite] = value
        with open(ConfigManager._getConfigPath, 'w') as f:
            json.dump(config, f)