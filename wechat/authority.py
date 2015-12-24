import hashlib, json, urllib
from ConfigParser import SafeConfigParser

WECHAT_CONF_FILE = '/etc/wechat.conf'

def get_server_token():
    parser = SafeConfigParser()
    parser.read(WECHAT_CONF_FILE)
    return parser.get('Server', 'Token')

def get_access_token():
    parser = SafeConfigParser()
    parser.read(WECHAT_CONF_FILE)
    appid = parser.get('DevID', 'AppID')
    secret = parser.get('DevID', 'AppSecret')
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid, secret)
    data = json.load(urllib.urlopen(url))
    return data['access_token']

def validate(signature, timestamp, nonce):
    token = get_server_token()
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = '%s%s%s' % tuple(tmpList)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    return tmpstr == signature
