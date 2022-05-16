---
title: "最初のSeleniumスクリプトを書く"
linkTitle: "最初のスクリプト"
weight: 8
needsTranslation: true
description: >
    Seleniumスクリプトを作成するための段階的な説明
---

[Seleniumをインストール]({{< ref "install_library.md" >}})し、
[ドライバーをインストール]({{< ref "install_drivers.md" >}})すると、Seleniumコードを書く準備が整います。

## Eight Basic Components

Seleniumが行うことはすべて、ブラウザコマンドを送信して、何かを実行したり、情報の要求を送信したりすることです。 
Seleniumで行うことのほとんどは、次の基本的なコマンドの組み合わせです。

### 1. ドライバーインスタンスでセッションを開始します

For more details on starting a session read our documentation on [opening and closing a browser]({{< ref "open_browser.md" >}})

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L17" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L6" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L15" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L5" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L5" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L17" >}}
    {{< /tab >}}
{{< /tabpane >}}

### 2. Take action on browser
In this example we are ブラウザが[ナビゲート]({{< ref "/documentation/webdriver/browser/navigation.md" >}})するコマンドを送信します

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L19" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L8" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L17" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L7" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L7" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L19" >}}
    {{< /tab >}}
{{< /tabpane >}}

### 3. [ブラウザに関する情報]({{< ref "/documentation/webdriver/browser" >}})をリクエストします

There are a bunch of types of [information about the browser]({{< ref "/documentation/webdriver/browser" >}}) you
can request, including window handles, browser size / position, cookies, alerts, etc.

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L21" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L10" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L19" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L9" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L9" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L21" >}}
    {{< /tab >}}
{{< /tabpane >}}

### 4. Establish Waiting Strategy

Synchronizing the code with the current state of the browser is one of the biggest challenges
with Selenium, and doing it well is an advanced topic.

Essentially you want to make sure that the element is on the page before you attempt to locate it
and the element is in an interactable state before you attempt to interact with it.

An implicit wait is rarely the best solution, but it's the easiest to demonstrate here, so
we'll use it as a placeholder.

Read more about [Waiting strategies]({{< ref "/documentation/webdriver/waits.md" >}}).

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L24" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L13" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L22" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L12" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L11" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L24" >}}
    {{< /tab >}}
{{< /tabpane >}}

### 5. [要素を検索する]({{< ref "/documentation/webdriver/elements" >}})ためのコマンドを送信します
The majority of commands in most Selenium sessions are element related, and you can't interact
with one without first [finding an element]({{< ref "/documentation/webdriver/elements" >}})

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L26-L27" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L15-L16" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L24-L25" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L14-L15" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L13-L14" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L26-L27" >}}
    {{< /tab >}}
{{< /tabpane >}}

### 6. 要素に対してアクションを実行する
There are only a handful of [actions to take on an element]({{< ref "/documentation/webdriver/elements/interactions.md" >}}),
but you will use them frequently. 

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L29-L30" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L18-L19" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L27-L28" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L17-L18" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L16-L17" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L29-L30" >}}
    {{< /tab >}}
{{< /tabpane >}}

### 7. 要素に関する情報をリクエストします
Elements store a lot of [information that can be requested]({{< ref "/documentation/webdriver/elements/information" >}}).
Notice that we need to relocate the search box because the DOM has changed since we first located it.  

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L33" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L22" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L31" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L21" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L20" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L33" >}}
    {{< /tab >}}
{{< /tabpane >}}

### 8. セッションを終了します 

This ends the driver process, which by default closes the browser as well. 
No more commands can be sent to this driver instance. 

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java#L36" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py#L25" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs#L34" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb#L24" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js#L22" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt#L36" >}}
    {{< /tab >}}
{{< /tabpane >}}

## Putting everything together

これらの8つを組み合わせて、使う必要のあるライブラリを含む完全なスクリプトにしましょう。

{{< tabpane disableCodeBlock=true >}}
    {{< tab header="Java" >}}
        {{< gh-codeblock path="examples/java/src/test/java/dev/selenium/getting_started/FirstScriptTest.java" >}}
    {{< /tab >}}
    {{< tab header="Python" >}}
        {{< gh-codeblock path="examples/python/tests/getting_started/test_first_script.py" >}}
    {{< /tab >}}
    {{< tab header="CSharp" >}}
        {{< gh-codeblock path="examples/dotnet/SeleniumDocs/GettingStarted/FirstScriptTest.cs" >}}
    {{< /tab >}}
    {{< tab header="Ruby" >}}
        {{< gh-codeblock path="examples/ruby/spec/getting_started/first_script_spec.rb" >}}
    {{< /tab >}}
    {{< tab header="JavaScript" >}}
        {{< gh-codeblock path="examples/javascript/getting_started/firstScript.js" >}}
    {{< /tab >}}
    {{< tab header="Kotlin" >}}
        {{< gh-codeblock path="examples/kotlin/src/test/kotlin/dev/selenium/getting_started/FirstScriptTest.kt" >}}
    {{< /tab >}}
{{< /tabpane >}}

## Next Steps

Take what you've learned and build out your Selenium code. 

As you find more functionality that you need, read up on the rest of our
[WebDriver documentation]({{< ref "/documentation/webdriver/" >}}).
