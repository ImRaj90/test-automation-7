---
title: "Overview"
linkTitle: "Overview"
weight: 1
description: >
  Is Selenium for you? See an overview of the different project components.
aliases: ["/documentation/ko/introduction/"]
---

{{% pageinfo color="warning" %}}
<p class="lead">
   <i class="fas fa-language display-4"></i> 
   Page being translated from 
   English to Korean. Do you speak Korean? Help us to translate
   it by sending us pull requests!
</p>
{{% /pageinfo %}}

셀레니움은 하나의 도구(tool)나 API가 아닌, 여러 도구들로 구성되어 있습니다.

## 웹 드라이버(WebDriver)

컴퓨터나 모바일 웹사이트 테스트를 자동화하는 것부터 시작하신다면,
아마 웹 드라이버 APIs부터 쓰게 될 겁니다.  [웹 드라이버]({{< ref "/webdriver.md" >}})
는 브라우저를 조종하고 테스트를 진행할 수 있도록 제작사에서 제공하는 브라우저 자동화 API를 사용합니다.
이는 진짜 사용자가 브라우저를 이용하는 것과 유사합니다.
웹 드라이버 API를 애플리케이션의 코드로 컴파일할 필요가 없기 때문에, 독립적으로 작동합니다.

더 나아가, 실시간으로 사용하는 것처럼 애플리케이션을 테스트합니다.

## 통합개발환경 (IDE)

[통합 개발 환경](https://selenium.dev/selenium-ide) (IDE, Integrated Development Environment) 
은 자신만의 셀레니움 테스트 케이스를 개발하기 위해 사용할 도구입니다.
크롬이나 파이어폭스 확장으로 사용하기 쉽고, 이는 보통 테스트 케이스를 개발하는데 가장 효율적인 방법이기도 
합니다.
이 도구는 여러분을 위해 브라우저 상에서 사용자의 행동을 수집합니다.
기존의 셀레니움 커맨드를 이용해서, 각 요소의 문맥에 따라 정의된 매개변수로 말이죠.
이는 시간을 절약해줄 뿐만 아니라 셀레니움 스크립트 문법을 배우는데 최고의 방법입니다.

## 조합 격자 (Grid)

Selenium 그리드를 사용하면 여러 플랫폼에 걸쳐 서로 다른 컴퓨터에서 테스트 케이스를 실행할 수 있습니다. 
테스트 케이스의 트리거 제어는 로컬 엔드에 있으며, 테스트 케이스가 트리거되면 원격 엔드에 의해 자동으로 실행됩니다.

웹 드라이버 테스트가 개발된 후, 여러 브라우저와 운영 체제 조합에서 테스트를 실행해야 할 수도 있습니다.  
[여기]({{< ref "/grid.md" >}})서 그리드가 나타납니다.
