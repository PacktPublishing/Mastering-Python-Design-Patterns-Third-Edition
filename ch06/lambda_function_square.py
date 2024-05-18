def lambda_handler(event, context):
    number = event["number"]
    squared = number * number
    return f"The square of {number} is {squared}."
