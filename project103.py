import os
import time
import shutil
import random
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

 
to_dir = "C:/Users/Shinj_28/OneDrive/Desktop/files"
from_dir = "C:/Users/Shinj_28/OneDrive/Desktop/python/Class 103/eventtracker.py"


class FileEventHandler(FileSystemEventHandler):
        def on_created(self, event):
            print(f"Hey, {event.src_path} has been created")
        
        def on_deleted(self, event):
            print(f"Oops ! Someone deleted ,{event.src_path}")
        
        def on_modfied(self, event):
            print(f"Looks like someone modified, {event.src_path}!")
        
        def on_moved(self, event):
            print(f"Looks like someone moved ,{event.src_path}!")
        
event_handler= FileEventHandler()
Observer().schedule(event_handler, from_dir , recursive = True)
Observer().start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped!")
    Observer( ).stop()