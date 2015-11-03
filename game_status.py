class GameStatus(object):
    def __init__(self):
        command_file = open('referee.command','r')
        self.status = eval(command_file.readline())
        command_file.close()

    def status(self):
        return self.status






     