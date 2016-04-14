class CSS_Class(Object):
	def __init__(self, ID, tag, attributes):
		self.ID = ID
		self.attributes = attributes

	def generate_class():
		print(" .{} {").format(ID)
		for item in attributes:
			print("{} {").format(tag)



def generate_CSS(css_stack):

	css_stack.sort(key=lambda x: x[1])

