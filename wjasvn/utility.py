import os

import wjasvn.common
import wjasvn.local
import wjasvn.remote
import wjasvn.constants

def get_client(url_or_path, *args, **kwargs):
    if url_or_path[0] == '/':
        return wjasvn.local.LocalClient(url_or_path, *args, **kwargs)
    else:
        return wjasvn.remote.RemoteClient(url_or_path, *args, **kwargs)

def get_common_for_cwd():
    path = os.getcwd()
    uri = 'file://{}'.format(path)

    cc = wjasvn.common.CommonClient(uri, wjasvn.constants.LT_URL)
    return cc
