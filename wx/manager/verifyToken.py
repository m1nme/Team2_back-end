import jwt
from jwt import exceptions
from wx.secrets import salt_jwt

def verifyToken(token):
    result = None
    msg = None
    try:
        result = jwt.decode(token, salt_jwt, True)
        return True
    except exceptions.ExpiredSignatureError:
        msg = "token失效"
        return msg
    except exceptions.DecodeError:
        msg = "token认证失败"
        return msg
    except exceptions.InvalidTokenError:
        msg = "非法token"
        return msg