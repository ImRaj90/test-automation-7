<!-- Upstream docsy commit — ecd4be87ea48e8e94684e32c925049e9bdf7f127-->
var tabContents = document.querySelectorAll('.tab-content.persist');
if (tabContents.length > 1) {
    const persistTab = document.querySelector('ul.persist').querySelectorAll('.nav-link');
    var heightMap = {};

    // select each persist tab and store calculated heights
    persistTab.forEach((langTab) => {
        langTab.click();
        tabContents.forEach((tabContent) => {
            heightMap[tabContent.id] ||= [];
            heightMap[tabContent.id].push(tabContent.clientHeight);
        })
        // everything ends up active unless classes removed
        document.querySelectorAll('.active.show').forEach((activeTab) => {
            activeTab.classList.remove('active');
            activeTab.classList.remove('show');
        })
    })
    // need to make something active/shown again
    persistTab[0].click();

    tabContents.forEach((tabContent) => {
        tabContent.style.height = Math.max.apply(Math, heightMap[tabContent.id]).toString() + 'px';
    })
}

if (typeof Storage !== 'undefined') {
    let activeLanguage = localStorage.getItem('active_language');

    // Get active language from URL params if exists
    const params = new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
    });
    if (params.language !== null) {
        activeLanguage = params.language;
        localStorage.setItem('active_language', activeLanguage);
    }
    if (activeLanguage) {
        document
            .querySelectorAll('.persistLang-' + activeLanguage)
            .forEach((element) => {
              $('#' + element.id).tab('show');
            });
    }
}
function persistLang(language) {
    if (typeof Storage !== 'undefined') {
        localStorage.setItem('active_language', language);
        document.querySelectorAll('.persistLang-' + language)
          .forEach((element) => {
            $('#' + element.id).tab('show');
        });
    }
}
