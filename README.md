# Bluemix CLI
This is the command line for [Bluemix](https://console.ng.bluemix.net/). See help of each command [here](https://console.ng.bluemix.net/docs/cli/reference/bluemix_cli/index.html) or by running `bluemix help`.

# Getting started

Download and run the installer for your platform from [Download](#Download) section.

Once installed, you can login and interact with Bluemix
```
$ bx api https://api.ng.bluemix.net
Setting api endpoint to https://api.ng.bluemix.net...
OK

$ bx login
API endpoint: https://api.ng.bluemix.net

Email> xxxx@xxx.xxx.xxx

Password> 
Authenticating...
OK

$ bx list

Getting resources in org 'boyang@cn.ibm.com' / space 'ben' as xxxx@xxx.xxx.xxx...

...
```
Check our [plugin repository](http://plugins.ng.bluemix.net/ui/repository.html#bluemix-plugins) for any extension that enahnce our CLI capability.

# Download
You can download the latest installers below.

| **macOS** | **Linux 64 bit** | **Windows 64 bit** |
|-----------|------------------|--------------------|
| [Bluemix_CLI.pkg](http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/Bluemix_CLI.pkg) | [Bluemix_CLI_amd64.tar.gz](http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/Bluemix_CLI_amd64.tar.gz) | [Bluemix_CLI_amd64.exe](http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/Bluemix_CLI_amd64.exe) |

# Changelog
Please refer to [here](./CHANGELOG.md) for details.


# Issues and defects
Any issue or defect, please [report in this GIT project repository](https://github.com/IBM-Bluemix/bluemix-cli-release/issues).