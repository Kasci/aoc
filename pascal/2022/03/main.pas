program main;
uses 
	util;

const
	debug = false;

	sampleFile = 'sample.txt';
	inputFile = 'input.txt';	

var
	fp: string;
	f: text;
	
	function eval(c: char): integer;
	begin
		if (ord(c) >= ord('a')) and (ord(c) <= ord('z')) then
			eval := ord(c) - ord('a') + 1
		else eval := ord(c) - ord('A') + 27;
	end;
	
	procedure part1;
	var 
		A: array of string;
		i, l, n: integer;	
		aa, q, w: string;
	begin		
		A := util.readInput(f);
		i := 0;
		for aa in A do
		begin
			l := round(length(aa)/2);
			q := copy(aa, 0, l);
			w := copy(aa, l+1, l); 
			for n := 1 to l+1 do
			begin
				if pos(q[n], w) > 0 then
				begin
					i := i + eval(q[n]);
					break;
				end;
			end;
		end;
		WriteLn('Part 1: ',i);
	end;

	procedure part2;
	var 
		A: array of string;
		i, j, l, n: integer;	
		q: string;
	begin		
		A := util.readInput(f);
		i := 0;
		for j := 0 to (length(A) div 3)-1 do begin
			q := A[3*j];
			l := round(length(q));
			for n := 1 to l+1 do
			begin
				if (pos(q[n], A[3*j+1]) > 0) and (pos(q[n], A[3*j+2]) > 0) then
				begin
					i := i + eval(q[n]);
					break;
				end;
			end;
		end;
		WriteLn('Part 2: ',i);
	end;
begin
	if debug then
		fp := sampleFile
	else
		fp := inputFile;	
	assign(f, fp);

	part1;
	part2;

end.
