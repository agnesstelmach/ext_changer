import os

directory = raw_input("Paste the full directory path: ")
files = os.listdir(directory)
os.chdir(directory)
for filename in files:
	file_extension = os.path.splitext(filename)[1]
	if file_extension == ".PDF":
		new_file_name = filename.replace(".PDF",".pdf")
		print filename + " => " + new_file_name
		os.rename(filename, new_file_name)