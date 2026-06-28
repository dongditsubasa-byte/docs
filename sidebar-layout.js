/**
 * 修正 Mintlify mint 主题侧栏：一级加粗、箭头右对齐、行距。
 * DOM: #sidebar-content ul.sidebar-group > li > button / ul > li > a
 */
(function () {
  var L1_SELECTOR = "#sidebar-content ul.sidebar-group > li > button";
  var L2_SELECTOR = "#sidebar-content ul.sidebar-group > li > ul > li > a";

  function patchLevel1Button(button) {
    if (!button) return;

    button.style.setProperty("display", "flex", "important");
    button.style.setProperty("align-items", "center", "important");
    button.style.setProperty("justify-content", "space-between", "important");
    button.style.setProperty("width", "100%", "important");
    button.style.setProperty("box-sizing", "border-box", "important");
    button.style.setProperty("padding-top", "6px", "important");
    button.style.setProperty("padding-bottom", "6px", "important");
    button.style.setProperty("padding-right", "0", "important");
    button.style.setProperty("margin", "0", "important");
    button.style.setProperty("color", "#64748b", "important");
    button.style.setProperty("font-size", "16px", "important");
    button.style.setProperty("font-weight", "700", "important");
    button.style.setProperty("line-height", "20px", "important");
    button.style.setProperty("min-height", "unset", "important");

    button.querySelectorAll("span").forEach(function (node) {
      node.style.setProperty("font-weight", "700", "important");
      node.style.setProperty("color", "#64748b", "important");
      node.style.setProperty(
        "text-shadow",
        "-0.2px 0 0 currentColor, 0.2px 0 0 currentColor",
        "important",
      );
    });

    var iconWrap = button.querySelector(":scope > div:last-child");
    if (iconWrap) {
      iconWrap.style.setProperty("margin-left", "auto", "important");
      iconWrap.style.setProperty("flex-shrink", "0", "important");
    }
  }

  function patchLevel2Links() {
    document.querySelectorAll(L2_SELECTOR).forEach(function (link) {
      link.style.setProperty("display", "block", "important");
      link.style.setProperty("font-size", "16px", "important");
      link.style.setProperty("line-height", "18px", "important");
      link.style.setProperty("padding-top", "4px", "important");
      link.style.setProperty("padding-bottom", "4px", "important");
      link.style.setProperty("padding-left", "0.5rem", "important");
      link.style.setProperty("color", "#7b8a9a", "important");
      link.style.setProperty("min-height", "unset", "important");
    });
  }

  function patchSidebar() {
    document.querySelectorAll(L1_SELECTOR).forEach(patchLevel1Button);
    patchLevel2Links();
  }

  function run() {
    patchSidebar();
    var timer;
    new MutationObserver(function () {
      clearTimeout(timer);
      timer = setTimeout(patchSidebar, 40);
    }).observe(document.getElementById("sidebar-content") || document.documentElement, {
      childList: true,
      subtree: true,
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
