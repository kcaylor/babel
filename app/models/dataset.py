from . import db

class Vic_Conus_3km(db.Document):

    point = db.PointField(db_field='point')
    x = db.IntField()
    y = db.IntField()

    meta = { 
        'collection': 'vic_conus_3km'
    }

    def __repr__(self):
        return '<Point %r>' % self.get_id()

    def get_id(self):
        return unicode(self.id)

class Dataset(db.Document):

    name = db.StringField(db_field='name')
    # the precision of the data should be defined, otherwise 0 becomes 0.0000000000something
    precision = db.IntField(default=8)
    url = db.StringField()

    meta = {
        'collection': 'dataset_list',
        'indexes': [
            'name'
        ]
    }


    def __repr__(self):
        return '<Dataset %r>' % self.name

    def get_id(self):
        return unicode(self.id)

    def get_xy(self,lat=None,lon=None,limit=100):
        point = Vic_Conus_3km.objects(point__near=[lon,lat]).limit(limit)
        return point.to_json()

    def get_data(self,x=None,y=None,var=None):
        if not var:
            var = 'prec'
        # var should be passed together with x and y
        # time must be passed too, but so far we just pick all the data from July 1st, 2009
        subset = self.data[var][var][1,y,x][0]*self.data[var].scale_factor+self.data[var].add_offset
        # the type of the output must be defined, so far it is numpy.ndarray
        # NoData must be managed too, they are defined as data[var]._FillValue, maybe they can be returned as a separate variable
        return subset.round(self.precision) #, data[var]._FillValue
 

    def make_json(self):
        pass


