import re
import dns.resolver
import socket
import smtplib


def validate_email(mail):
    result = {}

    if not check_mail_syntax(mail):
        result = {
            'email':mail,
            'valid':False,
            'status':400,
            'message': '올바르지 않은 이메일입니다.'
        }
        return result

    domain_name = mail.split('@')[1]

    try:
        server, mx_record = get_mail_server(domain_name)
    except dns.resolver.NXDOMAIN:
        result = {
            'email': mail,
            'valid': False,
            'status':400,
            'message': '{}이 존재하지 않거나 잘못되었습니다.'.format(domain_name)
        }
        return result


    try:
        server.connect(mx_record)
        host = socket.gethostname()
        server.helo(host)

    except smtplib.SMTPServerDisconnected:

        result = {
            'email': mail,
            'valid': False,
            'status': 500,
            'message': '메일 서버에서 연결을 차단하였습니다.'
        }
        return result

    server.mail('hi@hi.com')

    code, message = server.rcpt(str(mail))


    if code == 250:
        result = {
            'email': mail,
            'valid': True,
            'status':200,
            'message': '존재하는 이메일입니다.'
        }
    else:
        result = {
            'email': mail,
            'valid': False,
            'status': 400,
            'message': '{}의 메일서버({})에 계정이 존재하지 않습니다.'.format(domain_name, mx_record)
        }

    server.quit()
    return result


def check_mail_syntax(mail):
    match = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', mail)
    return False if match == None else True


def get_mail_server(domain_name):
    records = dns.resolver.query(domain_name, 'MX')

    mx_record = records[0].exchange
    mx_record = str(mx_record)

    server = smtplib.SMTP()
    server.set_debuglevel(0)
    return (server, mx_record)
