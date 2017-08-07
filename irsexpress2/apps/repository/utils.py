# -*- coding: utf-8 -*-

import io
from collections import defaultdict

from pdfminer.converter import TextConverter
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTChar, LAParams, LTTextBox, LTTextLine


def get_num_from_elem(e):
    return int(e.text.replace('$', '').replace(',', ''))


def parse_pdf(file_data: 'either string or stream', cell_min_margin=12) -> str:
    """ Convert PDF file to CSV(TSV)-like string """

    class CsvConverter(TextConverter):
        def __init__(self, *args, **kwargs):
            TextConverter.__init__(self, *args, **kwargs)

        def end_page(self, i):
            lines = defaultdict(lambda: {})
            for child in self.cur_item._objs:
                if isinstance(child, LTChar):
                    (_, _, x, y) = child.bbox
                    line = lines[int(-y)]
                    line[x] = child._text

            for y in sorted(lines.keys()):
                line = lines[y]
                stline = ""
                prevx = 0
                for x in sorted(line.keys()):
                    if prevx > 0 and x > prevx + cell_min_margin:
                        stline += '\t'
                    stline += line[x]
                    prevx = x
                self.outfp.write(stline)
                self.outfp.write("\n")

    rsrc = PDFResourceManager()
    outfp = io.StringIO()
    device = CsvConverter(rsrc, outfp, laparams=LAParams())

    if hasattr(file_data, 'read'):
        fp = file_data  # stream
    else:
        # suppose it is a string and convert to stream
        fp = io.StringIO(file_data)
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')

    interpreter = PDFPageInterpreter(rsrc, device)

    for page in doc.get_pages():
        if page is not None:
            interpreter.process_page(page)

    device.close()
    if hasattr(fp, 'close'):
        fp.close()

    return outfp.getvalue()
