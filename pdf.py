import sys
import os

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

inputs = sys.argv[1:]
assert inputs
outfn = os.path.basename(inputs[0])

writer = PdfWriter()
for inpfn in inputs:
    writer.addpages(PdfReader(inpfn).pages)

writer.trailer.Info = IndirectPdfDict(
    Title="SHAFIQ'S RESUME",
    Author='Md Shafiqul Islam',
    Subject='System Analyst - DevOps',
    Creator='self',
)
writer.write(outfn)