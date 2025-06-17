import os
import yaml


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ImportFile:
    def import_testdata(self, file):
        try:
            with open(os.path.join(BASE_DIR, file)) as file:
                testdata = yaml.load(file, Loader=yaml.FullLoader)
                return testdata
        except FileNotFoundError:
            raise FileNotFoundError
