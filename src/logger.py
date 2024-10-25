import logging 
import os # İşletim sistemi üzerinden bilgileri çekeceğiz.

from  datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #getcwd methodu istenilen dosya yolunu getiri. logs adında klasör açıldı ve LOG_FILE adını klasöre ekler.
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) ## Dosya yolları birleştirilerek bir değişkene atandı.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

if __name__ == "__main__":
    logging.info("Loggin Başladı")
