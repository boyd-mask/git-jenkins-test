from fabric.api import local
import os, json


def test():
    f = open(os.getcwd() + '/log')
    text = f.read()
    f.close()
    comment = json.dumps({'body': text})


    # local("curl https://api.github.com/repos/boyd-mask/git-jenkins-test/issues/2/comments -X POST -d \'{0}\'".format(comment))
