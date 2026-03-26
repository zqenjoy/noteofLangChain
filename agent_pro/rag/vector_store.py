import os
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from model.factory import embed_model
from utils.config_handler import chroma_config
from utils.path_tool import get_abs_path
from utils.file_handler import txt_loader,pdf_loader,listdir_with_allowed_type,get_file_md5_hex
from utils.logger_handler import logger



class VextorStoreService:
    def __init__(self):
        self.vector_store = Chroma(
            collection_name = chroma_config["collection_name"],
            embedding_function = embed_model ,  #不可写死，而是写一个工厂factory的文件，模型创建时有聊天模型，嵌入模型等等多类模型，生产模型
            persist_directory = chroma_config["persist_directory"]
        )

        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size = chroma_config["chunk_size"],
            chunk_overlap = chroma_config["chunk_overlap"],
            separators = chroma_config["separators"],
            length_function = len
        )

    # 获取检索器对象
    def get_retriever(self):
        return self.vector_store.as_retriever(
            search_kwargs = {"k": chroma_config["k"]},
        )

    # 从数据文件夹内读取数据文件，转为向量存入向量库 要计算文件的md5去重
    def load_document(self):

        def check_md5_hex(md5_for_check:str):
            if not os.path.exists(get_abs_path(chroma_config["md5_hex_store"])):
                # 如果不存在，则创建这个文件
                open(get_abs_path(chroma_config["md5_hex_store"]),'w',encoding='utf-8').close()
                return False

            with open(get_abs_path(chroma_config["md5_hex_store"]),"r",encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip()
                    if line == md5_for_check:
                        return True #md5处理过了
                return False  # 没处理过

        #保存md5
        def save_md5_hext(md5_for_check:str):
            with open(get_abs_path(chroma_config["md5_hex_store"]),"w",encoding="utf-8") as f:
                f.write(md5_for_check + '\n')

        # 读文件内容
        def get_file_document(read_path:str):
            if read_path.endswith('txt'):
                return txt_loader(read_path)
            if read_path.endswith('pdf'):
                return pdf_loader(read_path)

            return []

        allowed_files_path: list[str] = listdir_with_allowed_type(get_abs_path(chroma_config["data_path"]),tuple(chroma_config["allow_knowledge_file_type"]))

        for path in allowed_files_path:
            # 获取文件的md5
            md5_hex=get_file_md5_hex(path)
            if check_md5_hex(md5_hex):
                logger.info(f'[加载知识库]{path}内容已经存在于知识库,跳过')
                continue

            try:
                documents: list[Document] = get_file_document(path)

                if not documents:
                    logger.warning(f'[加载知识库]{path}内没有有效文本内容,跳过')
                    continue
                split_document:list[Document] =  self.spliter.split_documents(documents)
                if not split_document:
                    logger.warning(f'[加载知识库]{path}分片后没有有效文本内容,跳过')
                    continue

#                将内容存入向量库中
                self.vector_store.add_documents(split_document)
#               # 记录这个已经处理好的文件md5，避免下次重复下载

                logger.info(f"[加载知识库]{path}内容加载成功")
            except Exception as e:
                # exc_info:True会记录详细的报错堆栈，如果为False仅记录报错信息本身
                logger.error(f"[加载知识库]{path}加载失败",exc_info=True)
                continue



if __name__ == '__main__':
    vs = VextorStoreService()
    vs.load_document()
    retriver = vs.get_retriever()
    res = retriver.invoke('迷路')
    print(res)