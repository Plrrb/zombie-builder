class __Input__:
    __slots__ = ("inputs",)

    def __init__(self):
        self.inputs = {}


class BooleanInput(__Input__):
    __slots__ = ("inputs",)

    def __getitem__(self, name):
        return self.inputs.get(name, False)

    def press(self, name):
        self.inputs[name] = True

    def release(self, name):
        self.inputs[name] = False


class NumericalInput(__Input__):
    __slots__ = ("inputs",)

    def __getitem__(self, name):
        return self.inputs.get(name, 0)

    def set(self, name, value):
        self.inputs[name] = value
