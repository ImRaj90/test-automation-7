---
title: "クッキーの使用"
weight: 6
---


Cookieは、Webサイトから送信され、コンピューターに保存される小さなデータです。
Cookieは、主にユーザーを認識し、保存されている情報を読み込むために使用されます。

WebDriver APIは、組み込みメソッドでCookieと対話するメソッドを提供します。

## クッキーの追加
現在のブラウジングコンテキストにCookieを追加するために使用されます。
Cookieの追加では、一連の定義済みのシリアル化可能なJSONオブジェクトのみを受け入れます。
受け入れられたJSONキー値のリストへのリンクは<a href="https://www.w3.org/TR/webdriver1/#cookies">こちら</a>にあります。

まず、Cookieが有効になるドメインにいる必要があります。
サイトとの対話を開始する前にCookieを事前設定しようとしていて、ホームページが大きい場合/代替の読み込みに時間がかかる場合は、サイトで小さいページを見つけることです。（通常、たとえば http://example.com/some404page のような、404ページは小さいです。）

{{< code-tab >}}
  {{< code-panel language="java" >}}
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;

public class addCookie {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("http://www.example.com");

            // Adds the cookie into current browser context
            driver.manage().addCookie(new Cookie("key", "value"));
        } finally {
            driver.quit();
        }
    }
}
  {{< / code-panel >}}
{{< code-panel language="python" >}}
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "key", "value": "value"})
  {{< / code-panel >}}
{{< code-panel language="csharp" >}}
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace AddCookie {
 class AddCookie {
  public static void Main(string[] args) {
   IWebDriver driver = new ChromeDriver();
   try {
    // Navigate to Url
    driver.Navigate().GoToUrl("https://example.com");

    // Adds the cookie into current browser context
    driver.Manage().Cookies.AddCookie(new Cookie("key", "value"));
   } finally {
    driver.Quit();
   }
  }
 }
}
  {{< / code-panel >}}
{{< code-panel language="ruby" >}}
require 'selenium-webdriver'
driver = Selenium::WebDriver.for :chrome

begin
  driver.get 'https://www.example.com'
  
  # Adds the cookie into current browser context
  driver.manage.add_cookie(name: "key", value: "value")
ensure
  driver.quit
end
  {{< / code-panel >}}
{{< code-panel language="javascript" >}}
const {Builder} = require('selenium-webdriver');
(async function example() {
    let driver = new Builder()
        .forBrowser('chrome')
        .build();

    await driver.get('https://www.example.com');

    // set a cookie on the current domain
    await driver.manage().addCookie({name:'key', value: 'value'});
})();
  {{< / code-panel >}}
{{< code-panel language="kotlin" >}}
import org.openqa.selenium.Cookie
import org.openqa.selenium.chrome.ChromeDriver

fun main() {
    val driver = ChromeDriver()
    try {
        driver.get("https://example.com")

        // Adds the cookie into current browser context
        driver.manage().addCookie(Cookie("key", "value"))
    } finally {
        driver.quit()
    }
}  
  {{< / code-panel >}}
{{< / code-tab >}}

## 命名されたクッキーの取得

関連付けられているすべてのCookieの中で、Cookie名と一致するシリアル化されたCookieデータを返します。

{{< code-tab >}}
  {{< code-panel language="java" >}}
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;

public class getCookieNamed {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("http://www.example.com");
            driver.manage().addCookie(new Cookie("foo", "bar"));

            // Get cookie details with named cookie 'foo'
            Cookie cookie1 = driver.manage().getCookieNamed("foo");
            System.out.println(cookie1);
        } finally {
            driver.quit();
        }
    }
}
  {{< / code-panel >}}
 {{< code-panel language="python" >}}
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

# Adds the cookie into current browser context
driver.add_cookie({"name": "foo", "value": "bar"})

# Get cookie details with named cookie 'foo'
print(driver.get_cookie("foo"))
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace GetCookieNamed {
 class GetCookieNamed {
  public static void Main(string[] args) {
   IWebDriver driver = new ChromeDriver();
   try {
    // Navigate to Url
    driver.Navigate().GoToUrl("https://example.com");
    driver.Manage().Cookies.AddCookie(new Cookie("foo", "bar"));

    // Get cookie details with named cookie 'foo'
    var cookie = driver.Manage().Cookies.GetCookieNamed("foo");
    System.Console.WriteLine(cookie);
   } finally {
    driver.Quit();
   }
  }
 }
}
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
require 'selenium-webdriver'
driver = Selenium::WebDriver.for :chrome

begin
  driver.get 'https://www.example.com'
  driver.manage.add_cookie(name: "foo", value: "bar")

  # Get cookie details with named cookie 'foo'
  puts driver.manage.cookie_named('foo')
ensure
  driver.quit
end
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
const {Builder} = require('selenium-webdriver');
(async function example() {
    let driver = new Builder()
        .forBrowser('chrome')
        .build();

    await driver.get('https://www.example.com');

    // set a cookie on the current domain
    await driver.manage().addCookie({name:'foo', value: 'bar'});

    // Get cookie details with named cookie 'foo' 
    driver.manage().getCookie('foo').then(function (cookie) {
        console.log('cookie details => ', cookie);
    });
})();
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
import org.openqa.selenium.Cookie
import org.openqa.selenium.chrome.ChromeDriver

fun main() {
    val driver = ChromeDriver()
    try {
        driver.get("https://example.com")
        driver.manage().addCookie(Cookie("foo", "bar"))

        // Get cookie details with named cookie 'foo'
        val cookie = driver.manage().getCookieNamed("foo")
        println(cookie)
    } finally {
        driver.quit()
    }
}  
  {{< / code-panel >}}
{{< / code-tab >}}

## 全てのクッキーの取得

現在のブラウジングコンテキストの '成功したシリアル化されたCookieデータ' を返します。
ブラウザが使用できなくなった場合、エラーが返されます。

{{< code-tab >}}
  {{< code-panel language="java" >}}
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.Set;

public class getAllCookies {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("http://www.example.com");
            // Add few cookies
            driver.manage().addCookie(new Cookie("test1", "cookie1"));
            driver.manage().addCookie(new Cookie("test2", "cookie2"));

            // Get All available cookies
            Set<Cookie> cookies = driver.manage().getCookies();
            System.out.println(cookies);
        } finally {
            driver.quit();
        }
    }
}
  {{< / code-panel >}}
 {{< code-panel language="python" >}}
from selenium import webdriver

driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")

driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Get all available cookies
print(driver.get_cookies())
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace GetAllCookies {
 class GetAllCookies {
  public static void Main(string[] args) {
   IWebDriver driver = new ChromeDriver();
   try {
    // Navigate to Url
    driver.Navigate().GoToUrl("https://example.com");
    driver.Manage().Cookies.AddCookie(new Cookie("test1", "cookie1"));
    driver.Manage().Cookies.AddCookie(new Cookie("test2", "cookie2"));

    // Get All available cookies
    var cookies = driver.Manage().Cookies.AllCookies;
   } finally {
    driver.Quit();
   }
  }
 }
}
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
require 'selenium-webdriver'
driver = Selenium::WebDriver.for :chrome

begin
  driver.get 'https://www.example.com'
  driver.manage.add_cookie(name: "test1", value: "cookie1")
  driver.manage.add_cookie(name: "test2", value: "cookie2")

  # Get all available cookies
  puts driver.manage.all_cookies
ensure
  driver.quit
end
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
const {Builder} = require('selenium-webdriver');
(async function example() {
    let driver = new Builder()
        .forBrowser('chrome')
        .build();

    await driver.get('https://www.example.com');

    // Add few cookies
    await driver.manage().addCookie({name:'test1', value:'cookie1'});
    await driver.manage().addCookie({name:'test2', value:'cookie2'});

    // Get all Available cookies
    driver.manage().getCookies().then(function (cookies) {
        console.log('cookie details => ', cookies);
    });
})();
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
import org.openqa.selenium.Cookie
import org.openqa.selenium.chrome.ChromeDriver

fun main() {
    val driver = ChromeDriver()
    try {
        driver.get("https://example.com")
        driver.manage().addCookie(Cookie("test1", "cookie1"))
        driver.manage().addCookie(Cookie("test2", "cookie2"))

        // Get All available cookies
        val cookies = driver.manage().cookies
        println(cookies)
    } finally {
        driver.quit()
    }
}  
  {{< / code-panel >}}
{{< / code-tab >}}


## クッキーの削除

指定されたCookie名と一致するCookieデータを削除します。

{{< code-tab >}}
  {{< code-panel language="java" >}}
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;

public class deleteCookie {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("http://www.example.com");
            driver.manage().addCookie(new Cookie("test1", "cookie1"));
            Cookie cookie1 = new Cookie("test2", "cookie2");
            driver.manage().addCookie(cookie1);

            // delete a cookie with name 'test1'
            driver.manage().deleteCookieNamed("test1");

            /*
             Selenium Java bindings also provides a way to delete
             cookie by passing cookie object of current browsing context
             */
            driver.manage().deleteCookie(cookie1);
        } finally {
            driver.quit();
        }
    }
}
  {{< / code-panel >}}
 {{< code-panel language="python" >}}
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# Delete a cookie with name 'test1'
driver.delete_cookie("test1")
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace DeleteCookie {
 class DeleteCookie {
  public static void Main(string[] args) {
   IWebDriver driver = new ChromeDriver();
   try {
    // Navigate to Url
    driver.Navigate().GoToUrl("https://example.com");
    driver.Manage().Cookies.AddCookie(new Cookie("test1", "cookie1"));
    var cookie = new Cookie("test2", "cookie2");
    driver.Manage().Cookies.AddCookie(cookie);

    // delete a cookie with name 'test1'	
    driver.Manage().Cookies.DeleteCookieNamed("test1");

    // Selenium .net bindings also provides a way to delete
    // cookie by passing cookie object of current browsing context
    driver.Manage().Cookies.DeleteCookie(cookie);
   } finally {
    driver.Quit();
   }
  }
 }
}
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
require 'selenium-webdriver'
driver = Selenium::WebDriver.for :chrome

begin
  driver.get 'https://www.example.com'
  driver.manage.add_cookie(name: "test1", value: "cookie1")
  driver.manage.add_cookie(name: "test2", value: "cookie2")

  # delete a cookie with name 'test1'
  driver.manage.delete_cookie('test1')
ensure
  driver.quit
end
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
const {Builder} = require('selenium-webdriver');
(async function example() {
    let driver = new Builder()
        .forBrowser('chrome')
        .build();

    await driver.get('https://www.example.com');

    // Add few cookies
    await driver.manage().addCookie({name:'test1', value:'cookie1'});
    await driver.manage().addCookie({name:'test2', value:'cookie2'});

    // Delete a cookie with name 'test1'
    await driver.manage().deleteCookie('test1');
    
    // Get all Available cookies
    driver.manage().getCookies().then(function (cookies) {
        console.log('cookie details => ', cookies);
    });
})();
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
import org.openqa.selenium.Cookie
import org.openqa.selenium.chrome.ChromeDriver

fun main() {
    val driver = ChromeDriver()
    try {
        driver.get("https://example.com")
        driver.manage().addCookie(Cookie("test1", "cookie1"))
        val cookie1 = Cookie("test2", "cookie2")
        driver.manage().addCookie(cookie1)

        // delete a cookie with name 'test1'
        driver.manage().deleteCookieNamed("test1")

        // delete cookie by passing cookie object of current browsing context.
        driver.manage().deleteCookie(cookie1)
    } finally {
        driver.quit()
    }
}  
  {{< / code-panel >}}
{{< / code-tab >}}


## 全てのクッキーの削除

現在のブラウジングコンテキストの全てのCookieを削除します。

{{< code-tab >}}
  {{< code-panel language="java" >}}
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;

public class deleteAllCookies {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("http://www.example.com");
            driver.manage().addCookie(new Cookie("test1", "cookie1"));
            driver.manage().addCookie(new Cookie("test2", "cookie2"));

            // deletes all cookies
            driver.manage().deleteAllCookies();
        } finally {
            driver.quit();
        }
    }
}
  {{< / code-panel >}}
 {{< code-panel language="python" >}}
from selenium import webdriver
driver = webdriver.Chrome()

# Navigate to url
driver.get("http://www.example.com")
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

#  Deletes all cookies
driver.delete_all_cookies()
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace DeleteAllCookies {
 class DeleteAllCookies {
  public static void Main(string[] args) {
   IWebDriver driver = new ChromeDriver();
   try {
    // Navigate to Url
    driver.Navigate().GoToUrl("https://example.com");
    driver.Manage().Cookies.AddCookie(new Cookie("test1", "cookie1"));
    driver.Manage().Cookies.AddCookie(new Cookie("test2", "cookie2"));

    // deletes all cookies
    driver.Manage().Cookies.DeleteAllCookies();
   } finally {
    driver.Quit();
   }
  }
 }
}
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
require 'selenium-webdriver'
driver = Selenium::WebDriver.for :chrome

begin
  driver.get 'https://www.example.com'
  driver.manage.add_cookie(name: "test1", value: "cookie1")
  driver.manage.add_cookie(name: "test2", value: "cookie2")

  # deletes all cookies
  driver.manage.delete_all_cookies
ensure
  driver.quit
end
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
const {Builder} = require('selenium-webdriver');
(async function example() {
    let driver = new Builder()
        .forBrowser('chrome')
        .build();

    await driver.get('https://www.example.com');

    // Add few cookies
    await driver.manage().addCookie({name:'test1', value:'cookie1'});
    await driver.manage().addCookie({name:'test2', value:'cookie2'});

    // Delete all cookies
    await driver.manage().deleteAllCookies();
})();
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
import org.openqa.selenium.Cookie
import org.openqa.selenium.chrome.ChromeDriver

fun main() {
    val driver = ChromeDriver()
    try {
        driver.get("https://example.com")
        driver.manage().addCookie(Cookie("test1", "cookie1"))
        driver.manage().addCookie(Cookie("test2", "cookie2"))

        // deletes all cookies
        driver.manage().deleteAllCookies()
    } finally {
        driver.quit()
    }
}  
  {{< / code-panel >}}
{{< / code-tab >}}

## SameSite Cookie属性

これにより、ユーザーは、サードパーティのサイトによって開始されたリクエストとともに
Cookieを送信するかどうかをブラウザに指示できます。
CSRF（クロスサイトリクエストフォージェリ）攻撃を防ぐために導入されました。

SameSite Cookie属性は、2つのパラメーターを命令として受け入れます。

## Strict:
SameSite属性が **Strict** に設定されている場合、CookieはサードパーティのWebサイトによって
開始されたリクエストとともに送信されません。

## Lax:
CookieのSameSite属性を **Lax** に設定すると、CookieはサードパーティのWebサイトによって
開始されたGETリクエストとともに送信されます。

**Note**: **As of now this feature is landed in chrome(80+version), 
Firefox(79+version) and works with Selenium 4 and later versions.**

{{< code-tab >}}
  {{< code-panel language="java" >}}
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;

public class cookieTest {
  public static void main(String[] args) {
    WebDriver driver = new ChromeDriver();
    try {
      driver.get("http://www.example.com");
      Cookie cookie = new Cookie.Builder("key", "value").sameSite("Strict").build();
      Cookie cookie1 = new Cookie.Builder("key", "value").sameSite("Lax").build();
      driver.manage().addCookie(cookie);
      driver.manage().addCookie(cookie1);
      System.out.println(cookie.getSameSite());
      System.out.println(cookie1.getSameSite());
    } finally {
      driver.quit();
    }
  }
}
  {{< / code-panel >}}
 {{< code-panel language="python" >}}
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.example.com")
# Adds the cookie into current browser context with sameSite 'Strict' (or) 'Lax'
driver.add_cookie({"name": "foo", "value": "value", 'sameSite': 'Strict'})
driver.add_cookie({"name": "foo1", "value": "value", 'sameSite': 'Lax'})
cookie1 = driver.get_cookie('foo')
cookie2 = driver.get_cookie('foo1')
print(cookie1)
print(cookie2)
  {{< / code-panel >}}
  {{< code-panel language="csharp" >}}
// Please raise a PR
  {{< / code-panel >}}
  {{< code-panel language="ruby" >}}
require 'selenium-webdriver'
driver = Selenium::WebDriver.for :chrome

begin
  driver.get 'https://www.example.com'
  # Adds the cookie into current browser context with sameSite 'Strict' (or) 'Lax'
  driver.manage.add_cookie(name: "foo", value: "bar", same_site: "Strict")
  driver.manage.add_cookie(name: "foo1", value: "bar", same_site: "Lax")
  puts driver.manage.cookie_named('foo')
  puts driver.manage.cookie_named('foo1')
ensure
  driver.quit
end
  {{< / code-panel >}}
  {{< code-panel language="javascript" >}}
const {Builder} = require('selenium-webdriver');
(async function example() {
    let driver = new Builder()
        .forBrowser('chrome')
        .build();
        
    await driver.get('https://www.example.com');
    
    // set a cookie on the current domain with sameSite 'Strict' (or) 'Lax'
    await driver.manage().addCookie({name:'key', value: 'value', sameSite:'Strict'});
    await driver.manage().addCookie({name:'key', value: 'value', sameSite:'Lax'});
    console.log(await driver.manage().getCookie('key'));
})();
  {{< / code-panel >}}
  {{< code-panel language="kotlin" >}}
import org.openqa.selenium.Cookie
import org.openqa.selenium.chrome.ChromeDriver

fun main() {
    val driver = ChromeDriver()
    try {
        driver.get("http://www.example.com")
        val cookie = Cookie.Builder("key", "value").sameSite("Strict").build()
        val cookie1 = Cookie.Builder("key", "value").sameSite("Lax").build()
        driver.manage().addCookie(cookie)
        driver.manage().addCookie(cookie1)
        println(cookie.getSameSite())
        println(cookie1.getSameSite())
    } finally {
        driver.quit()
    }
} 
  {{< / code-panel >}}
{{< / code-tab >}}
