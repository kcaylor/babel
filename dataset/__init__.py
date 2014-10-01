from app import opendap_databases

class Dataset(object):
    """docstring for Dataset"""
    def __init__(self, arg):
        super(Dataset, self).__init__()
        self.arg = arg
        self.name = 'vic_conus_3km'
        self.collection = opendap_databases[self.name]

    def get_xy(self,lat=None,lon=None):
        # Do the search
        return x, y

    def get_data(self,x=None,y=None):
        pass

    def make_json(self):
        pass



        