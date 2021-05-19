employees = [
    {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 25000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
print(developers)
#sal=list(filter(lambda salry:salry[]))