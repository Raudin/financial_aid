import africastalking

# TODO: Initialize Africa's Talking

username = 'get_your_own'
api_key = '12345'

africastalking.initialize(username, api_key)


class send_sms():
    def sending(number, name, message):
        name = name
        number = str(number)
        # Set the numbers in international format
        recipients = [number]
        # Set your message
        message = message

        try:
            sms = africastalking.SMS
            response = sms.send(message, recipients)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')
