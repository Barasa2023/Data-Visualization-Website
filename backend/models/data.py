class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    filepath = db.Column(db.String(300), nullable=False)
    upload_date = db.Column(db.DateTime, server_default=db.func.now())

    user = db.relationship('User', backref=db.backref('data', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'filename': self.filename,
            'filepath': self.filepath,
            'upload_date': self.upload_date
        }
