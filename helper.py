import transcrib
import rag

def give_answer(url,query):
    txt_file_path = transcrib.transcribe(url)
    rag.save_faiss(txt_file_path)
    ans = rag.get_faiss_ans(txt_file_path,query)
    return ans
    