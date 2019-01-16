from app import db

class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data

class Brew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    description = db.Column(db.String(500))
    batch_size = db.Column(db.String(64))

    def __repr__(self):
        return '<Brew {}>'.format(self.name)

    def to_dict(self):
        data = {
            'id': self.id,
            "name": self.name,
            "description": self.description,
            "batchSize": self.batch_size
            # "ingredients": self.ingredients,
            # "steps": self.steps,
        }
        return data

    def from_dict(self, data, new_brew=False):
        for field in ['name', 'description', 'batchSize']:
            if field in data:
                setattr(self, field, data[field])
                