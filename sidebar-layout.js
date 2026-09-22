/**
 * Mintlify mint 主题侧栏增强（适配 2026 DOM）：
 * - 一级标题（.sidebar-group-header / h3.sidebar-title）字号与二级一致
 * - 一级右侧下拉箭头，点击展开/折叠，状态写入 localStorage
 *
 * DOM:
 *   #navigation-items > div
 *     > .sidebar-group-header > h3.sidebar-title
 *     > ul.sidebar-group > li > a
 */
(function () {
  var FONT_SIZE = "16px";
  var LINE_HEIGHT = "20px";
  var STORAGE_KEY = "sunnymeteo.sidebar.collapsed.v2";
  var CHEVRON_SVG =
    '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>';

  function loadCollapsed() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}") || {};
    } catch (_) {
      return {};
    }
  }

  function saveCollapsed(map) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(map));
    } catch (_) {
      /* ignore */
    }
  }

  function groupKey(header) {
    var title = header.querySelector(".sidebar-title, h3");
    var label = ((title && title.textContent) || header.textContent || "")
      .replace(/\s+/g, " ")
      .trim();
    return label || "unnamed";
  }

  function sectionRoot(header) {
    return header.parentElement;
  }

  function sectionList(header) {
    var root = sectionRoot(header);
    if (!root) return null;
    return root.querySelector(":scope > ul.sidebar-group");
  }

  function ensureChevron(header) {
    var icon = header.querySelector(":scope > .sm-sidebar-chevron");
    if (!icon) {
      icon = document.createElement("span");
      icon.className = "sm-sidebar-chevron";
      icon.setAttribute("aria-hidden", "true");
      icon.innerHTML = CHEVRON_SVG;
      header.appendChild(icon);
    } else if (!icon.querySelector("svg")) {
      icon.innerHTML = CHEVRON_SVG;
    }
    return icon;
  }

  function styleHeader(header) {
    header.style.setProperty("display", "flex", "important");
    header.style.setProperty("align-items", "center", "important");
    header.style.setProperty("justify-content", "space-between", "important");
    header.style.setProperty("width", "100%", "important");
    header.style.setProperty("cursor", "pointer", "important");
    header.style.setProperty("font-size", FONT_SIZE, "important");
    header.style.setProperty("line-height", LINE_HEIGHT, "important");
    header.style.setProperty("font-weight", "600", "important");
    header.style.setProperty("color", "#64748b", "important");

    header.querySelectorAll(".sidebar-title, .sidebar-title span, h3, h3 span").forEach(function (node) {
      node.style.setProperty("font-size", FONT_SIZE, "important");
      node.style.setProperty("line-height", LINE_HEIGHT, "important");
      node.style.setProperty("font-weight", "600", "important");
      node.style.setProperty("letter-spacing", "normal", "important");
      node.style.setProperty("text-transform", "none", "important");
      node.style.setProperty("color", "#64748b", "important");
      node.style.setProperty("margin", "0", "important");
    });
  }

  function styleLinks(list) {
    if (!list) return;
    list.querySelectorAll(":scope > li > a").forEach(function (link) {
      link.style.setProperty("font-size", FONT_SIZE, "important");
      link.style.setProperty("line-height", LINE_HEIGHT, "important");
      link.querySelectorAll("span").forEach(function (span) {
        span.style.setProperty("font-size", FONT_SIZE, "important");
        span.style.setProperty("line-height", LINE_HEIGHT, "important");
      });
    });
  }

  function setCollapsed(header, collapsed, persist) {
    var root = sectionRoot(header);
    var list = sectionList(header);
    if (!root || !list) return;

    ensureChevron(header);
    root.dataset.smCollapsed = collapsed ? "true" : "false";
    header.setAttribute("aria-expanded", collapsed ? "false" : "true");
    header.setAttribute("role", "button");
    header.tabIndex = 0;

    list.style.setProperty("display", collapsed ? "none" : "", "important");

    if (persist) {
      var map = loadCollapsed();
      map[groupKey(header)] = collapsed;
      saveCollapsed(map);
    }
  }

  function bindHeader(header) {
    styleHeader(header);
    ensureChevron(header);
    styleLinks(sectionList(header));

    var map = loadCollapsed();
    var key = groupKey(header);
    var collapsed = typeof map[key] === "boolean" ? map[key] : false;
    setCollapsed(header, collapsed, false);

    if (header.dataset.smToggleBound) return;
    header.dataset.smToggleBound = "1";

    function toggle(event) {
      event.preventDefault();
      event.stopPropagation();
      var root = sectionRoot(header);
      var next = !(root && root.dataset.smCollapsed === "true");
      setCollapsed(header, next, true);
    }

    header.addEventListener("click", toggle, true);
    header.addEventListener(
      "keydown",
      function (event) {
        if (event.key === "Enter" || event.key === " ") {
          toggle(event);
        }
      },
      true,
    );
  }

  function patchSidebar() {
    var headers = document.querySelectorAll(
      "#sidebar-content #navigation-items .sidebar-group-header",
    );
    headers.forEach(bindHeader);
  }

  function run() {
    patchSidebar();
    var timer;
    var target = document.getElementById("sidebar-content") || document.documentElement;
    new MutationObserver(function () {
      clearTimeout(timer);
      timer = setTimeout(patchSidebar, 40);
    }).observe(target, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
