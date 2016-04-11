
outpath = "source.txt"
inpath = raw_input("Enter izitag source file path:  ")

with open(inpath, 'r') as content_file:
	content = content_file.read()
	content_file.close()

with open(outpath, 'w+') as source_write:
	source_write.write(content)
	source_write.close() 