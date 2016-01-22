from app import db
from sqlalchemy.dialects.prostgresql import JSON


class Visit(db.Model):
	__tablename__ = 'visits__c'

	app_user_id__c = db.Column(db.String(200))
	name = db.Column(db.String(200))
	sfid = db.Column(db.String(200))
	user_name__c = db.Column(db.String(200))
	geopoints__latitude__s = db.Column(db.Float())
	geopoints__longitude__s = db.Column(db.Float())
	location__c = db.Column(db.String(200))
	salesforce_contact__c = db.Column(db.String(200))