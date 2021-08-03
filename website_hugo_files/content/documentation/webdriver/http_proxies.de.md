---
title: "Http Proxies"
linkTitle: "Http Proxies"
weight: 7
---

Ein Proxy-Server fungiert als Zwischenstation für Anfragen zwischen
Client und Server. Simpel erklärt werden die Daten über den Proxy zu der
gewünschten Internetadresse und wieder retour geleitet.

Ein Proxy Server für die automatisierten Selenium-Skripte kann hilfreich 
sein bei:
- Aufzeichnen des Netzwerkverkehrs
- Mocken von Backend-Aufrufen die von der Website abgesetzt werden
- Zugriff auf die gewünschte Website unter komplexen Netzwerkbedingungen oder 
strengen Einschränkungen.

Hat man Probleme bei der Verbindung zu einer URL aus einem Unternehmensnetzwerk, 
deutet das meistens darauf hin, dass es notwendig ist die Verbindung über
einen Proxy herzustellen.

Der Selenium WebDriver stellt die Möglichkeit zur Verfügung um
Proxyeinstellungen vorzunehmen:

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}
import org.openqa.selenium.Proxy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class proxyTest {
  public static void main(String[] args) {
    Proxy proxy = new Proxy();
    proxy.setHttpProxy("<HOST:PORT>");
    ChromeOptions options = new ChromeOptions();
    options.setCapability("proxy", proxy);
    WebDriver driver = new ChromeDriver(options);
    driver.get("https://www.google.com/");
    driver.manage().window().maximize();
    driver.quit();
  }
}
  {{< /tab >}}
  {{< tab header="Python" >}}
from selenium import webdriver

PROXY = "<HOST:PORT>"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://selenium.dev")

  {{< /tab >}}
  {{< tab header="CSharp" >}}
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

public class ProxyTest{
  public static void Main() {
    ChromeOptions options = new ChromeOptions();
    Proxy proxy = new Proxy();
    proxy.Kind = ProxyKind.Manual;
    proxy.IsAutoDetect = false;
    proxy.SslProxy = "<HOST:PORT>";
    options.Proxy = proxy;
    options.AddArgument("ignore-certificate-errors");
    IWebDriver driver = new ChromeDriver(options);
    driver.Navigate().GoToUrl("https://www.selenium.dev/");
  }
}
  {{< /tab >}}
  {{< tab header="Ruby" >}}
# this code was written with Selenium 4

proxy = Selenium::WebDriver::Proxy.new(http: '<HOST:PORT>')
cap   = Selenium::WebDriver::Remote::Capabilities.chrome(proxy: proxy)

driver = Selenium::WebDriver.for(:chrome, capabilities: cap)
driver.get('http://google.com')
  {{< /tab >}}
  {{< tab header="JavaScript" >}}
let webdriver = require('selenium-webdriver');
let chrome = require('selenium-webdriver/chrome');
let proxy = require('selenium-webdriver/proxy');
let opts = new chrome.Options();

(async function example() {
  opts.setProxy(proxy.manual({http: '<HOST:PORT>'}));
  let driver = new webdriver.Builder()
    .forBrowser('chrome')
    .setChromeOptions(opts)
    .build();
  try {
    await driver.get("https://selenium.dev");
  }
  finally {
   await driver.quit();
  }
}());
  {{< /tab >}}
  {{< tab header="Kotlin" >}}
import org.openqa.selenium.Proxy
import org.openqa.selenium.WebDriver
import org.openqa.selenium.chrome.ChromeDriver
import org.openqa.selenium.chrome.ChromeOptions

class proxyTest {
    fun main() {

        val proxy = Proxy()
        proxy.setHttpProxy("<HOST:PORT>")
        val options = ChromeOptions()
        options.setCapability("proxy", proxy)
        val driver: WebDriver = ChromeDriver(options)
        driver["https://www.google.com/"]
        driver.manage().window().maximize()
        driver.quit()
    }
}
  {{< /tab >}}
{{< /tabpane >}}
