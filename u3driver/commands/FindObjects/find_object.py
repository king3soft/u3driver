from u3driver.commands.command_returning_alt_elements import CommandReturningAltElements
from u3driver.by import By
import airtest.core.cv as cv
import json
import os

class FindObject(CommandReturningAltElements):
    def __init__(self, socket,request_separator,request_end,appium_driver,by,value,image_url = None):
        super(FindObject, self).__init__(socket,request_separator,request_end,appium_driver)
        self.by=by
        self.value=value
        self.image_url = image_url
    
    def execute(self):
        path=self.set_path(self.by,self.value)
        if self.by == By.PATH:
            data = self.send_data(self.create_command('findObject', path))
        elif self.by == By.LEVEL:
            data = self.send_data(self.create_command('findObjectByLevel', path))
        #通过图像识别，只能得出位置，而无法得出文本和设置文本
        #所以只能根据位置得出按钮物体，而无法做出更复杂的操作
        #这对于节点变化时，可以使用图像识别的方法找到按钮，其他物体就无法找到了
        #而且找到的位置是最佳位置，不会返回其他符合的位置，即使图像上有多个相同的图像
        if "error:notFound" in data and self.image_url != None:
            png_url = self.image_url + path.replace("//","~") + ".png"
            pos,rotation = cv.loop_find_android(cv.Template(png_url),device_s = self.appium_driver)
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
            data = self.send_data(self.create_command('findObjectByPoint',pos[0] - sub_width, int(screen['height']) - pos[1] - sub_height))
            return self.get_alt_element(data)

        return self.get_alt_element(data)