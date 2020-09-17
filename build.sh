echo '########## build server begin ##########'
svn up
#pip install -r requirements.txt
uwsgi --reload uwsgi.pid
echo '########## build server end ##########'