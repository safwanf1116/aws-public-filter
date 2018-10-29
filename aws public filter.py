import boto3

ec2 = boto3.resource('ec2')

ram_dict = {
        "c4.large" : "3.75 GiB",
        "i3.large" : "15.25 GiB",
        "m3.medium" : "3.75 GiB",
        "m4.2xlarge": "32 GiB",
        "m4.2large" : "32 GiB",
        "m4.xlarge" : "16 GiB",
        "m5.2xlarge": "32 GiB",
        "m4.large" : "8 GiB",
        "m5.large" : "8 GiB",
        "m5.xlarge" : "16 GiB",
        "r5.large" : "16 GiB",
        "t2.2xlarge" : "32 GiB",
        "t2.xlarge" : "16 GiB",
        "t2.large" : "8 GiB",
        "t2.medium" : "4 GiB",
        "t2.small" : "2 GiB"
}

for i in ec2.instances.all():
    if (i.public_ip_address != None):
        print("----------------------------------------")
        for tag in i.tags: #Stepping into dictionaries to pull out needed value (Name)
                if tag["Key"] == "Name":
                        print("Name: ", tag["Value"])
        print("Instance Name: ", i.id)
        print("Public IP Address: ", i.public_ip_address)
        print("Public DNS Name: ", i.public_dns_name)
        print("Subnet ID: ", i.subnet_id)
        print("RAM Size: ",  ram_dict[i.instance_type] if ram_dict.__contains__(i.instance_type) else "unknown") #Need to find proper Attribute 
        if i.platform == "windows":
                print("Operating System: ", i.platform)
        else:              
                print("Operating System: linux")
        for security_groups in i.security_groups:
                print("Security Groups: ", security_groups["GroupName"])
        print("----------------------------------------")


