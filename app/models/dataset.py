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

    def get_xy(self,lat=None,lon=None,limit=1):
        point = Vic_Conus_3km.objects(point__near=[lon,lat]).limit(limit)
        return point.to_json()

    def get_data(self,x=None,y=None):
        pass

    def make_json(self):
        pass


