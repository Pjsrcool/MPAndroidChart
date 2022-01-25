from subprocess import Popen, PIPE

process = Popen(["./gradlew", "MPChartLib:build"], stdout=PIPE, stderr=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()
f = open("output.txt", "a")

errorString = str(err)
parse = errorString.split("\\n")
# print (parse)

# parse = ["asf", "aefefewf"]
# print(len(parse))
for line in parse:
    f.write(line + "\n")
f.close()

print("done")
