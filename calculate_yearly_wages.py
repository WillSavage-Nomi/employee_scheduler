
import scheduler_pb2
import json
from google.protobuf.json_format import MessageToDict

f = open("schedules.json")
data = json.load(f)


shift_message = scheduler_pb2.Shift()
shift_message.day_of_the_week = data["schedule_list"][0]["day_of_the_week"]
shift_message.start_hour = data["schedule_list"][0]["start_hour"] # this gives back EIGHT I want 8
shift_message.end_hour = data["schedule_list"][0]["end_hour"] # this gives back FIVE I want 5


employee_message = scheduler_pb2.Employee()
employee_message.employee_id = data["schedule_list"][0]["employee_id"]
employee_message.base_pay = data["schedule_list"][0]["base_pay"]
employee_message.shift_list.add(shift_name = data["schedule_list"][0]["shift_list"]) # used for repeated items
employee_message.weekend_bonus = data["schedule_list"][0]["weekend_bonus"]
employee_message.night_bonus = data["schedule_list"][0]["night_bonus"]


shift_dict = MessageToDict(shift_message, including_default_value_fields=True)
employee_dict = MessageToDict(employee_message, including_default_value_fields=True)
final_dict = {**shift_dict, **employee_dict}


print(final_dict)