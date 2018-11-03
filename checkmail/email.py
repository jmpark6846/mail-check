import re
import dns.resolver
import socket
import smtplib


def validate_email(mail):
    result = {}

    if not check_mail_syntax(mail):
        result = {
            'valid':False,
            'message': '올바르지 않은 이메일입니다.'
        }
        return result

    domain_name = mail.split('@')[1]

    try:
        server, mx_record = get_mail_server(domain_name)
    except ValueError:
        result = {
            'valid': False,
            'message': '존재하지 않는 메일서버입니다.'
        }
        return result


    try:
        server.connect(mx_record)
        host = socket.gethostname()
        server.helo(host)

    except smtplib.SMTPServerDisconnected:

        result = {
            'valid': False,
            'message': '메일서버와 연결이 종료되었습니다.'
        }
        return result

    server.mail('hi@hi.com')

    code, message = server.rcpt(str(mail))


    if code == 250:
        result = {
            'valid': True,
            'message': '존재하는 이메일입니다.'
        }
    else:
        result = {
            'valid': False,
            'message': '계정이 네임서버에 존재하지 않습니다.'
        }

    server.quit()
    return result


def check_mail_syntax(mail):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
    return False if match == None else True


def get_mail_server(domain_name):
    records = dns.resolver.query(domain_name, 'MX')

    mx_record = records[0].exchange
    mx_record = str(mx_record)

    server = smtplib.SMTP()
    server.set_debuglevel(0)
    return (server, mx_record)
