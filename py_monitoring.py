import psutil


print "CPU core :", psutil.cpu_count(logical=True)

usage5 = psutil.cpu_percent(interval=5)

print "CPU usage :", usage5

print "RAM usage :", psutil.virtual_memory()

print "Disk usage :", psutil.disk_usage('/')

usage25 = psutil.cpu_percent(interval=25)
usage30 = usage5+usage25
print "CPU usage after 30 seconds :", usage30

# average usage of CPU!!

usage60 = psutil.cpu_percent(interval=30)

avg_usage60 = (usage30 + usage60) / 2

print "Average usage after a minute is :", avg_usage60

usage240 = psutil.cpu_percent(interval=240)

avg_usage5 = (usage240 + avg_usage60) / 2

print "Average usage after 5 minutes is :", avg_usage5
