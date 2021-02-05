import json
from u3driver.commands.ObjectCommands.get_text import GetText
from u3driver.commands.ObjectCommands.set_text import SetText
from u3driver.commands.ObjectCommands.tap import Tap
from u3driver.commands.ObjectCommands.drag import Drag

class AltElement(object):
    def __init__(self, alt_unity_driver, appium_driver, json_data):
        self.alt_unity_driver = alt_unity_driver
        self.appium_driver=None
        if (appium_driver != None):
            self.appium_driver = appium_driver
        data = json.loads(json_data)
        self.name = str(data['name'])
        self.id = str(data['id'])

    def toJSON(self):
        dict = {
            'name': self.name,
            'id' : self.id
        }
        return json.dumps(dict)

    def get_text(self):
        alt_object = self.toJSON()
        return GetText(self.alt_unity_driver.socket,self.alt_unity_driver.request_separator,self.alt_unity_driver.request_end,alt_object).execute()
    
    def set_text(self, text):
        alt_object = self.toJSON()
        data = SetText(self.alt_unity_driver.socket,self.alt_unity_driver.request_separator,self.alt_unity_driver.request_end,text,alt_object).execute()
        return AltElement(self.alt_unity_driver, self.appium_driver, data)
        
    
    def drag(self, x1, y1,x2 = None,y2 = None):
        data = Drag(self.alt_unity_driver.socket,self.alt_unity_driver.request_separator,self.alt_unity_driver.request_end,self.name,x1,y1,x2,y2).execute()
        return data

    def tap(self):
        alt_object=self.toJSON()
        data= Tap(self.alt_unity_driver.socket,self.alt_unity_driver.request_separator,self.alt_unity_driver.request_end,alt_object).execute()
        return AltElement(self.alt_unity_driver,self.appium_driver,data)
