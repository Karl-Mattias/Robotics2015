class GameStatus(object):

	@staticmethod
	def status():
		try:
			command_file = open('referee.command', 'r')
			status = eval(command_file.readline())
			command_file.close()
			last_status = status
			return status
		except EOFError:
			return last_status
