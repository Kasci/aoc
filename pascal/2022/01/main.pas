program main;
uses 
	util, sysutils;

type
	m_arr = array [0..2] of longint;

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

	procedure add(v: longint; var max: m_arr);
	begin
(*		writeln('>',v,' ',max[0],' ',max[1],' ',max[2]);*)
		if v > max[0] then begin
			max[2] := max[1];
			max[1] := max[0];
			max[0] := v;
		end else if v > max[1] then begin
			max[2] := max[1];
			max[1] := v;
		end else if v > max[2] then begin
			max[2] := v;
		end;
	end;

	procedure part2;
	var 
		A: array of string;
		i, tmp: longint;	
		max: array [0..2] of longint = (0,0,0);
		aa: string;
	begin		
		A := util.readInput(f);
		i := 0;
		tmp := 0;
		for aa in A do begin
			if aa = '' then begin
				add(tmp, max);
				tmp := 0;
			end else begin
				tmp += StrToInt(aa);
			end
		end;
		add(tmp, max);
		i := max[0]+max[1]+max[2];
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
