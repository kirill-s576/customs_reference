class Excel(object):
    def __init__(self):
        self.path = ""

    def file_path(self, path: str):
        self.path = path
        return self

    def get_fields(self):
        pass

    def get_objects(self):
        pass


class ExcelPaymentTypes(Excel):
    pass


class ExcelCountry(Excel):
    pass
