class CSS_Class(Object):
	def __init__(self, css_statement):
		self.ID = css_statement[1]
		self.tag = css_statement[2]
		self.attributes = css_statement[3,len(css_statement)]

	def generate_css_class():
		print(" .{} {").format(ID)
		for item in attributes:
			print("{} {").format(tag)



def generate_CSS(css_stack):

	css_stack.sort(key=lambda x: x[1])

