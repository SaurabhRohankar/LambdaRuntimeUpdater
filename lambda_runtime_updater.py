import boto3
import sys

# Initialize the AWS Lambda client
lambda_client = boto3.client('lambda')

# Function to retrieve Lambda functions based on app name
def get_lambda_functions_with_app_name(app_name):
    functions_with_layers = []
    functions_without_layers = []
    
    #add your runtimes that you want to upgrade here
    runtimes = ['python3.7', 'python3.8']
    
    next_marker = None
    while True:
        list_functions_params = {
            "FunctionVersion": "ALL"
        }
        if next_marker:
            list_functions_params["Marker"] = next_marker

        # Call the list_functions method to get a list of Lambda functions
        response = lambda_client.list_functions(**list_functions_params)
        
        for function in response['Functions']:
            if (app_name in function['FunctionName']) and (function['Runtime'] in runtimes):
                layers = [layer_arn.split(':')[-1] for layer_arn in function.get('Layers', [])]
                if layers:
                    functions_with_layers.append((function['FunctionName'], layers))
                else:
                    functions_without_layers.append(function['FunctionName'])

        if 'NextMarker' in response:
            next_marker = response['NextMarker']
        else:
            break

    return functions_with_layers, functions_without_layers

# Function to upgrade a Lambda function's runtime
def upgrade_lambda_function(runtime, function_name):
    try:
        # Call the update_function_configuration method to upgrade the runtime
        response = lambda_client.update_function_configuration(
            FunctionName=function_name,
            Runtime=runtime
        )
        print(f"Function {function_name} upgraded to {runtime}")
    except Exception as e:
        print(f"Error upgrading function {function_name}: {str(e)}")

if __name__ == "__main__":
    app_name = input("Enter the application name: ")
    functions_with_layers, functions_without_layers = get_lambda_functions_with_app_name(app_name)

    print("\nFunctions using layers:")
    for index, (function, layer_names) in enumerate(functions_with_layers, start=1):
        print(f"{index}. Function: {function}, Layers: {', '.join(layer_names)}")

    print("\nFunctions without layers:")
    for index, function in enumerate(functions_without_layers, start=1):
        print(f"{index}. {function}")

    print("\nOptions:")
    print("1. Upgrade all functions")
    print("2. Upgrade functions with layers")
    print("3. Upgrade functions without layers")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == 'q':
        sys.exit()

    upgrade_runtime = 'python3.9'

    if choice == '1':
        functions_to_upgrade = functions_with_layers + functions_without_layers
    elif choice == '2':
        functions_to_upgrade = functions_with_layers
    elif choice == '3':
        functions_to_upgrade = functions_without_layers

    # Loop through the selected functions and upgrade their runtime
    for function_name in functions_to_upgrade:
        upgrade_lambda_function(upgrade_runtime, function_name)

