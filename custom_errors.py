class BaseError:
	def __init__(self, message, value):
		self.message = message
		self.value = value
	
	def __str__(self):
		return f"\n\nThe input: '{self.value}'\n{self.message}"

class MenuOutOfRange(BaseError, Exception):
	def __init__(self, value, message="The specified input is not in the (1, 9) range in the main menu..."):
		super().__init__(message, value)
	
class MenuNotInteger(BaseError, Exception):
	def __init__(self, value, message="The specified input is not a number in the (1, 9) range in the main menu"):
		super().__init__(message, value)