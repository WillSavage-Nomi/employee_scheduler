from scheduler_pb2 import Shift
from google.protobuf.json_format import ParseDict
import json

with open("schedules.json") as file:
    message_dicts = json.load(file)


for message_dict in message_dicts["schedule_list"]:
    shift_message = ParseDict(message_dict, Shift())
    
    print(shift_message.start_hour)
