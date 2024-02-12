def evaluate_deployments(deployments):
    result = {
        "Success": 0,
        "Fail": 0,
        "Error": 0
    }
    for deployment in deployments:
        status = deployment.split('"status": "')[1].split('"')[0]
        if status == "Error" or status not in result.keys():
            result["Error"] += 1
        else:
            result[status] += 1

    toReturn = [result["Success"], result["Fail"], result["Error"]]
    return toReturn

deployments = ['{"deployment_id": "d-12345678ab", "status": "Success"}', '{"deployment_id": "d-09876543cd", "status": "Fail"}','{"deployment_id": "d-12345678ab", "status": "asdas"}','{"deployment_id": "d-12345678ab", "status": "Error"}']

print(evaluate_deployments(deployments))