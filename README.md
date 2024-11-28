# Gophish Groups Adder

This script allows you to parse a CSV file containing user data and create user groups in Gophish using its API. It is particularly useful for vishing (voice phishing) operations where an operator needs to send messages to users separately.

### Requirements

    Python 3.x
    requests library (install via pip install requests)

## CSV File Format

The CSV file should contain the following headers:

    name: First name of the user
    surname: Surname of the user
    last_name: Last name of the user
    email: Email address of the user

### Example CSV

```csv
name,surname,last_name,email
John,Doe,Smith,john.doe@example.com
Jane,Doe,Johnson,jane.doe@example.com
```
## Usage

    Set Your API Key: Replace HARDCODE_YOUR_API_KEY_HERE in the script with your actual Gophish API key.

    Run the Script: Use the command line to execute the script with the path to your CSV file and the Gophish API URL.


    python add_groups.py users.csv "https://example.com:3333/api"

    Replace users.csv with the path to your CSV file and https://example.com:3333/api with your Gophish API URL.

## Error Handling

    The script will print error messages if the Gophish URL is invalid or if there are issues with creating groups.
    If a group already exists, it will notify you without attempting to create a duplicate.


## Disclaimer

This script is intended for educational and ethical use only. Ensure you have permission to perform any actions related to vishing or phishing simulations.
