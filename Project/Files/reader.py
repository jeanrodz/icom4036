
outpath = "/source.txt"
inpath = raw_input("Enter izitag source file path")

if(inpath.endswith('.izi') == False: 
	raise Exception('Target file is not a valid iziTag file')
else:
	with open(path, 'r') as content_file:
	    content = content_file.read()

	with open(outpath, 'w') as source_write
			source_write = content 