def activation_sms_message_format(name, code):
    text_message = f"""
    Hello {name},
    Thanks for Subscribing Lookout MES.
    Please download  & activate the application from the link below:
    https://get.lookout.com/web-code?code={code}

    Thanks,
    Team Haigreve
    """
    return text_message


def renewal_sms_message_format(name, url):
    text_message = f"""
    Hello {name},
    Your Lookout MES subscription is expiring on DD/MM/YY.
    To resubscribe please visit {url} .

    Thanks,
    Team Haigreve
    """
