---
title: "Capabilities spécifiques du Driver"
weight: 2
---

{{% notice info %}}
<i class="fas fa-language"></i> Page being translated from 
English to French. Do you speak French? Help us to translate
it by sending us pull requests!
{{% /notice %}}

## Firefox

### Define Capabilities using `FirefoxOptions`

`FirefoxOptions` is the new way to define capabilities for the Firefox 
browser and should generally be used in preference to DesiredCapabilities.

{{< code-tab >}}
  {{< code-panel language="java" >}}
FirefoxOptions options = new FirefoxOptions();
options.addPreference("network.proxy.type", 0);
driver = new RemoteWebDriver(options);
  {{< / code-panel >}}
  {{< code-panel language="python" >}}
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
var options = new FirefoxOptions();
options.Proxy.Kind = ProxyKind.Direct;
var driver = new FirefoxDriver(options);
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
require 'selenium-webdriver'
opts = Selenium::WebDriver::Firefox::Options.new(args: ['-headless'])
driver = Selenium::WebDriver.for(:firefox, options: opts)
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
const { Builder } = require("selenium-webdriver");
const firefox = require('selenium-webdriver/firefox');

const options = new firefox.Options();
options.headless();
const driver = new Builder()
    .forBrowser('firefox')
    .setFirefoxOptions(options)
    .build();
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
val options = new FirefoxOptions()
options.addPreference("network.proxy.type", 0)
driver = RemoteWebDriver(options)
  {{< / code-panel >}}
{{< / code-tab >}}


### Setting a custom profile

It is possible to create a custom profile for Firefox as demonstrated below.

{{< code-tab >}}
  {{< code-panel language="java" >}}
FirefoxProfile profile = new FirefoxProfile();
FirefoxOptions options = new FirefoxOptions();
options.setProfile(profile);
driver = new RemoteWebDriver(options);
  {{< / code-panel >}}
  {{< code-panel language="python" >}}
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
options=Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
var options = new FirefoxOptions();
var profile = new FirefoxProfile();
options.Profile = profile;
var driver = new RemoteWebDriver(options);
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
profile = Selenium::WebDriver::Firefox::Profile.new
profile['browser.download.dir'] = "/tmp/webdriver-downloads"
options = Selenium::WebDriver::Firefox::Options.new(profile: profile)
driver = Selenium::WebDriver.for :firefox, options: options
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
const { Builder } = require("selenium-webdriver");
const firefox = require('selenium-webdriver/firefox');

const options = new firefox.Options();
let profile = '/path to custom profile';
options.setProfile(profile);
const driver = new Builder()
    .forBrowser('firefox')
    .setFirefoxOptions(options)
    .build();
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
val options = FirefoxOptions()
options.profile = FirefoxProfile()
driver = RemoteWebDriver(options)
  {{< / code-panel >}}
{{< / code-tab >}}

## Internet Explorer

### fileUploadDialogTimeout

In some environments, Internet Explorer may timeout when opening the
File Upload dialog. IEDriver has a default timeout of 1000ms, but you
can increase the timeout using the fileUploadDialogTimeout capability.

{{< code-tab >}}
  {{< code-panel language="java" >}}
InternetExplorerOptions options = new InternetExplorerOptions();
options.waitForUploadDialogUpTo(Duration.ofSeconds(2));
WebDriver driver = new RemoteWebDriver(options);
  {{< / code-panel >}}
  {{< code-panel language="python" >}}
options = webdriver.IeOptions
options.file_upload_dialog_timeout(2000)
driver = webdriver.Ie(ie_driver_path, options=options)
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
var options = new InternetExplorerOptions();
options.FileUploadDialogTimeout = TimeSpan.FromMilliseconds(2000);
var driver = new RemoteWebDriver(options);
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
options = Selenium::WebDriver::IE::Options.new
options.file_upload_dialog_timeout = 2000
driver = Selenium::WebDriver.for(:ie, options: options)
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
// We don't have a JavaScript code sample yet -  Help us out and raise a PR  
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
val options = InternetExplorerOptions()
options.waitForUploadDialogUpTo(Duration.ofSeconds(2))
val driver = RemoteWebDriver(options)
  {{< / code-panel >}}
{{< / code-tab >}}
