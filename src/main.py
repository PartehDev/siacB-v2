import os
output = ""
class Parsing:
  def __init__(self):
    self.code = ""
    self.parsed = False
  def parse(code, self):
    line = 1
    self.code = code
    for line in code:
        if line == 1:
            if line != "WAKEY WAKEY": raise TypeError("Missing \"WAKEY WAKEY\" in the current file on line 1. Please put this line on line 1 and recompile. ")
            else:
                line += 1
        else:
            if line == "sicab::test":
                output += "Hello, world! "
            elif line == "sicab::lennyshrug":
                output += "¯\_(ツ)_/¯ "
            elif line == "BEDTIME":
                output += "EOF"
            elif line == "sicab::arnoldc":
                output += "IT'S SHOWTIME! "
            elif line == "sicab::changelog":
                output += "COMING SOON: MORE COMMANDS AND PARAMETERS!"
    if "EOF" not in output:
        raise TypeError("bruh, no \"BEDTIME\" in file, how can you mess that up?")
    run(output)
  def run(inn):
      inn_clean = inn.split("EOF")
      new_inn = inn.split(" ")
      print(new_inn)
fileName = input("Input the filename (leave out \".sb\", and make sure it's in the directory siacB is in.")
print(f"Searching for file {fileName}.sb in current directory.")
if os.path.exists(f"./{fileName}.sb") and os.path.isFile(f"./{fileName}.sb"):
  code = open(f"{fileName}.sb", "r").readlines()
  Parsing.parse(code)
