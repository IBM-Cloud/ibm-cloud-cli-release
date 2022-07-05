# IBM Cloud CLI

![ppc64le](https://img.shields.io/badge/ppc64le-supported-brightgreen.svg) ![x86_64](https://img.shields.io/badge/x86__64-supported-brightgreen.svg) ![x86_64](https://img.shields.io/badge/x86-supported-brightgreen.svg) ![s390x](https://img.shields.io/badge/s390x-not%20supported-red.svg)

This is the command line client for [IBM Cloud](https://cloud.ibm.com/). See more information of IBM Cloud CLI on [IBM Cloud Docs](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started) .

## Getting started

Download and run the installer for your platform from [Downloads](#downloads) section.

Once installed, you can login and interact with IBM Cloud
```
$ ibmcloud login
API endpoint: https://cloud.ibm.com

Email> user@example.org

Password> 
Authenticating...
OK

$ ibmcloud resource service-instances

Name                                         Location   State    Type
IBM Cloud Activity Tracker with LogDNA-em   us-south   active   service_instance
Continuous Delivery-example                 us-south   active   service_instance
toolchain-example                           us-east    active   service_instance
```

## Downloads
You can download the latest installers below.

| **macOS** | **Linux 64 bit** | **Windows 64 bit** |
|-----------|------------------|--------------------|
| [download](https://download.clis.cloud.ibm.com/ibm-cloud-cli/2.9.0/IBM_Cloud_CLI_2.9.0.pkg) | [download](https://download.clis.cloud.ibm.com/ibm-cloud-cli/2.9.0/IBM_Cloud_CLI_2.9.0_amd64.tar.gz) | [download](https://download.clis.cloud.ibm.com/ibm-cloud-cli/2.9.0/IBM_Cloud_CLI_2.9.0_amd64.exe) |


32 bit releases and previous releases can be found [here](https://github.com/IBM-Cloud/ibm-cloud-cli-release/releases)

## Extending with plugins

Check [plugin repository](http://plugins.cloud.ibm.com) for any extension that enhances the CLI capabilities.


To list the plugins in IBM Cloud plugin repository:

```
ibmcloud plugin repo-plugins

```

To download and install the plugin:

```
ibmcloud plugin install PLUGIN_NAME 

```

## Release notes

Please refer to [here](https://github.com/IBM-Cloud/ibm-cloud-cli-release/releases) for details.


# Issues, defects and feature requests

Any issues/defects, or feature requests, please [file an issue](https://github.com/IBM-Cloud/ibm-cloud-cli-release/issues) if not raised before.
