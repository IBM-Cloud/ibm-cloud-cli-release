# Bluemix CLI

This is the command line client for [Bluemix](https://console.ng.bluemix.net/). See help of each command from [Bluemix Docs](https://console.ng.bluemix.net/docs/cli/reference/bluemix_cli/index.html) or by running `bluemix help`.

## Getting started

Download and run the installer for your platform from [Downloads](#downloads) section.

Once installed, you can login and interact with Bluemix
```
$ bluemix api https://api.ng.bluemix.net
Setting api endpoint to https://api.ng.bluemix.net...
OK

$ bluemix login
API endpoint: https://api.ng.bluemix.net

Email> xxxx@xxx.xxx.xxx

Password> 
Authenticating...
OK

$ bluemix list

Getting resources in org 'myorg' / space 'dev' as xxxx@xxx.xxx.xxx...

...
```

## Downloads
You can download the latest installers below.

| **macOS** | **Linux 64 bit** | **Windows 64 bit** |
|-----------|------------------|--------------------|
| [Bluemix_CLI.pkg](http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/latest/Bluemix_CLI.pkg) | [Bluemix_CLI_amd64.tar.gz](http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/latest/Bluemix_CLI_amd64.tar.gz) | [Bluemix_CLI_amd64.exe](http://public.dhe.ibm.com/cloud/bluemix/cli/bluemix-cli/latest/Bluemix_CLI_amd64.exe) |


32 bit releases and previous releases can be found [here](https://github.com/IBM-Bluemix/bluemix-cli-release/releases)

## Extending with plugins

Check [plugin repository](http://plugins.ng.bluemix.net/ui/repository.html#bluemix-plugins) for any extension that enhances the CLI capabilities.


To list the plugins in Bluemix plugin repository:

```
bluemix plugin repo-plugins

```

To download and install the plugin:

```
bluemix plugin install PLUGIN_NAME -r Bluemix

```

## Release notes

Please refer to [here](https://github.com/IBM-Bluemix/bluemix-cli-release/releases) for details.


# Issues, defects and feature requests

Any issues/defects, or feature requests, please [file an issue](https://github.com/IBM-Bluemix/bluemix-cli-release/issues) if not raised before.
