unit util;

interface
	type AOS = array of string;
	function readInput(var f: text): AOS;

implementation
	function readInput(var f: text): AOS;
	var
		A: AOS;
		i,n: integer;
		s: string;
	begin
		i := 0;
		n := 0;
		reset(f);
		while not eof(f) do
		begin
			readLn(f,s);
			inc(n);
		end;
		setLength(A, n);
		reset(f);
		while not eof(f) do
		begin
			readLn(f,A[i]);
			inc(i);
		end;
		readInput := A;
	end;
	
end.
