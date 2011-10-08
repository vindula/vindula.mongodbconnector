from zope.interface import Interface
from zope import schema

class IMongoDBConnector(Interface):
    """
    MongoDB Connector interface
    """
    host = schema.TextLine(title=u"Address of the host",default=u"127.0.0.1")
    port = schema.Int(title=u"Port used by the mongodb",default=27017,min=1,max=65535)
    db_name = schema.TextLine(title=u"Database name",default=u"database")
    