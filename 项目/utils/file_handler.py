import os ,hashlib
from logger_handler import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader,TextLoader


def get_file_md5_hex(filepath:str):# 获取文件的md5的十六进制字符串
    if not os.path.exists(filepath):
        logger.error(f"[md计算]文件{filepath}不存在")

    if not os.path.isfile(filepath):
        logger.error(f"[md计算]文件{filepath}不存在")

    md5_obj = hashlib.md5()
    chunk_size = 1024
    try:

        with open(filepath,'rb') as f:
            while chunk:= f.read(chunk_size):
                md5_obj.update(chunk)
            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f"md计算文件{filepath}失败")
        return None


def listdir_with_allowed_type(path,allow_types:tuple[str]): # 返回文件夹内的文件列表（允许的文件后缀）
    files = []
    if not os.path.isdir(path):
        logger.error(f"[listdir_with_allowed_type]{path}不是文件夹")
        return allow_types

    for f in os.listdir(path):
        if f.endswith(tuple(allow_types)):
            files.append(os.path.join(path,f))
    return tuple(files)  #转成元祖类型就不允许改变了


def  pdf_loader(filepath:str,password=None)->list[Document]:
    return PyPDFLoader(filepath,password).load()

def  txt_loader(filepath:str)->list[Document]:
    return TextLoader(filepath,encodings="utf-8").load()