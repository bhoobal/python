#!/bin/python3
import json
input_json = """{
    "Reservations": [
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    }, 
                    "StateReason": {
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown", 
                        "Code": "Client.UserInitiatedShutdown"
                    }, 
                    "PublicDnsName": "", 
                    "Platform": "windows", 
                    "State": {
                        "Code": 48, 
                        "Name": "terminated"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2018-10-15T11:45:07.000Z", 
                    "ProductCodes": [], 
                    "CpuOptions": {
                        "CoreCount": 4, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "User initiated (2018-10-15 16:55:31 GMT)", 
                    "InstanceId": "i-052b77d2c7b8e90e2", 
                    "ImageId": "ami-00a8ae3387b86a6ca", 
                    "PrivateDnsName": "", 
                    "KeyName": "Main", 
                    "SecurityGroups": [], 
                    "ClientToken": "", 
                    "InstanceType": "t2.xlarge", 
                    "NetworkInterfaces": [], 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1f"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "OnDemand", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "0 23 * * *", 
                            "Key": "auto:stop"
                        }, 
                        {
                            "Value": "mwelch", 
                            "Key": "creator"
                        }, 
                        {
                            "Value": "mwelch-42", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "0 12 * * 1-5", 
                            "Key": "auto:start"
                        }, 
                        {
                            "Value": "mwelch", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "default", 
                            "Key": "profile"
                        }, 
                        {
                            "Value": "odi", 
                            "Key": "role"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-00296fe2d68c9ef5c", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "enabled"
                    }, 
                    "PublicDnsName": "ec2-52-3-247-100.compute-1.amazonaws.com", 
                    "StateReason": {
                        "Message": "", 
                        "Code": ""
                    }, 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2017-06-23T19:50:22.000Z", 
                    "PublicIpAddress": "52.3.247.100", 
                    "PrivateIpAddress": "10.5.3.156", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-896d01ed", 
                    "CpuOptions": {
                        "CoreCount": 1, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-066989f4d4922c728", 
                    "ImageId": "ami-c8580bdf", 
                    "PrivateDnsName": "ip-10-5-3-156.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "BosOffice-PreProd-Instance-All", 
                            "GroupId": "sg-7077b908"
                        }, 
                        {
                            "GroupName": "BosOffice-PreProd-Services-ELB", 
                            "GroupId": "sg-7d77b905"
                        }, 
                        {
                            "GroupName": "PreProd-PreProd-Instance-All", 
                            "GroupId": "sg-7f77b907"
                        }
                    ], 
                    "ClientToken": "bca26c96-2922-4f38-a25d-ba6fb029ff30_subnet-e6ef81db_1", 
                    "SubnetId": "subnet-e6ef81db", 
                    "InstanceType": "t2.small", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "06:3b:04:45:f3:16", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-896d01ed", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-27cfad26", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-5-3-156.ec2.internal", 
                                    "PrivateIpAddress": "10.5.3.156", 
                                    "Primary": true, 
                                    "Association": {
                                        "PublicIp": "52.3.247.100", 
                                        "PublicDnsName": "ec2-52-3-247-100.compute-1.amazonaws.com", 
                                        "IpOwnerId": "amazon"
                                    }
                                }
                            ], 
                            "PrivateDnsName": "ip-10-5-3-156.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-277b00c7", 
                                "AttachTime": "2017-06-23T19:50:22.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "BosOffice-PreProd-Instance-All", 
                                    "GroupId": "sg-7077b908"
                                }, 
                                {
                                    "GroupName": "BosOffice-PreProd-Services-ELB", 
                                    "GroupId": "sg-7d77b905"
                                }, 
                                {
                                    "GroupName": "PreProd-PreProd-Instance-All", 
                                    "GroupId": "sg-7f77b907"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "PrivateIpAddress": "10.5.3.156", 
                            "SubnetId": "subnet-e6ef81db", 
                            "Association": {
                                "PublicIp": "52.3.247.100", 
                                "PublicDnsName": "ec2-52-3-247-100.compute-1.amazonaws.com", 
                                "IpOwnerId": "amazon"
                            }
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1e"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-03261438c7abdf320", 
                                "AttachTime": "2017-06-23T19:50:23.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAIQSJ4J6E4NQGNPQ6I", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/vault_server_instance_profile"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "ops", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "preprod", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "TF-PreProd-Vault-Cluster", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "vault", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "TF-PreProd-Vault-Cluster", 
                            "Key": "aws:autoscaling:groupName"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-040a2e28cbbb5b82f", 
            "RequesterId": "226008221399", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    }, 
                    "PublicDnsName": "", 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2018-10-15T11:45:07.000Z", 
                    "PrivateIpAddress": "10.3.38.40", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-787a351d", 
                    "CpuOptions": {
                        "CoreCount": 2, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-08a37b11053294cc3", 
                    "EnaSupport": true, 
                    "ImageId": "ami-02818559cbcc107cb", 
                    "PrivateDnsName": "ip-10-3-38-40.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "TESTPRIVSGWEB", 
                            "GroupId": "sg-de47d3ba"
                        }
                    ], 
                    "ClientToken": "", 
                    "SubnetId": "subnet-903eb19f", 
                    "InstanceType": "t2.large", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "16:9a:34:9d:c9:6c", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-787a351d", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-03a95178e8f38a859", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-3-38-40.ec2.internal", 
                                    "Primary": true, 
                                    "PrivateIpAddress": "10.3.38.40"
                                }
                            ], 
                            "PrivateDnsName": "ip-10-3-38-40.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-0c2b3e4a0a7dd3a66", 
                                "AttachTime": "2018-10-12T20:27:08.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "TESTPRIVSGWEB", 
                                    "GroupId": "sg-de47d3ba"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "SubnetId": "subnet-903eb19f", 
                            "PrivateIpAddress": "10.3.38.40"
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1f"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-020852fe4bcd83840", 
                                "AttachTime": "2018-10-12T20:27:08.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAIIKXASASAKNR6YDBQ", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/odi-instance"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "0 12 * * 1-5", 
                            "Key": "auto:start"
                        }, 
                        {
                            "Value": "jmacinnes", 
                            "Key": "creator"
                        }, 
                        {
                            "Value": "0 23 * * *", 
                            "Key": "auto:stop"
                        }, 
                        {
                            "Value": "default", 
                            "Key": "profile"
                        }, 
                        {
                            "Value": "jmacinnes", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "OnDemand", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "rd-293-linux", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "odi", 
                            "Key": "role"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-0dc46f5f94f308e7d", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    }, 
                    "StateReason": {
                        "Message": "Client.UserInitiatedShutdown: User initiated shutdown", 
                        "Code": "Client.UserInitiatedShutdown"
                    }, 
                    "PublicDnsName": "", 
                    "Platform": "windows", 
                    "State": {
                        "Code": 80, 
                        "Name": "stopped"
                    }, 
                    "EbsOptimized": true, 
                    "LaunchTime": "2015-12-08T16:50:34.000Z", 
                    "PrivateIpAddress": "10.3.1.28", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-787a351d", 
                    "CpuOptions": {
                        "CoreCount": 1, 
                        "ThreadsPerCore": 2
                    }, 
                    "StateTransitionReason": "User initiated (2017-04-03 21:05:34 GMT)", 
                    "InstanceId": "i-c822c779", 
                    "ImageId": "ami-14cf817e", 
                    "PrivateDnsName": "ip-10-3-1-28.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "TESTPRIVSGWEB", 
                            "GroupId": "sg-de47d3ba"
                        }
                    ], 
                    "ClientToken": "ZZFZz1449593433487", 
                    "SubnetId": "subnet-c19333ea", 
                    "InstanceType": "m4.large", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "12:9a:52:d4:be:9b", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-787a351d", 
                            "Description": "Primary network interface", 
                            "NetworkInterfaceId": "eni-ee4861ce", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-3-1-28.ec2.internal", 
                                    "Primary": true, 
                                    "PrivateIpAddress": "10.3.1.28"
                                }
                            ], 
                            "PrivateDnsName": "ip-10-3-1-28.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-500eafbe", 
                                "AttachTime": "2015-12-08T16:50:34.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "TESTPRIVSGWEB", 
                                    "GroupId": "sg-de47d3ba"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "SubnetId": "subnet-c19333ea", 
                            "PrivateIpAddress": "10.3.1.28"
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1a"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-55680cba", 
                                "AttachTime": "2015-12-08T16:50:36.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "Fiddler (Preprod)", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "fiddler", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "preprod", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "infra", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "Infrastructure", 
                            "Key": "Owner"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-3dba9d94", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    }, 
                    "PublicDnsName": "", 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2018-10-15T11:45:07.000Z", 
                    "PrivateIpAddress": "10.3.37.90", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-787a351d", 
                    "CpuOptions": {
                        "CoreCount": 2, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-0d84e1f75fc3d6ede", 
                    "EnaSupport": true, 
                    "ImageId": "ami-12d5ec6d", 
                    "PrivateDnsName": "ip-10-3-37-90.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "TESTPRIVSGWEB", 
                            "GroupId": "sg-de47d3ba"
                        }
                    ], 
                    "ClientToken": "", 
                    "SubnetId": "subnet-903eb19f", 
                    "InstanceType": "t2.large", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "16:bc:ee:e4:00:4c", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-787a351d", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-fc736d59", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-3-37-90.ec2.internal", 
                                    "Primary": true, 
                                    "PrivateIpAddress": "10.3.37.90"
                                }
                            ], 
                            "PrivateDnsName": "ip-10-3-37-90.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-c7a3b262", 
                                "AttachTime": "2018-07-17T18:28:31.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "TESTPRIVSGWEB", 
                                    "GroupId": "sg-de47d3ba"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "SubnetId": "subnet-903eb19f", 
                            "PrivateIpAddress": "10.3.37.90"
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1f"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-0dd45d5894ad014b9", 
                                "AttachTime": "2018-07-17T18:28:32.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAIIKXASASAKNR6YDBQ", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/odi-instance"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "default", 
                            "Key": "profile"
                        }, 
                        {
                            "Value": "fsergile", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "odi", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "fs-ident2-linux", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "fsergile", 
                            "Key": "creator"
                        }, 
                        {
                            "Value": "0 12 * * 1-5", 
                            "Key": "auto:start"
                        }, 
                        {
                            "Value": "OnDemand", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "0 23 * * *", 
                            "Key": "auto:stop"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-0dfb93d3fc7896980", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "enabled"
                    }, 
                    "StateReason": {
                        "Message": "", 
                        "Code": ""
                    }, 
                    "PublicDnsName": "", 
                    "Platform": "windows", 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2017-06-28T15:42:14.000Z", 
                    "PrivateIpAddress": "10.5.2.24", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-896d01ed", 
                    "CpuOptions": {
                        "CoreCount": 2, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-09243883527d82c68", 
                    "EnaSupport": true, 
                    "ImageId": "ami-f9f2c3ef", 
                    "PrivateDnsName": "ip-10-5-2-24.ec2.internal", 
                    "KeyName": "preprod", 
                    "SecurityGroups": [
                        {
                            "GroupName": "BosOffice-PreProd-Instance-All", 
                            "GroupId": "sg-7077b908"
                        }, 
                        {
                            "GroupName": "PreProd-PreProd-Instance-All", 
                            "GroupId": "sg-7f77b907"
                        }
                    ], 
                    "ClientToken": "0bf99020-fced-42c1-9f12-375377934c8a_subnet-d354a2f9_1", 
                    "SubnetId": "subnet-d354a2f9", 
                    "InstanceType": "t2.large", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "12:bf:06:c4:59:0e", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-896d01ed", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-8d5ff121", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-5-2-24.ec2.internal", 
                                    "Primary": true, 
                                    "PrivateIpAddress": "10.5.2.24"
                                }
                            ], 
                            "PrivateDnsName": "ip-10-5-2-24.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-c80d8ee9", 
                                "AttachTime": "2017-06-28T15:42:14.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "BosOffice-PreProd-Instance-All", 
                                    "GroupId": "sg-7077b908"
                                }, 
                                {
                                    "GroupName": "PreProd-PreProd-Instance-All", 
                                    "GroupId": "sg-7f77b907"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "SubnetId": "subnet-d354a2f9", 
                            "PrivateIpAddress": "10.5.2.24"
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1a"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-0dd35afe844d41dda", 
                                "AttachTime": "2017-06-28T15:42:15.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAJPTU6GLQISTQ36OBQ", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/bach-preprod-iam-instance-profile"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "bach", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "preprod", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "TF-PreProd-Bach-Green", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "PreProd", 
                            "Key": "Patch Group"
                        }, 
                        {
                            "Value": "True", 
                            "Key": "ParallelDeploy"
                        }, 
                        {
                            "Value": "contest_entry", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "TF-PreProd-Bach-Green", 
                            "Key": "aws:autoscaling:groupName"
                        }, 
                        {
                            "Value": "S", 
                            "Key": "maintenance_window"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-0edfe66fb85856855", 
            "RequesterId": "226008221399", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "enabled"
                    }, 
                    "StateReason": {
                        "Message": "", 
                        "Code": ""
                    }, 
                    "PublicDnsName": "", 
                    "Platform": "windows", 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2017-06-30T16:16:05.000Z", 
                    "PrivateIpAddress": "10.5.0.25", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-896d01ed", 
                    "CpuOptions": {
                        "CoreCount": 1, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-0fddfcc4d5af744a2", 
                    "EnaSupport": true, 
                    "ImageId": "ami-0ce6cf1a", 
                    "PrivateDnsName": "ip-10-5-0-25.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "BosOffice-PreProd-Instance-All", 
                            "GroupId": "sg-7077b908"
                        }, 
                        {
                            "GroupName": "PreProd-PreProd-Instance-All", 
                            "GroupId": "sg-7f77b907"
                        }
                    ], 
                    "ClientToken": "74fcf11f-13a8-47fb-94f6-71daec011f72_subnet-d74eeda1_1", 
                    "SubnetId": "subnet-d74eeda1", 
                    "InstanceType": "t2.small", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "0a:97:42:d0:d9:64", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-896d01ed", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-0dfdc0dd", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-5-0-25.ec2.internal", 
                                    "Primary": true, 
                                    "PrivateIpAddress": "10.5.0.25"
                                }
                            ], 
                            "PrivateDnsName": "ip-10-5-0-25.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-a5d7af9b", 
                                "AttachTime": "2017-06-30T16:16:05.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "BosOffice-PreProd-Instance-All", 
                                    "GroupId": "sg-7077b908"
                                }, 
                                {
                                    "GroupName": "PreProd-PreProd-Instance-All", 
                                    "GroupId": "sg-7f77b907"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "SubnetId": "subnet-d74eeda1", 
                            "PrivateIpAddress": "10.5.0.25"
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1b"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-03052b55670733ece", 
                                "AttachTime": "2017-06-30T16:16:06.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAI3SBR367MOZROCGL2", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/mjolnir-preprod-iam-instance-profile"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "FinOps Payments", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "TF-PreProd-Mjolnir-Green", 
                            "Key": "aws:autoscaling:groupName"
                        }, 
                        {
                            "Value": "PreProd", 
                            "Key": "Patch Group"
                        }, 
                        {
                            "Value": "mjolnir", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "S", 
                            "Key": "maintenance_window"
                        }, 
                        {
                            "Value": "preprod", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "TF-PreProd-Mjolnir-Green", 
                            "Key": "Name"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-0ab1575de580ae648", 
            "RequesterId": "226008221399", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "enabled"
                    }, 
                    "PublicDnsName": "ec2-54-86-38-174.compute-1.amazonaws.com", 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2016-09-09T15:58:30.000Z", 
                    "PublicIpAddress": "54.86.38.174", 
                    "PrivateIpAddress": "10.5.0.16", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-896d01ed", 
                    "CpuOptions": {
                        "CoreCount": 1, 
                        "ThreadsPerCore": 2
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-086bf791", 
                    "ImageId": "ami-fce3c696", 
                    "PrivateDnsName": "ip-10-5-0-16.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "BosOffice-PreProd-Support", 
                            "GroupId": "sg-7c77b904"
                        }, 
                        {
                            "GroupName": "BosOffice-PreProd-Instance-All", 
                            "GroupId": "sg-7077b908"
                        }, 
                        {
                            "GroupName": "PreProd-PreProd-Instance-All", 
                            "GroupId": "sg-7f77b907"
                        }
                    ], 
                    "ClientToken": "", 
                    "SubnetId": "subnet-d74eeda1", 
                    "InstanceType": "r3.large", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "0a:4e:89:ff:39:29", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-896d01ed", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-517f0d56", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-5-0-16.ec2.internal", 
                                    "PrivateIpAddress": "10.5.0.16", 
                                    "Primary": true, 
                                    "Association": {
                                        "PublicIp": "54.86.38.174", 
                                        "PublicDnsName": "ec2-54-86-38-174.compute-1.amazonaws.com", 
                                        "IpOwnerId": "amazon"
                                    }
                                }
                            ], 
                            "PrivateDnsName": "ip-10-5-0-16.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-8b57be39", 
                                "AttachTime": "2016-09-09T15:58:30.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "BosOffice-PreProd-Support", 
                                    "GroupId": "sg-7c77b904"
                                }, 
                                {
                                    "GroupName": "BosOffice-PreProd-Instance-All", 
                                    "GroupId": "sg-7077b908"
                                }, 
                                {
                                    "GroupName": "PreProd-PreProd-Instance-All", 
                                    "GroupId": "sg-7f77b907"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "PrivateIpAddress": "10.5.0.16", 
                            "SubnetId": "subnet-d74eeda1", 
                            "Association": {
                                "PublicIp": "54.86.38.174", 
                                "PublicDnsName": "ec2-54-86-38-174.compute-1.amazonaws.com", 
                                "IpOwnerId": "amazon"
                            }
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "TF-Aerospike-XDR-2-PG", 
                        "AvailabilityZone": "us-east-1b"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-98158334", 
                                "AttachTime": "2016-09-09T15:58:31.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAI6EDGDDAMOCAZREKQ", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/aerospike-preprod-iam-instance-profile"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "TF-PreProd-Aerospike-XDR-2", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "Aerospike", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "Infra", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "preprod", 
                            "Key": "env"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-5a53be8d", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    }, 
                    "PublicDnsName": "ec2-34-239-157-231.compute-1.amazonaws.com", 
                    "Platform": "windows", 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2018-10-15T11:45:07.000Z", 
                    "PublicIpAddress": "34.239.157.231", 
                    "PrivateIpAddress": "10.3.37.12", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-787a351d", 
                    "CpuOptions": {
                        "CoreCount": 4, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-02a21d164abf57842", 
                    "ImageId": "ami-07047544f18a883fa", 
                    "PrivateDnsName": "ip-10-3-37-12.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "PayPal IPN Override", 
                            "GroupId": "sg-8dd880e9"
                        }, 
                        {
                            "GroupName": "TESTPRIVSGWEB", 
                            "GroupId": "sg-de47d3ba"
                        }
                    ], 
                    "ClientToken": "", 
                    "SubnetId": "subnet-903eb19f", 
                    "InstanceType": "t2.xlarge", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "16:ae:6b:36:d0:58", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-787a351d", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-0f1176fdcaba855e1", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-3-37-12.ec2.internal", 
                                    "PrivateIpAddress": "10.3.37.12", 
                                    "Primary": true, 
                                    "Association": {
                                        "PublicIp": "34.239.157.231", 
                                        "PublicDnsName": "ec2-34-239-157-231.compute-1.amazonaws.com", 
                                        "IpOwnerId": "amazon"
                                    }
                                }
                            ], 
                            "PrivateDnsName": "ip-10-3-37-12.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-007b45491fabde44a", 
                                "AttachTime": "2018-08-24T14:21:36.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "PayPal IPN Override", 
                                    "GroupId": "sg-8dd880e9"
                                }, 
                                {
                                    "GroupName": "TESTPRIVSGWEB", 
                                    "GroupId": "sg-de47d3ba"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "PrivateIpAddress": "10.3.37.12", 
                            "SubnetId": "subnet-903eb19f", 
                            "Association": {
                                "PublicIp": "34.239.157.231", 
                                "PublicDnsName": "ec2-34-239-157-231.compute-1.amazonaws.com", 
                                "IpOwnerId": "amazon"
                            }
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1f"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-089ce57f45657f596", 
                                "AttachTime": "2018-08-24T14:21:37.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAIIKXASASAKNR6YDBQ", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/odi-instance"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "0 12 * * 1-5", 
                            "Key": "auto:start"
                        }, 
                        {
                            "Value": "0 23 * * *", 
                            "Key": "auto:stop"
                        }, 
                        {
                            "Value": "odi", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "fs-ident6", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "fsergile", 
                            "Key": "creator"
                        }, 
                        {
                            "Value": "OnDemand", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "fsergile", 
                            "Key": "owner"
                        }, 
                        {
                            "Value": "default", 
                            "Key": "profile"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-021c270f3165f2a93", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }, 
        {
            "Instances": [
                {
                    "Monitoring": {
                        "State": "disabled"
                    }, 
                    "StateReason": {
                        "Message": "", 
                        "Code": ""
                    }, 
                    "PublicDnsName": "ec2-52-91-0-157.compute-1.amazonaws.com", 
                    "Platform": "windows", 
                    "State": {
                        "Code": 16, 
                        "Name": "running"
                    }, 
                    "EbsOptimized": false, 
                    "LaunchTime": "2017-10-11T11:45:06.000Z", 
                    "PublicIpAddress": "52.91.0.157", 
                    "PrivateIpAddress": "10.3.1.52", 
                    "ProductCodes": [], 
                    "VpcId": "vpc-787a351d", 
                    "CpuOptions": {
                        "CoreCount": 4, 
                        "ThreadsPerCore": 1
                    }, 
                    "StateTransitionReason": "", 
                    "InstanceId": "i-030a6098d460812b0", 
                    "ImageId": "ami-f0b3748a", 
                    "PrivateDnsName": "ip-10-3-1-52.ec2.internal", 
                    "KeyName": "Main", 
                    "SecurityGroups": [
                        {
                            "GroupName": "PayPal IPN Override", 
                            "GroupId": "sg-8dd880e9"
                        }, 
                        {
                            "GroupName": "TESTPRIVSGWEB", 
                            "GroupId": "sg-de47d3ba"
                        }
                    ], 
                    "ClientToken": "", 
                    "SubnetId": "subnet-c19333ea", 
                    "InstanceType": "t2.xlarge", 
                    "NetworkInterfaces": [
                        {
                            "Status": "in-use", 
                            "MacAddress": "12:2f:62:3a:79:70", 
                            "SourceDestCheck": true, 
                            "VpcId": "vpc-787a351d", 
                            "Description": "", 
                            "NetworkInterfaceId": "eni-9b09f911", 
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "ip-10-3-1-52.ec2.internal", 
                                    "PrivateIpAddress": "10.3.1.52", 
                                    "Primary": true, 
                                    "Association": {
                                        "PublicIp": "52.91.0.157", 
                                        "PublicDnsName": "ec2-52-91-0-157.compute-1.amazonaws.com", 
                                        "IpOwnerId": "amazon"
                                    }
                                }
                            ], 
                            "PrivateDnsName": "ip-10-3-1-52.ec2.internal", 
                            "Attachment": {
                                "Status": "attached", 
                                "DeviceIndex": 0, 
                                "DeleteOnTermination": true, 
                                "AttachmentId": "eni-attach-e8863c1f", 
                                "AttachTime": "2017-10-05T15:31:56.000Z"
                            }, 
                            "Groups": [
                                {
                                    "GroupName": "PayPal IPN Override", 
                                    "GroupId": "sg-8dd880e9"
                                }, 
                                {
                                    "GroupName": "TESTPRIVSGWEB", 
                                    "GroupId": "sg-de47d3ba"
                                }
                            ], 
                            "Ipv6Addresses": [], 
                            "OwnerId": "248797271221", 
                            "PrivateIpAddress": "10.3.1.52", 
                            "SubnetId": "subnet-c19333ea", 
                            "Association": {
                                "PublicIp": "52.91.0.157", 
                                "PublicDnsName": "ec2-52-91-0-157.compute-1.amazonaws.com", 
                                "IpOwnerId": "amazon"
                            }
                        }
                    ], 
                    "SourceDestCheck": true, 
                    "Placement": {
                        "Tenancy": "default", 
                        "GroupName": "", 
                        "AvailabilityZone": "us-east-1a"
                    }, 
                    "Hypervisor": "xen", 
                    "BlockDeviceMappings": [
                        {
                            "DeviceName": "/dev/sda1", 
                            "Ebs": {
                                "Status": "attached", 
                                "DeleteOnTermination": true, 
                                "VolumeId": "vol-00ceb64669d62cb8b", 
                                "AttachTime": "2017-10-05T15:31:57.000Z"
                            }
                        }
                    ], 
                    "Architecture": "x86_64", 
                    "RootDeviceType": "ebs", 
                    "IamInstanceProfile": {
                        "Id": "AIPAIIKXASASAKNR6YDBQ", 
                        "Arn": "arn:aws:iam::248797271221:instance-profile/odi-instance"
                    }, 
                    "RootDeviceName": "/dev/sda1", 
                    "VirtualizationType": "hvm", 
                    "Tags": [
                        {
                            "Value": "odi", 
                            "Key": "role"
                        }, 
                        {
                            "Value": "merch", 
                            "Key": "Name"
                        }, 
                        {
                            "Value": "dkerrigan", 
                            "Key": "creator"
                        }, 
                        {
                            "Value": "OnDemand", 
                            "Key": "env"
                        }, 
                        {
                            "Value": "dkerrigan", 
                            "Key": "owner"
                        }
                    ], 
                    "AmiLaunchIndex": 0
                }
            ], 
            "ReservationId": "r-0fc6ff30a08f43f41", 
            "Groups": [], 
            "OwnerId": "248797271221"
        }
    ], 
    "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxMH0="
}"""
# Complete the 'main' function below.

def main():
    # Write your code here
    # Q0 - "Hellow world"
    #print("Hello world!")
    
    #Q1 - total no of Instance ids
    counter = 0
        
    loadjson =json.loads(input_json)
    
    
    for instanceid in (loadjson["Reservations"]):
        # print(instanceid["Instances"])
        for iid in instanceid["Instances"]:
            counter +=1            
            #print("Length of tags", len(iid['Tags']))
            for i in range(len(iid['Tags'])):
                
                for kkey in  iid['Tags'][i]:
                    #print(kkey) 
                    #print(iid['Tags'][i][kkey])
                    if(iid['Tags'][i][kkey] == "OnDemand"):
                    #if(iid['Tags'][i]['Value'] == "OnDemand"):
                        print (iid["InstanceId"], "is OnDemand tagged instance")   
                    
                    if(iid['Tags'][i][kkey] == "auto:start"):
                        print("Auto start enabled ",iid['Tags'][i]['Value'])
                    if(iid['Tags'][i][kkey] == "preprod" and iid["Monitoring"]["State"] == "enabled"):
                        print(iid["InstanceId"], " Monitoring is Enabled and pre prod instance")            
            if iid["Monitoring"]["State"] == "disabled":
                print(iid["InstanceId"], " Monitoring is disabled")            
    print("No of Instances is ", counter)
     

if __name__ == '__main__':
    main()

