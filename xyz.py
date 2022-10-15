def implementAPI(logs):
    res = []
    users = {}
    curr_user = ""

    for x in logs:
        log = x.split()

        if log[0] == "register":
            if log[1] not in users:
                users[log[1]] = log[2]
                res.append("Registered Successfully")
            else:
                res.append("Username already exists")
        elif log[0] == "login":
            if curr_user == "":
                if log[1] in users and log[2] == users[log[1]]:
                    curr_user = log[1]
                    res.append("Logged In Successfully")
                else:
                    res.append("Login Unsuccessful")
            else:
                res.append("Login Unsuccessful")
        else:
            if curr_user == log[1]:
                curr_user = ""
                res.append("Logged Out Successfully")
            else:
                res.append("Logout Unsuccessful")
    return res
