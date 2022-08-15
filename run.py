import subprocess



def run_command(command):
    whole = "bash -c \"" + command + " \""
    return subprocess.check_output(whole, shell=True)


def _check_type(t):
    result = run_command("find | grep \\." + t + "$")
    r = result.splitlines()
    

    number = 0
    for line in r:
        run_command("feh -. -D 1 --on-last-slide quit '" + str(line)[4:-1] + "'")
        answer = input("Copy file? (y|N)")
        print(answer)
        if (answer == "y" or answer == "Y"):
            run_command("cp '" + str(line)[4:-1] + "' command_result/" + str(number) + "." + t)
            number += 1

def check_type(t):
    try:
        _check_type(t)
    except:
        print("Nothing found for " + t)


run_command("mkdir command_result")

check_type("png")
check_type("PNG")
check_type("jpg")
check_type("jpeg")
check_type("JPG")
check_type("JPEG")
