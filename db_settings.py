# private ec2에 위치한 장고에서 aws rds 접근(private ec2와 rds는 서로 연결되어 있음)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # mysql엔진
        "NAME": "djangodb",  # 데이터베이스 이름
        "USER": "admin",  # 사용자
        "PASSWORD": "Pa55w.rd1234",  # 비밀번호
        "HOST": "db-1.cyf8tnql7evk.us-east-2.rds.amazonaws.com",  # 호스트(aws rds주소)
        "PORT": "3306",  # 포트번호
    }
}
SECRET_KEY = "django-insecure-)k$=#vl2dlq8vw9+sc8-+x06bsc985^yx1uuf)q6am98k*@y@i"


# 로컬에서 aws rds접근(ssh tunneling)
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",  # mysql엔진
#         "NAME": "djangodb",  # 데이터베이스 이름
#         "USER": "admin",  # 사용자
#         "PASSWORD": "Pa55w.rd1234",  # 비밀번호
#         "HOST": "localhost",  # 호스트
#         "PORT": "4406",  # 포트번호
#     }
# }
# SECRET_KEY = "django-insecure-)k$=#vl2dlq8vw9+sc8-+x06bsc985^yx1uuf)q6am98k*@y@i"