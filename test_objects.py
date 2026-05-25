from mygit.objects import Blob


def test_blob():
    blob = Blob(b"hello")

    assert blob.hash is not None