/**
 * 文档站 → 主站：按当前文档语言（/zh、/en）同步 logo 与官网链接。
 * Mintlify 会自动加载仓库根目录下的 .js 文件。
 */
(function () {
  var MAIN_ORIGIN = "https://www.sunnymeteo.com";
  var LOCALE_COOKIE = "sunnymeteo_locale";
  var patched = new WeakSet();

  function docsLocale() {
    var path = window.location.pathname || "/";
    if (path === "/en" || path.indexOf("/en/") === 0) return "en";
    if (path === "/zh" || path.indexOf("/zh/") === 0) return "zh";
    return "zh";
  }

  function mainSiteHome(locale) {
    return MAIN_ORIGIN + "/" + locale + "/";
  }

  function setLocaleCookie(locale) {
    try {
      document.cookie =
        LOCALE_COOKIE +
        "=" +
        locale +
        "; path=/; domain=.sunnymeteo.com; max-age=31536000; SameSite=Lax";
    } catch (_) {
      /* ignore */
    }
  }

  function patchAnchor(anchor, home, locale) {
    if (!anchor || patched.has(anchor)) return;
    if (anchor.hostname && anchor.hostname !== "www.sunnymeteo.com") return;

    var path = anchor.pathname || "/";
    if (path !== "/" && path !== "/zh/" && path !== "/en/" && path !== "/zh" && path !== "/en") {
      return;
    }

    anchor.href = home;
    patched.add(anchor);

    if (anchor.closest("nav-logo")) {
      anchor.setAttribute(
        "aria-label",
        locale === "zh" ? "返回小晴天科技官网" : "Back to SunnyMeteo website",
      );
    }
  }

  function patchLinks() {
    var locale = docsLocale();
    var home = mainSiteHome(locale);
    setLocaleCookie(locale);

    document.querySelectorAll("nav-logo a").forEach(function (anchor) {
      patchAnchor(anchor, home, locale);
    });

    document.querySelectorAll(
      '#footer a[href*="www.sunnymeteo.com"], footer a[href*="www.sunnymeteo.com"], .nav-anchor a[href*="www.sunnymeteo.com"], navbar-link a[href*="www.sunnymeteo.com"]',
    ).forEach(function (anchor) {
      patchAnchor(anchor, home, locale);
    });
  }

  function run() {
    patchLinks();
    var timer;
    var observer = new MutationObserver(function () {
      clearTimeout(timer);
      timer = setTimeout(patchLinks, 50);
    });
    observer.observe(document.documentElement, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
