def login():
    return dict()

def store():
    submitted_name = request.vars.name
    submitted_password = request.vars.password

    results = db.users.insert(
        db_name = submitted_name,
        db_password = submitted_password
    )

    if results:
        return "Successful"
    else:
        return "An Error Occured"