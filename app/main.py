from langchain_docling import DoclingLoader

def main():

    document_path = input("Enter the path to the document: ")

    loader = DoclingLoader(file_path=document_path)

    docs = loader.load()

    ...