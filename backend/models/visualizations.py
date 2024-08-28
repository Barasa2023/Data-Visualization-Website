class Visualization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data_id = db.Column(db.Integer, db.ForeignKey('data.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    config = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', backref=db.backref('visualizations', lazy=True))
    data = db.relationship('Data', backref=db.backref('visualizations', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'data_id': self.data_id,
            'title': self.title,
            'config': self.config,
            'created_at': self.created_at
        }