import json
from datetime import datetime
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    i=1
    for i in range(5):
       with open("Source.json", "r") as jsonFile:
          data = json.load(jsonFile)

       data["resultDate"] = datetime.now()
       #dataStr = data+"\n"
       #print(data)
       with open("replaceScript.json", "a") as jsonFile:
          json.dump(data, jsonFile,default=str)

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    
    print(threads)

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

