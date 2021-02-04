from u3driver.commands.base_command import BaseCommand
import json

class JX(BaseCommand):
    def __init__(self, socket, request_separator, request_end, args):
        super(JX, self).__init__(socket, request_separator, request_end)
        self.args = args

    def execute(self):
        cmd = self.create_command('jx', self.args)
        # cmd = 'jx;'+self.args+';&'
        print(f'Will Send {cmd}')
        data = self.send_data(cmd)
        # if (data == 'Ok'):
        #     return True
        # return False
        if self.args == 'mem_unity' or self.args == 'mem_lua':
            res = json.loads(data)
            return res
        else:
            return self.parse_data(data)

    def parse_data(self, data):
        if "404" in data:
            return False
        res = json.loads(data)
        if "code" in res.keys():
            if res["code"] == 200:
                return True
        elif "itemCount" in res.keys():
            return res["itemCount"]