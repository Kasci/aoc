program main;
uses 
	util;

const
	debug = true;

	sampleFile = 'sample.txt';
	inputFile = 'input.txt';	

var
	fp: string;
	f: text;
	
	procedure part1;
	var 
		A: array of string;
		i: integer;	
		aa: string;
	begin		
		A := util.readInput(f);
		i := 0;
		WriteLn('Part 1: ',i);
	end;

	procedure part2;
	var 
		A: array of string;
		i: integer;	
		aa: string;
	begin		
		A := util.readInput(f);
		i := 0;
		WriteLn('Part 2: ',i);
	end;
begin
	if debug then
		fp := sampleFile
	else
		fp := inputFile;	
	assign(f, fp);

	part1;
	(* part2; *)

end.
