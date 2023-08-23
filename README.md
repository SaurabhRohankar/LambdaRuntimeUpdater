# Lambda Runtime Upgrader

![GitHub](https://img.shields.io/github/license/SaurabhRohankar/LambdaRuntimeUpdater)

## Overview

Lambda Runtime Upgrader is a Python script designed to automate the process of upgrading deprecated AWS Lambda runtimes to a more modern version. This script allows you to identify Lambda functions with deprecated runtimes, categorize them based on usage of layers, and offers the option to upgrade them to a specified runtime.

## Features

- Query AWS Lambda to find functions with deprecated runtimes and categorized usage of layers.
- Option to upgrade all functions, functions with layers, or functions without layers to a modern runtime.
- User-friendly menu interface for interaction.

## Requirements

- Python 3.7 or later
- AWS credentials with sufficient permissions

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/lambda-runtime-upgrader.git
   cd lambda-runtime-upgrader

## Install the Required Packages

```bash
pip install boto3
```

## Run the Script

```bash
python lambda_runtime_upgrader.py
```
Follow the prompts to enter the application name, choose an upgrade option, and perform the runtime upgrade.

## Note
Make sure to configure your AWS credentials either through environment variables or AWS CLI configuration before running the script.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
