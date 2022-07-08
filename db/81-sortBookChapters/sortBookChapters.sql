CREATE PROCEDURE solution()
BEGIN
	SELECT chapter_name FROM
    (SELECT chapter_name, chapter_number, 
	i+5*v+10*x+50*l+100*c+500*d+1000*m-2*iv-2*ix-20*xl-20*xc-200*cd-200*cm AS val FROM
	(SELECT chapter_name, chapter_number, 
    LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "I", "")) as i,
    LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "V", "")) as v,
    LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "X", "")) as x,
    LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "L", "")) as l,
    LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "C", "")) as c,
    LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "D", "")) as d,
    LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "M", "")) as m,
    (LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "IV", "")))/2 as iv,
    (LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "IX", "")))/2 as ix,
    (LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "XL", "")))/2 as xl,
    (LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "XC", "")))/2 as xc,
    (LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "CD", "")))/2 as cd,
    (LENGTH(chapter_number) - LENGTH(REPLACE(chapter_number, "CM", "")))/2 as cm
    FROM book_chapters) mysq) mysq2 ORDER BY val;
END