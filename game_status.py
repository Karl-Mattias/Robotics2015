class GameStatus(object):

	@staticmethod
	def status():
		last_status = False
		try:
			command_file = open('referee.command', 'r')
			status = eval(command_file.readline())
			command_file.close()
			last_status = status
			return status
		except SyntaxError:  # when file is empty during writing
			return last_status
