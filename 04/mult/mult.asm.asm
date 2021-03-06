// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

	@R0
	D=M
	@n
	M=D
	@R1
	D=M
	@add
	M=D
	@n
	D=M
	@ZERO
	D;JEQ
	(LOOP)
	@n
	D=M
	@STOP
	D;JEQ
	@n
	M=M-1
	@add
	D=M
	@sum
	M=M+D
	@LOOP
	0;JMP
	(ZERO)
	@R2
	M=0
	@END
	0;JMP
	(STOP)
	@sum
	D=M
	@R2
	M=D
	@sum
	M=0
	(END)
	@END
	0;JMP
	