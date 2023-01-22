SILCAWL Parser
==============

Tested on the SILCAWL PDF from [here](https://www.sil.org/resources/archives/7882).

1. Use `pdftotext` form poppler to convert the PDF to a TXT file.
2. Delete the index and abstract from the TXT file.
3. Use a regex find replace with the pattern `\s+\d+` to remove line numbers.
4. Add a `.` after the `2` for `MAN'S NONPHYSICAL BEING`.
5. Add spaces after ID numbers for category 1.1.2.
5. Run the program on the TXT file.
