from twilio.rest import TwilioRestClient

account_sid = "ACce3943433f336ea8ad182aa419779890" # Your Account SID from www.twilio.com/console
auth_token  = "096e010017f8aab81a358a0cf91da1fc"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hey! I am Sundar Pichai,CEO of Google.I saw your activity of SOK. I am touched by the motive of your task.We would like to have you as an intern.Keep coding !!",
    to="+917997078740",    # Replace with your phone number
    from_="+12405585927 ") # Replace with your Twilio number

print(message.sid)

