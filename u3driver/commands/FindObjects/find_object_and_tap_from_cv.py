from u3driver.commands.command_returning_alt_elements import CommandReturningAltElements
from u3driver.by import By
import airtest.core.cv as cv
import json
import os
class FindObjectAndTapFromCV(CommandReturningAltElements):
    def __init__(self, socket,request_separator,request_end,appium_driver,path,url):
        super(FindObjectAndTapFromCV, self).__init__(socket,request_separator,request_end,appium_driver)
        self.path = path
        self.url = url
    
    def execute(self):
        png_url = self.url + self.path.replace("//","~") + ".png"
        
        pos,rotation = cv.loop_find_android(cv.Template(png_url),device_s = self.appium_driver)
        #直接使用adb模拟点击
      
        return os.popen(f"adb -s {self.appium_driver} shell input tap {pos[0]} {pos[1]}").read()

        #使用SDK的方法，点击物体并返回节点
        screen = self.send_data(self.create_command('getScreen'))
        screen = json.loads(screen)

        #竖屏游戏的高度和宽度会相反，但手机的尺寸并不会，当前默认是横屏的游戏，之后再处理竖屏
        sub_height = sub_width = 0
        if rotation == 1:
            #adb截图的屏幕大小,还要根据屏幕的旋转来处理，当正向是刘海屏时，减去，否则不减
            phone_screen = os.popen(f"adb -s {self.appium_driver} shell wm size").read()
            phone_screen = phone_screen.split(':')[1]
            phone_height = int(phone_screen.split('x')[0])
            phone_width = int(phone_screen.split('x')[1])
            sub_height = phone_height - int(screen['height'])
            sub_width = phone_width - int(screen['width'])
        #unity以左下角为原点，cv以左上角为原点
        data = self.send_data(self.create_command('tapScreen',pos[0] - sub_width, int(screen['height']) - pos[1] - sub_height))
        return self.get_alt_element(data)