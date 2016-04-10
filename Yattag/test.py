from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
	with tag('h1'):
		text("This is a header!\n")
		text("This is also a header!")

print(doc.getvalue())