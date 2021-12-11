---
title: "Install a Selenium library"
linkTitle: "Install Library"
weight: 1
description: >
  Setting up the Selenium library for your favourite programming language.
aliases: [
"/documentation/en/selenium_installation/installing_selenium_libraries/",
"/documentation/getting_started/installing_selenium_libraries/"
]
---

The installation process for libraries depends on the language you choose to use:

{{< tabpane-md  paneID="2" tabCount="6" headerTab1="Java" headerTab2="Python" headerTab3="CSharp" headerTab4="Ruby" headerTab5="JavaScript" headerTab6="Kotlin" >}}
{{< tab-md ID="1" >}}
Installation of Selenium libraries for Java is accomplished using a build tool.
You can find the latest version on [Selenium Downloads](/downloads/) and see all available versions on
[Maven Repository](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java)

For Maven, add the _selenium-java_ dependency in your project `pom.xml` file:

```xml
<dependency>
  <groupId>org.seleniumhq.selenium</groupId>
  <artifactId>selenium-java</artifactId>
  <version>4.0.0</version>
</dependency>
```

For Gradle, add the _selenium-java_ dependency in your project `build.gradle` file:

```text
dependencies {
    compile group: 'org.seleniumhq.selenium', name: 'selenium-java', version: '4.0.0'
```
{{< /tab-md >}}
{{< tab-md ID="2" >}}
Installation of Selenium libraries for Python can be done using pip:

```shell
pip install selenium
```

Alternatively you can download the [PyPI source archive](https://pypi.org/project/selenium/#files)
(selenium-x.x.x.tar.gz) and install it using _setup.py_:

```shell
python setup.py install
```

{{< /tab-md >}}
{{< tab-md ID="3" >}}
Installation of Selenium libraries for C# can be done using NuGet:

```shell
# Using package manager
Install-Package Selenium.WebDriver
# or using .Net CLI
dotnet add package Selenium.WebDriver
```
{{< /tab-md >}}
{{< tab-md ID="4" >}}
Installation of Selenium libraries for Ruby can be done using gem:

```shell
gem install selenium-webdriver
```

Or add it to your `Gemfile`:

```rb
gem 'selenium-webdriver', '~> 4.0'
```

{{< /tab-md >}}
{{< tab-md ID="5" >}}
Installation of Selenium libraries for JavaScript can be done using npm:

```shell
npm install selenium-webdriver
```

{{< /tab-md >}}
{{< tab-md ID="6" >}}
Due to missing native language bindings for Kotlin, you have to use the
Java Bindings, e.g. with maven [Java](#java)
{{< /tab-md >}}
{{< /tabpane-md >}}
