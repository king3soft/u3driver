from u3driver.commands.base_command import BaseCommand
import json

class UploadFinish(BaseCommand):
    def __init__(self, socket, request_separator, request_end):
        super(UploadFinish, self).__init__(socket, request_separator, request_end)

    def execute(self):
        cmd = self.create_command('uploadFinish')
        print(f'Will Send {cmd}')
        data = self.send_data(cmd)
        res = json.loads(data)
        return res['finish'] == 1