from u3driver.commands.base_command import BaseCommand

class MoveTo(BaseCommand):
    def __init__(self, socket, request_separator, request_end, x, y):
        super(MoveTo, self).__init__(socket, request_separator, request_end)
        self.x = x
        self.y = y

    def execute(self):
        cmd = self.create_command('moveTo', self.x, self.y)
        print(f'Will Send {cmd}')
        data = self.send_data(cmd)
        if (data == 'Ok'):
            return True
        return False