import scheduler_pb2
import json
from google.protobuf.json_format import MessageToDict

f = open("schedules.json")
data = json.load(f)


shift_message = scheduler_pb2.Shift()
shift_message.day_of_the_week = data["schedule_list"][0]["day_of_the_week"]
shift_message.start_hour = data["schedule_list"][0]["start_hour"] # this gives back EIGHT I want 8
shift_message.end_hour = data["schedule_list"][0]["end_hour"] # this gives back FIVE I want 5
shift_message.employee.employee_id = data["schedule_list"][0]["employee_id"]
shift_message.employee.base_pay = data["schedule_list"][0]["base_pay"]
shift_message.employee.shift_list.add(shift_name = data["schedule_list"][0]["shift_list"]) # used for repeated items
shift_message.employee.weekend_bonus = data["schedule_list"][0]["weekend_bonus"]
shift_message.employee.night_bonus = data["schedule_list"][0]["night_bonus"]


dict_object = MessageToDict(shift_message)


print(dict_object)
