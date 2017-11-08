from DistServiceHandler import DistServiceHandler


obj = DistServiceHandler('test1')
# print(obj.get_service_status("ntp"))
print obj.status_services()


