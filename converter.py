import json

with open("status.json", "r") as myfile:
    myjson = json.load(myfile)
    downed_servers = [] 
    for serv in myjson:
        print(serv)
        if serv["state"] == "down":
            print("this one is down")
            downed_servers.append(serv["server"])

print(f"the following is a list of all the servers in a down state: {downed_servers}")

with open("downed_servers.txt", "w") as f2:
    spaced_servers = [f"{srv}\n" for srv in downed_servers]
    f2.writelines(downed_servers)

