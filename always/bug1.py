import os

bug = "IndentationError: unindent does not match any outer indentation level"

def FB(bug):
	if bug == "IndentationError: unindent does not match any outer indentation level":
		with open("Bug1.txt", "a") as file:
			file.write("1.Bug:\n")
			file.write("	IndentationError: unindent does not match any outer indentation level\n")
			file.write("2.Fix\n")
			file.write("	All text editor has the button is {Indentation}: 1 to 8\n")
			file.write("	Press {Convert_Indentation_To_Spaces} or {Convert_Indentation_To_Tabs}")
FB(bug)
