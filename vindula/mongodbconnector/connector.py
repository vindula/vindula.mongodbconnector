from five import grok
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.z3cform import layout
from interfaces import IMongoDBConnector
from zope.component import getUtility
import pymongo

class MongoDBConnector(grok.GlobalUtility):
    """
    """
    grok.provides(IMongoDBConnector)

    @property
    def db_connection(self):
        db = 'db connection'
        return getUtility(IMongoDBConnector, db)
 

class MongoDBControlPanel(RegistryEditForm):
    schema = IMongoDBConnector

MongodbControlPanelView = layout.wrap_form(MongoDBControlPanel, ControlPanelFormWrapper)
MongodbControlPanelView.label = u"Vindula: MongoDB settings"