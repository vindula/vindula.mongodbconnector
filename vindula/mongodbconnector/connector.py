from five import grok
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.z3cform import layout
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from interfaces import IMongoDBConnector
from pymongo import Connection

class MongoDBConnector(grok.GlobalUtility):
    """
    Provides a mongodb connection
    """
    grok.provides(IMongoDBConnector)

    def getDBConnection(self,db_name=None,transformation_class=None):
        """
        Returns the connection object
        """
        registry = getUtility(IMongoDBConnector)
        vars = self.getSettings()
        if db_name == None:
            db_name = vars['db_name']
            
        connection = Connection(host=vars['host'],port=vars['port'])
        db = connection[db_name]
        if transformation_class != None:
            db.add_son_manipulator(transformation_class())
        return db
 
    def getSettings(self):
        registry = getUtility(IRegistry)
        vars = {'db_name':registry.records.get('vindula.mongodbconnector.interfaces.IMongoDBConnector.db_name').value,
                'host':registry.records.get('vindula.mongodbconnector.interfaces.IMongoDBConnector.host').value,
                'port':registry.records.get('vindula.mongodbconnector.interfaces.IMongoDBConnector.port').value,
                }
        return vars

class MongoDBControlPanel(RegistryEditForm):
    schema = IMongoDBConnector

MongodbControlPanelView = layout.wrap_form(MongoDBControlPanel, ControlPanelFormWrapper)
MongodbControlPanelView.label = u"Vindula: MongoDB settings"