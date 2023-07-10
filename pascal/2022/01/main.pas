program main;
uses 
	util, sysutils;

const
	debug = false;

	sampleFile = 'sample.txt';
	inputFile = 'input.txt';	

var
	fp: string;
	f: text;
	
	procedure part1;
	var 
		A: array of string;
		i, tmp, max: longint;	
		aa: string;
	begin		
		A := util.readInput(f);
		i := 0;
		tmp := 0;
		max := -1;
		for aa in A do begin
			if aa = '' then begin
				if tmp > max then begin
					max := tmp;
				end;
				tmp := 0;
			end else begin
				tmp += StrToInt(aa);
			end
		end;
		if tmp > max then begin
			i := tmp;
		end else begin
			i := max;
		end;
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
