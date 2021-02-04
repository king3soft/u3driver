from u3driver.commands.base_command import BaseCommand

class StartRecord(BaseCommand):
    def __init__(self, socket, request_separator, request_end, device,start):
        super(StartRecord, self).__init__(socket, request_separator, request_end)
        self.device = device
        self.start = start

    def execute(self):
        cmd = self.create_command('startRecord', self.device, self.start)
        data = self.send_data(cmd)
        return data