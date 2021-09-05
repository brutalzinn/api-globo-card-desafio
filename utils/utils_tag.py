from services.service_tag import *


def tag_creator(list):
    listTags = []
    for t in list:
        tag = {}
        tag['name'] = t
        listTags.append(insert_tag(tag))
    return listTags

def tag_delete(list):
    listTags = []
    for t in list:
        delete_tag(str(t))
    return listTags