from u3driver.commands.base_command import BaseCommand
import json

class TalkTo(BaseCommand):
    def __init__(self, socket, request_separator, request_end,id):
        super(TalkTo, self).__init__(socket, request_separator, request_end)
        self.id = id

    def execute(self):
        cmd = self.create_command('talkTo',self.id)
        print(f'Will Send {cmd}')
        data = self.send_data(cmd)
        return data