def cmdissue(toissue, activesession):
      ssh_stdin, ssh_stdout, ssh_stderr = activesession.exec_command(toissue)
      return ssh_stdout.read().decode('UTF-8')
def commands_list(sshsession, commands):
    for x in commands:
        ## call our imported function and save the value returned
        resp = cmdissue(x, sshsession)
        ## if returned response is not null, print it out
        if resp != "":
            print(resp)

