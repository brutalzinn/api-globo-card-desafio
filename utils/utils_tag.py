from services.service_tag import *


def tagCreator(list):
    listTags = []
    for t in list:
        tag = {}
        tag['name'] = t
        listTags.append(insertTag(tag))
    return listTags

def tagDelete(list):
    listTags = []
    for t in list:
        deleteTag(str(t))
    return listTags