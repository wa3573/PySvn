__author__ = 'dsoprea'

import unittest
import tempfile
import shutil
import logging

import wjasvn.admin
import wjasvn.remote

_LOGGER = logging.getLogger(__name__)


class TestAdmin(unittest.TestCase):
    """
    For testing wjasvn/admin.py
    """

    def shortDescription(self):
        return None

    def test_create_repository(self):
        """
        Testing repository creation.
        :return:
        """

        temp_path = tempfile.mkdtemp()
        shutil.rmtree(temp_path)

        a = wjasvn.admin.Admin()

        try:
            # Create.
            a.create(temp_path)

            # Do a read.
            rc = wjasvn.remote.RemoteClient('file://' + temp_path)
            info = rc.info()
            _LOGGER.debug("Info from new repository: [%s]", str(info))
        finally:
            try:
                shutil.rmtree(temp_path)
            except:
                pass

