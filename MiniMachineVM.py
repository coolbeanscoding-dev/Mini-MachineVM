class MiniVM:
  def OpenFile(self):
    with open("program.masm", "r") as f:
      self.program = f.read()
    return self.program

  def __init__(self):
    self.stack = [0] * 10
    self.SP = 9
    self.PC = 0
    self.tokenize()
  
  def load(self, Value):
    self.stack[self.SP] = Value
    
  def intload(self,Value):
    self.stack[self.SP] = int(Value)
  
  def remove(self):
    self.stack[self.SP] = 0
    
  def shiftup(self,index):
    index = int(index)
    self.SP += index
    if self.SP >= len(self.stack):
      print("Error: Stack Overflow")
      self.SP = len(self.stack) - 1
  
  def shiftdown(self,index):
    self.SP -= int(index)
    if self.SP < 0:
      self.SP = 0
      print("Error: Stack Underflow")
    
  def add(self):
    if self.SP >= 1:
      a = self.stack[self.SP]
      self.SP -= 1
      b = self.stack[self.SP]
      c = a + b
      self.SP += 1
      self.load(c)
  
  def sub(self):
    if self.SP >= 1:
      a = self.stack[self.SP]
      self.SP -= 1
      b = self.stack[self.SP]
      c = a - b
      self.SP += 1
      self.load(c)
      
  def jump(self, PCJUMP):
    self.PC = int(PCJUMP)
  
  def PRINT(self):
    if 0 <= self.SP < len(self.stack):
      print(self.stack[self.SP])
    else:
      print("Error: Invalid stack pointer")
      
  def tokenize(self):
    NeedsOperand = ["LOAD","INTLOAD","SHIFT+","SHIFT-"]
    self.program = self.OpenFile()
    tokens = self.program.strip().split()
    self.code = []
    index = 0
    while len(tokens) > index:
      if tokens[index] in NeedsOperand:
        self.code.append({"Instruction":tokens[index],"Operand":tokens[index + 1]})
        index += 2
        continue
      elif tokens[index] not in NeedsOperand:
        self.code.append({"Instruction":tokens[index],"Operand":None})
        index += 1
        continue
      else:
        print("your code prob doesn't follow the syntax or you mispelt smth idk lmfaoooo")
        quit()
  
  def run(self):
    self.opcode_tables = {
      "LOAD":self.load,
      "INTLOAD":self.intload,
      "REMOVE":self.remove,
      "ADD":self.add,
      "SUB":self.sub,
      "SHIFT+":self.shiftup,
      "SHIFT-":self.shiftdown,
      "PRINT":self.PRINT,
      "JUMP":self.jump,
    }

    while self.PC < len(self.code):
      codeSnippet = self.code[self.PC]
      instruction = self.opcode_tables[codeSnippet["Instruction"]]
      if codeSnippet["Operand"] is not None:
        if codeSnippet["Instruction"]  == "JUMP":
          instruction(codeSnippet["Operand"])
          continue
        instruction(codeSnippet["Operand"])
      else:
        instruction()
      self.PC += 1