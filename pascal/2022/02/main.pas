program main;
uses 
	util, strutils, sysutils, types;
const
	debug = false;

	sampleFile = 'sample.txt';
	inputFile = 'input.txt';	

var
	fp: string;
	f: text;
	
	function getScore(a, b: string): integer;
	var 
		c: string;
	begin
		if b = 'X' then c := 'A'
		else if b = 'Y' then c := 'B'
		else if b = 'Z' then c := 'C';
		if a = c then getScore := 3
		else if (((CompareStr(a, 'A') = 0) and (CompareStr(c, 'C') = 0))
			or ((CompareStr(a, 'B') = 0) and (CompareStr(c, 'A') = 0))
			or ((CompareStr(a, 'C') = 0) and (CompareStr(c, 'B') = 0)))
				then getScore := 0
		else getScore := 6;
	end;

	function getValue(a, b: string): integer;
	begin
		if a = 'A' then begin
			if b = 'X' then getValue := 3
			else if b = 'Y' then getValue := 1
			else if b = 'Z' then getValue := 2;
		end else if a = 'B' then begin
			if b = 'X' then getValue := 1
			else if b = 'Y' then getValue := 2
			else if b = 'Z' then getValue := 3;
		end else if a = 'C' then begin
			if b = 'X' then getValue := 2
			else if b = 'Y' then getValue := 3
			else if b = 'Z' then getValue := 1;
		end;
	end;

	procedure part1;
	var 
		A: array of string;
		i: integer;	
		aa: string;
		as: TStringDynArray;
	begin		
		A := util.readInput(f);
		i := 0;
		for aa in A do begin
			as := SplitString(aa, ' ');
			i += getScore(as[0], as[1]);
			if as[1] = 'X' then i+=1
			else if as[1] = 'Y' then i+=2
			else if as[1] = 'Z' then i+=3;	
		end;
		WriteLn('Part 1: ',i);
	end;

	procedure part2;
	var 
		A: array of string;
		i: integer;	
		aa: string;
		as: TStringDynArray;
	begin		
		A := util.readInput(f);
		i := 0;
		for aa in A do begin
			as := SplitString(aa, ' ');
			if as[1] = 'X' then i += 0
			else if as[1] = 'Y' then i+= 3
			else if as[1] = 'Z' then i+= 6;
			i += getValue(as[0], as[1]);
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
