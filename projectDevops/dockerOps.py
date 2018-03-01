from sshOps import SshOps

class  DockerOps():
    def __init__(self):
        pass

    def createContainer(self,id,image):
        command = "Docker run -d -it --name {} {}".format("{}_{}".format(image,id),'debian')
        ssh = SshOps()
        res = ssh.runCommand(command)
        if res['status'] == 1:
            print (res['message'])
        else:
            command = "docker exec {} uname -a {}".format(id,image)
            res = ssh.runCommand(command)
