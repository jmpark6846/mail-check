# mail check 📫
이메일 검증 API  
http://mail-env.iaadg2wdty.ap-northeast-2.elasticbeanstalk.com/

# 사용법

    curl -XGET http://mail-env.iaadg2wdty.ap-northeast-2.elasticbeanstalk.com/checkmail/{ 이메일 입력 }

    # 사용 예시
    # 올바른 이메일
    joonmo@linux:~$ curl -XGET http://mail-env.iaadg2wdty.ap-northeast-2.elasticbeanstalk.com/checkmail/jmpark6846@gmail.com
    {"email":"jmpark6846@gmail.com","valid":true,"status":200,"message":"존재하는 이메일입니다."}
    
    # 존재하지 않는 이메일 계정
    joonmo@linux:~$ curl -XGET http://mail-env.iaadg2wdty.ap-northeast-2.elasticbeanstalk.com/checkmail/jmpaawefaefrk6846@gmail.com
    {"email":"jmpaawefaefrk6846@gmail.com","valid":false,"status":400,"message":"gmail.com의 메일서버(gmail-smtp-in.l.google.com.)에 계정이 존재하지 않습니다."}
    
    
## 개발/배포 환경
- Python 3.6.6
- Django 2.1.3
- MySQL 5.6.40(AWS RDS)
- Ubuntu 18.04
- jQuery 3.3.1
- Bootstrap 4.1.3
- AWS Elastic Beanstalk