[![](https://cloud.githubusercontent.com/assets/1317406/12406044/32cd9916-be0f-11e5-9b18-1547f284f878.png)](http://www.synapse-wireless.com/)

# SNAPconnect Example - Display Basic SNAPconnect Info

This example application queries SNAPconnect for its version, address, and encryption settings
and displays that information on the command-line.

## Running This Example

This short example application has no command-line parameters, and requires no configuration,
other than installing SNAPconnect as a dependency:

```bash
pip install --extra-index-url https://update.synapse-wireless.com/pypi snapconnect
```
    
Once you have installed SNAPconnect, simply run:

```bash
python DisplayInfo.py
```

If SNAPconnect was installed correctly, you should see output that includes your Python version string,
your SNAPconnect version number, your SNAPconnect instance's SNAP address, and your SNAPconnect instance's
encryption setting:

```bash
$ python DisplayInfo.py
Python version is 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)]
2016-04-04 22:19:09 DEBUG: Permanent license created on 2012-02-14 14:14:45.343000 for 000020
SNAP Connect version number 3.5.1
My SNAP Address is 00.00.20
Encryption is set to 0
```

**Note**: If you do not have a `license.dat` file, you will get a message explaining that SNAPconnect is using
the default trial license.

For more details, refer to source file [DisplayInfo.py](DisplayInfo.py).

## License

Copyright © 2016 [Synapse Wireless](http://www.synapse-wireless.com/), licensed under the [Apache License v2.0](LICENSE.md).

<!-- meta-tags: vvv-snapconnect, vvv-python, vvv-example -->
