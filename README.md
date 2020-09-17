<!--
 * @Description: 
 * @Author: CoolSnow (coolsnow2020@gmail.com)
 * @Date: 2020-09-14 11:54:05
 * @LastEditors: CoolSnow
 * @LastEditTime: 2020-09-17 10:57:48
-->
# start
uwsgi -d --ini uwsgi.ini

# reload
uwsgi --reload uwsgi.pid

# stop
uwsgi --stop uwsgi.pid

# check status
netstat -lnp|grep 5001

# requirements
1. pip freeze >requirements.txt  (generate)
2. pip install -r requirements.txt (install)