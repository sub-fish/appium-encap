from ConfigParser import ConfigParser


class Read_driver_config:
    def __init__(self):
        self.CONFIGFILE = "C:/Users/xiangyong.wang/PycharmProjects/apptest/config/driverconfig.conf"
        self.cf = ConfigParser()
        self.cf.read(self.CONFIGFILE)
        self.s = self.cf.sections()

    def read_iterm_platformVersion(self):
         platformVersion = self.cf.get("driver", "platformVersion")
         return platformVersion

    def read_iterm_platformName(self):
        platformName = self.cf.get("driver", "platformName")
        return platformName
    def read_iterm_deviceName(self):
        deviceName = self.cf.get("driver", "deviceName")
        return deviceName

    def read_iterm_appPackage(self):
        appPackage = self.cf.get("driver", "appPackage")
        return appPackage

    def read_iterm_appActivity(self):
        appActivity = self.cf.get("driver", "appActivity")
        return appActivity


if __name__ == "__main__":
    t1 = Read_driver_config()
    print t1.read_iterm_appActivity()
