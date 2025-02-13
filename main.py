import logging, requests, json, sys
from config import headers

# 会话保持
session = requests.session()
# 设置header
session.headers.update(headers)

# 日志模块
# 创建一个logger
logger = logging.getLogger("ssr")
# 设置日志级别（可选）
logger.setLevel(logging.INFO)
# 创建一个handler，将日志发送到stdout
stdout_handler = logging.StreamHandler(sys.stdout)
# 创建一个formatter，定义日志输出格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# 将formatter添加到handler
stdout_handler.setFormatter(formatter)
# 将handler添加到logger
logger.addHandler(stdout_handler)

# 登录
def login():
  logger.info('开始登录')
  try:
    url = 'https://api.acck.io/api/v1/user/login'  # 更新登录URL
    data = {"email": "qimo84bep15900@163.com", "passwd": "123456789"}  # 更新登录信息
    msg = session.post(url, data=data)
    text = json.loads(msg.text)
    if msg.status_code == 200 and text["ret"] == 1:
      logger.info(text["msg"])
      return True
    else:
      logger.error(text["msg"])
      return False
  except Exception as e:
    logger.error(e)
    return False

# 签到
def checkin():
  logger.info('开始签到')
  try:
    url = 'https://sign-service.acck.io/api/acLogs/sign'  # 更新签到URL
    msg = session.post(url)
    text = json.loads(msg.text)
    if msg.status_code == 200 and text["ret"] == 1:
      logger.info(text["msg"])
    else:
      logger.error(text["msg"])
    return text["msg"]
  except Exception as e:
    logger.error(e)
    return "抛出异常"

# 入口
if __name__ == '__main__':
  login_res = login()
  if login_res:
    checkin_res = checkin()
    logger.info(checkin_res)  # 输出签到结果
