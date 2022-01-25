from subprocess import Popen, PIPE
from random import randint
import os

os.chdir("MPAndroidChart")

process = Popen(["./gradlew", "MPChartLib:build"], stdout=PIPE, stderr=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()

# print(output)
# print(err)

errorString = str(err)
parse = errorString.split("\\n")

print(len(parse))

# print parsed output
# for line in parse:
#     f.write(line + "\n")
# f.close()

errorCount = 0
for i in range (3, len(parse), 4):
    if parse[i] == "    (see http://t.uber.com/nullaway )":
        errorCount += 1
print("Number of errors: " + str(errorCount))

randErrors = []
for i in range(5):
    randErrors.append(randint(0, errorCount))

print("Random errors selected: " + str(randErrors))

os.chdir("..")
if errorCount >= 5:
    f = open("MPAndroid_Errors.txt", "a")
    for i in randErrors:
        for j in range(4):
            f.write(parse[(i*4) + j] + "\n")
    f.close()

print("done")
