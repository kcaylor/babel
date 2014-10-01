from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
opendap_database = client['opendap_databases']

opendap_database_list = opendap_database['database_list']

# for item in opendap_database_list:
#   this_database = database_init(item.name)
#   database_list[item.name] = this_database


class Dataset(object):
    """docstring for Dataset"""
    def __init__(self):
        super(Dataset, self).__init__()
        self.name = 'vic_conus_3km'
        self.collection = opendap_database[self.name]

    def get_xy(self,lat=None,lon=None):
        # Do the search
        return x, y

    def get_data(self,x=None,y=None):
        pass

    def make_json(self):
        pass

# This will end up somewhere else...
database_list = {}
my_dataset = Dataset()
database_list[my_dataset.name] = my_dataset

        