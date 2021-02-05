from u3driver.commands.command_returning_alt_elements import CommandReturningAltElements
from u3driver.by import By
import json
import os

class FindObject(CommandReturningAltElements):
    def __init__(self, socket,request_separator,request_end,appium_driver,by,value,image_url = None,needActive=True):
        super(FindObject, self).__init__(socket,request_separator,request_end,appium_driver)
        self.by=by
        self.value=value
        self.image_url = image_url
        self.needActive = "0"
        if needActive:
            self.needActive = "1"
    
    def execute(self):
        print(self.value)
        path=self.set_path(self.by,self.value)
        if self.by == By.PATH:
            data = self.send_data(self.create_command('findObject', path, self.needActive))
        elif self.by == By.LEVEL:
            data = self.send_data(self.create_command('findObjectByLevel', path))

        return self.get_alt_element(data)