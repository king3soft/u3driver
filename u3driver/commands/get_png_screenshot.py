from u3driver.commands.base_command import BaseCommand
import time
import base64
import numpy as np
import cv2.cv2 as cv2
class GetPNGScreenshot(BaseCommand):

    def __init__(self, socket,request_separator,request_end,path = None):
        super().__init__(socket,request_separator,request_end)
        self.path=path
    
    def execute(self):
            response=self.send_data(self.create_command('getPNGScreenshot'))
            screenshot_data=""
            if(response=="Ok"):
                screenshot_data=self.recvall(print_output=False)
                print("[INFO] Get Screenshot png")
                screenshot_data_bytes=base64.b64decode(screenshot_data)
                if self.path != None:
                    f =open(self.path,'wb')
                    f.write(screenshot_data_bytes)
                    f.close()
                readin_mode = cv2.IMREAD_GRAYSCALE if False else cv2.IMREAD_COLOR
                img = np.asarray(bytearray(screenshot_data_bytes), dtype="uint8")
                img = cv2.imdecode(img, readin_mode)
                return img
