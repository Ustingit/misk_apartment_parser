import random
import os


def get_random_pause():
    return random.randint(1, 3)


def create_directory_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


def write_file(path, content):
    if content:
        with open(path, 'wb') as f:
            f.write(content)
