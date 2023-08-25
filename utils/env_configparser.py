import configparser
from pathlib import Path

config_file = 'petsenvqa.ini'
config_file_dir = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(config_file_dir).joinpath(config_file)

config.read(CONFIG_FILE)


def get_pet_env_qa():
    return (config['pet_env_qa']['url'])


def get_pet_store_env_qa():
    return (config['pet_store_env_qa']['url'])


print(get_pet_env_qa())
print(get_pet_store_env_qa())
