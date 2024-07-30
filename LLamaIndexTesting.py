from llmsherpa.readers import LayoutPDFReader
from llama_index.core import Document
from llama_index.core import VectorStoreIndex


llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"
pdf_url = "testbook.pdf" # also allowed is a file path e.g. /home/downloads/xyz.pdf
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)

index = VectorStoreIndex([])
for chunk in doc.chunks():
    index.insert(Document(text=chunk.to_context_text(), extra_info={}))
query_engine = index.as_query_engine()

# Let's run one query
response = query_engine.query("list 10 things I could do in Laramie Wyoming")
print(response)