class Cow:
    # constructor
    def __init__(self, name: int):
        self._name = name
        self._image = None

    # returns cow name
    def get_name(self):
        return self._name

    # returns image to display cow
    def get_image(self):
        return self._image

    # sets image to display cow
    def set_image(self, _image: str):
        self._image = _image
