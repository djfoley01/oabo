output = """{
    "apiVersion": "batch/v1beta1",
    "kind": "CronJob",
    "metadata": {
        "creationTimestamp": null,
        "name": "pi",
        "namespace": namespace
    },
    "spec": {
        "concurrencyPolicy": "Allow",
        "failedJobsHistoryLimit": 1,
        "jobTemplate": {
            "metadata": {
                "creationTimestamp": null
            },
            "spec": {
                "template": {
                    "metadata": {
                        "creationTimestamp": null,
                        "labels": {
                            "parent": "backup-" + deploymconfig
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "command": [
                                    "perl",
                                    "-Mbignum=bpi",
                                    "-wle",
                                    "print bpi(2000)"
                                ],
                                "env": [
                                    "
                                ],
                                "image": "perl",
                                "imagePullPolicy": "Always",
                                "name": "pi",
                                "resources": {},
                                "terminationMessagePath": "/dev/termination-log",
                                "terminationMessagePolicy": "File"
                            }
                        ],
                        "dnsPolicy": "ClusterFirst",
                        "restartPolicy": "OnFailure",
                        "schedulerName": "default-scheduler",
                        "securityContext": {},
                        "terminationGracePeriodSeconds": 30
                    }
                }
            }
        },
        "schedule": "*/1 * * * *",
        "successfulJobsHistoryLimit": 3,
        "suspend": false
    },
    "status": {}
}"""

print(output)

