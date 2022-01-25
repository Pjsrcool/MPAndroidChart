from subprocess import Popen, PIPE

projects = [ "conductor", "mockito", "MPAndroidChart", "PhotoView"]
# projects = [ "conductor"]
for p in projects:
    script_location = p + "/getErrors.py"
    process = Popen(["python3", script_location ], stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    print(p + ":")
    print(output)
    print(err)

print("done")