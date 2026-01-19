READ USING CODE
A simple learning project I made over the weekend meant for me to learn python classes better and CS.
The language I implemented is going to be called MiniAssembly
Write your code in the program.masm file (Keep the name the same).

MiniAssembly syntax rules:
  -Higher Stack Pointer = Higher on the stack
  -Each instruction is 1 line so put your instructions on different lines
  -Manage the stack pointer well
  -Adding takes what your stack pointer is on and adds it with what is lower on the stack
  -Subtraction does the same thing except it subtracts
  -Opcodes must be all caps
  
MiniAssembly OpCodes:
  -LOAD InsertValue (Inserts a value onto the stack where the pointer is)
  -INTLOAD InsertValue (Does what load does except the type is int)
  -REMOVE (Removes what your stack pointer is on)
  -SHIFTUP InsertValue (Shifts pointer up a specified amount)
  -SHIFTDOWN InsertValue (Shifts pointer down a specified value)
  -ADD (Adds the values of what the pointer is on and what is below an index above it and replaces what the pointer is on with the sum)
  -SUB (Does the same as ADD except it subtracts what your pointer is on by what the index below is)
  -JUMP (Jumps to a certain line on your program and it starts from 0)
  -PRINT (Prints the value of what the pointer is on)
