from u3driver.commands.base_command import BaseCommand

class UBox(BaseCommand):
    def __init__(self, socket, request_separator, request_end, openProfiler):
        super(UBox, self).__init__(socket, request_separator, request_end)
        self.openProfiler = openProfiler

    def execute(self):
        cmd = self.create_command('ubox', self.openProfiler)
        print(f'Will Send {cmd}')
        data = self.send_data(cmd)
        if (data == 'Ok'):
            return True
        return False