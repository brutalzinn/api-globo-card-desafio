from bson.objectid import ObjectId
def validate_id(id):
    try:
        ObjectId(id)
        return True
    except:
        return False

