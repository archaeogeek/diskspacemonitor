Disk Space Monitor
================

Quick and dirty cross-platform script for monitoring disk space and alerting via email if pre-defined limit is reached.

Tested with python 2.6 but should/may work with 2.5+. Should work with windows and linux variants- not tested with Mac.

**Requirements**

  - Python 2.5+
  
 **Instructions**

  - If you wish to get an email alert when disk space reaches a pre-defined limit, edit the email config section at the top of the file to include details of your SMTP server, sending email, recipient email and message, leave unchanged if not required.
  - Edit the disk section to include the folder or drive that you wish to monitor, in either linux or windows format.
  - Edit the limit parameter to specify the free space size in GB at which you wish to be notified.

**Usage**

    python diskspace.py

**Todo**

Allow specification of multiple drives or folders
