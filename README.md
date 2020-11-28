# MailJet SMS Application
Using MailJet SMS API, sends SMS's to a list of contacts stored in a CSV file.

This application requires the requests library. To install open the terminal and type:

pip install requests

It also requires a MailJet SMS wallet and bearer token, which must be entered into the application at runtime.

Application takes a CSV comma delimited file with client name, state, mobile number and text message to send. This file 
should not include a header row or any trailing newline. The application does not allow any commas within the message to
be sent. The mobile number must start with the country code in the style of "+614xxxxxxxx" for Australian mobile phone 
numbers.

A file called log.csv will be created when SMS messages are sent. This file includes all entries that failed to be sent 
with the API.

This Application has not been thoroughly tested, but it works according to the response messages from API and MailJet 
site log.
