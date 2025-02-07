from langchain_community.llms import GooglePalm
from langchain_text_splitters import CharacterTextSplitter

with open("./data/sample.txt") as f:
    sample_data = f.read()
    print(sample_data)
    text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=200)
    mydata = text_splitter.create_documents([sample_data])
    print(mydata)