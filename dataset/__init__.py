from pymongo import MongoClient
import os 

# Go setup the database connection to compose.io:
mongo_user = os.environ.get('MONGO_USER','none')
mongo_password = os.environ.get('MONGO_PASSWORD','none')
mongo_url = 'mongodb://'+mongo_user+':'+mongo_password+\
    '@linus.mongohq.com:10009/opendap_datasets'
opendap_datasets = MongoClient(mongo_url)
dataset_list = opendap_datasets['dataset_list']

# for item in opendap_database_list:
#   this_database = database_init(item.name)
#   database_list[item.name] = this_database


class Dataset(object):
    """docstring for Dataset"""
    def __init__(self):
        super(Dataset, self).__init__()
        self.name = 'vic_conus_3km'
        self.collection = opendap_datasets[self.name]

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

        