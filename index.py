from flask import Flask, redirect, request
import random
import re
from flask_executor import Executor

app = Flask(__name__)
from flask_executor import Executor


@app.route('/')
def index():
  with open('index.html') as f:
    return f.read()


@app.route('/css/main.css')
def css():
  with open('css/main.css') as f:
    return f.read()


@app.route('/css/main.js')
def js():
  with open('css/main.js') as f:
    return f.read()


@app.route('/pc.php')
def pc():
  with open('pc.txt') as f:
    lines = [line.strip() for line in f]
    index = random.randint(0, len(lines) - 1)
    url = lines[index].strip()
    return redirect(url)


@app.route('/pe.php')
def pe():
  with open('pe.txt') as f:
    lines = [line.strip() for line in f]
    index = random.randint(0, len(lines) - 1)
    url = lines[index].strip()
    return redirect(url)


def isMobile():
  user_agent = request.headers.get('User-Agent')
  user_agent_commentsblock = re.findall(r'\((.*?)\)', user_agent)[0]
  mobile_os_list = [
      'Google Wireless Transcoder', 'Windows CE', 'WindowsCE', 'Symbian',
      'Android', 'armv6l', 'armv5', 'Mobile', 'CentOS', 'mowser', 'AvantGo',
      'Opera Mobi', 'J2ME/MIDP', 'Smartphone', 'Go.Web', 'Palm', 'iPAQ'
  ]
  mobile_token_list = [
      'Profile/MIDP', 'Configuration/CLDC-', '160×160', '176×220', '240×240',
      '240×320', '320×240', 'UP.Browser', 'UP.Link', 'SymbianOS', 'PalmOS',
      'PocketPC', 'SonyEricsson', 'Nokia', 'BlackBerry', 'Vodafone', 'BenQ',
      'Novarra-Vision', 'Iris', 'NetFront', 'HTC_', 'Xda_', 'SAMSUNG-SGH',
      'Wapaka', 'DoCoMo', 'iPhone', 'iPod'
  ]

  def CheckSubstrs(subs, str):
    for sub in subs:
      if sub in str:
        return True
    return False

  if CheckSubstrs(mobile_os_list, user_agent_commentsblock) or CheckSubstrs(
      mobile_token_list, user_agent):
    return True
  else:
    return False


@app.route('/api.php')
def api():
  if isMobile():
    return redirect('/pe.php')
  else:
    return redirect('/pc.php')


def run_in_background(func):

  def wrapper(*args, **kwargs):
    return executor.submit(func, *args, **kwargs)

  return wrapper


@app.route('/background_task')
@run_in_background
def background_task():
  return 'Background task completed'


if __name__ == '__main__':
  app.run(threaded=True, host='0.0.0.0', port=5000)
