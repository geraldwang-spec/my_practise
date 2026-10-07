// const sidebar = document.getElementById("sidebar");
// const sidebarToggle = document.getElementById("sidebarToggle");
// const mobileMenuButton = document.getElementById("mobileMenuButton");
const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebarToggle");
const sidebarLogo = document.getElementById("sidebarLogo");
const mobileMenuButton = document.getElementById("mobileMenuButton");

const themeSelect = document.getElementById("themeSelect");
const themeIcon = document.getElementById("themeIcon");
const themeName = document.getElementById("themeName");

const sidebarNav = document.getElementById("sidebarNav");

const topbarEyebrow = document.getElementById("topbarEyebrow");
const topbarPage = document.getElementById("topbarPage");

// 右邊的兩種內容
const chatView = document.getElementById("chat");
const mlView = document.getElementById("ml");
const pageTitle = document.getElementById("pageTitle");
const pageDescription = document.getElementById("pageDescription");
const chatPanelTitle = document.getElementById("chatPanelTitle");

const infoTheme = document.getElementById("infoTheme");
const infoModule = document.getElementById("infoModule");

const chatMessages = document.getElementById("chatMessages");
const chatSuggestions = document.getElementById("suggestions");
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const clearChatButton = document.getElementById("clearChatButton");

let currentTheme = null;
let currentNavigation = null;

/* =========================
   Cursor
========================= */

const cursorDot = document.getElementById("cursor-dot");
const cursorRing = document.getElementById("cursor-ring");

let mouseX = 0;
let mouseY = 0;
let ringX = 0;
let ringY = 0;

if (window.matchMedia("(pointer: fine)").matches) {
  document.addEventListener("mousemove", (event) => {
    mouseX = event.clientX;
    mouseY = event.clientY;

    cursorDot.style.left = `${mouseX}px`;
    cursorDot.style.top = `${mouseY}px`;
  });

  function moveRing() {
    ringX += (mouseX - ringX) * 0.12;
    ringY += (mouseY - ringY) * 0.12;

    cursorRing.style.left = `${ringX}px`;
    cursorRing.style.top = `${ringY}px`;

    requestAnimationFrame(moveRing);
  }

  moveRing();

  document.addEventListener("mouseover", (event) => {
    if (event.target.closest("a, button, select, input")) {
      cursorRing.style.transform =
        "translate(-50%, -50%) scale(2.1)";
      cursorRing.style.borderColor =
        "rgba(255,255,255,0.85)";
      cursorDot.style.opacity = "0.3";
    }
  });

  document.addEventListener("mouseout", (event) => {
    if (event.target.closest("a, button, select, input")) {
      cursorRing.style.transform =
        "translate(-50%, -50%) scale(1)";
      cursorRing.style.borderColor =
        "rgba(255,255,255,0.45)";
      cursorDot.style.opacity = "1";
    }
  });
}

/* =========================
   Initialization
========================= */

function init() {
  renderThemeOptions();

  const savedTheme =
    localStorage.getItem("vora-theme") ||
    APP_CONFIG.defaultTheme;

  const savedCollapsed =
    localStorage.getItem("vora-sidebar-collapsed");

  if (savedCollapsed === "true") {
    sidebar.classList.add("is-collapsed");
  }

  switchTheme(savedTheme);
  bindEvents();
  initReveal();
}

/* =========================
   Theme
========================= */

function renderThemeOptions() {
  themeSelect.innerHTML = "";

  APP_CONFIG.themes.forEach((theme) => {
    const option = document.createElement("option");

    option.value = theme.id;
    option.textContent = theme.name;

    themeSelect.appendChild(option);
  });
}

function switchTheme(themeId) {
  const theme =
    APP_CONFIG.themes.find((item) => item.id === themeId) ||
    APP_CONFIG.themes[0];

  currentTheme = theme;
  currentNavigation = theme.navigation[0];

  themeSelect.value = theme.id;
  themeIcon.textContent = theme.icon;
  themeName.textContent = theme.name;
  infoTheme.textContent = theme.name;
  topbarEyebrow.textContent = `${theme.name} — WORKSPACE`;

  renderNavigation();
  showView();

  localStorage.setItem("vora-theme", theme.id);
}

/* =========================
   Navigation
========================= */

function renderNavigation() {
  sidebarNav.innerHTML = "";

  currentTheme.navigation.forEach((item, index) => {
    const link = document.createElement("a");

    link.href = isMLView() ? "#ml" : "#chat";
    link.dataset.navigationId = item.id;
    link.className = index === 0 ? "active" : "";

    link.innerHTML = `
      <span class="sidebar__nav-icon">${item.icon}</span>

      <span class="sidebar__nav-copy">
        <span class="sidebar__nav-name">${item.name}</span>
        <span class="sidebar__nav-description">${item.description}</span>
      </span>
    `;

    link.addEventListener("click", (event) => {
      event.preventDefault();
      selectNavigation(item.id);

      if (window.innerWidth <= 800) {
        sidebar.classList.remove("is-mobile-open");
      }
    });

    sidebarNav.appendChild(link);
  });
}

function selectNavigation(navigationId) {
  const navigation = currentTheme.navigation.find(
    (item) => item.id === navigationId
  );

  if (!navigation) return;

  currentNavigation = navigation;

  document.querySelectorAll(".sidebar__nav a").forEach((link) => {
    link.classList.toggle(
      "active",
      link.dataset.navigationId === navigationId
    );
  });

  showView();
}

/* =========================
   View（右邊顯示聊天室或 ML）
========================= */

function isMLView() {
  return currentTheme.view === "ml";
}

function showView() {
  const ml = isMLView();

  chatView.hidden = ml;
  mlView.hidden = !ml;

  topbarPage.textContent = currentNavigation.name.toUpperCase();

  if (ml) {
    MLLab.show(currentNavigation, currentTheme);
    return;
  }

  MLLab.hide();
  updateNavigation(currentNavigation);
  resetChat();
}

function updateNavigation(navigation) {
  const name = navigation.name;

  topbarPage.textContent = name.toUpperCase();

  pageTitle.innerHTML = `
    Talk to<br>
    <span>${name}.</span>
  `;

  pageDescription.textContent =
    navigation.description +
    " — ask questions and get useful answers through your AI workspace.";

  chatPanelTitle.textContent = `${name} Assistant`;
  infoModule.textContent = navigation.description;
  messageInput.placeholder = navigation.placeholder;
}

/* =========================
   Chat
========================= */

function resetChat() {
  chatMessages.innerHTML = "";

  addMessage(
    "assistant",
    currentNavigation.welcomeMessage
  );

  renderSuggestions();
}

function renderSuggestions() {
  const suggestionData = {
    weather: [
      "What is the weather in Taipei?",
      "Will it rain tomorrow?",
      "Show me this week's forecast."
    ],

    store: [
      "Find a coffee shop nearby.",
      "Recommend popular products.",
      "Help me compare prices."
    ]
  };

  const items =
    suggestionData[currentNavigation.id] || [];

  chatSuggestions.innerHTML = "";

  items.forEach((text) => {
    const button = document.createElement("button");

    button.type = "button";
    button.className = "chat-suggestion";
    button.textContent = text;

    button.addEventListener("click", () => {
      messageInput.value = text;
      sendMessage();
    });

    chatSuggestions.appendChild(button);
  });
}

function addMessage(role, text) {
  const message = document.createElement("div");

  message.className = `chat-message ${role}`;

  const mark = role === "assistant" ? "V" : "A";
  const author = role === "assistant" ? "VORA AI" : "YOU";

  message.innerHTML = `
    <span class="chat-message__mark">${mark}</span>

    <div class="chat-message__body">
      <span class="chat-message__author">${author}</span>
      <p class="chat-message__text"></p>
    </div>
  `;

  message.querySelector(
    ".chat-message__text"
  ).textContent = text;

  chatMessages.appendChild(message);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// function sendMessage() {
//   const message = messageInput.value.trim();
//
//   if (!message) return;
//
//   addMessage("user", message);
//   messageInput.value = "";
//
//   setTimeout(() => {
//     addMessage(
//       "assistant",
//       createDemoResponse(message)
//     );
//   }, 650);
// }

async function sendMessage() {
  const message = messageInput.value.trim();

  if (!message) return;

  addMessage("user", message);
  messageInput.value = "";

  const sendButton = chatForm.querySelector(".chat-form__send");

  try {
    sendButton.disabled = true;
    sendButton.textContent = "SENDING...";

    const response = await fetch("/llmapi/messageInput", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: message,
        theme: currentTheme.id,
        module: currentNavigation.id
      })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Request failed");
    }

    console.log(data.message);

    addMessage("assistant", data.message);
  } catch (error) {
    console.error("API Error:", error);

    addMessage(
      "assistant",
      "抱歉，後端目前無法處理這個請求。"
    );
  } finally {
    sendButton.disabled = false;
    sendButton.textContent = "SEND →";
  }
}

function createDemoResponse(message) {
  if (currentNavigation.id === "weather") {
    return [
      "Demo response — Weather API.",
      "",
      `Your question: ${message}`,
      "",
      "Connect your weather API in this location to return real-time data."
    ].join("\n");
  }

  if (currentNavigation.id === "store") {
    return [
      "Demo response — Store API.",
      "",
      `Your question: ${message}`,
      "",
      "Connect your product or store API in this location to return real data."
    ].join("\n");
  }

  return `Demo response: ${message}`;
}

/* =========================
   Sidebar events
========================= */

function bindEvents() {
  // sidebarToggle.addEventListener("click", () => {
  //   if (window.innerWidth <= 800) {
  //     sidebar.classList.toggle("is-mobile-open");
  //     return;
  //   }
  //
  //   sidebar.classList.toggle("is-collapsed");
  //
  //   localStorage.setItem(
  //     "vora-sidebar-collapsed",
  //     sidebar.classList.contains("is-collapsed")
  //   );
  // });
  sidebarToggle.addEventListener("click", () => {
    if (window.innerWidth <= 800) {
      sidebar.classList.toggle("is-mobile-open");
      return;
    }

    // 按下收起按鈕後，Sidebar 收合
    sidebar.classList.add("is-collapsed");

    localStorage.setItem(
      "vora-sidebar-collapsed",
      "true"
    );
  });

  sidebarLogo.addEventListener("click", (event) => {
    // 只有 Sidebar 收合時，Logo 才負責展開
    if (sidebar.classList.contains("is-collapsed")) {
      event.preventDefault();

      sidebar.classList.remove("is-collapsed");

      localStorage.setItem(
        "vora-sidebar-collapsed",
        "false"
      );
    }
  });

  mobileMenuButton.addEventListener("click", () => {
    sidebar.classList.toggle("is-mobile-open");
  });

  themeSelect.addEventListener("change", (event) => {
    switchTheme(event.target.value);
  });

  chatForm.addEventListener("submit", (event) => {
    event.preventDefault();
    sendMessage();
  });

  clearChatButton.addEventListener("click", () => {
    resetChat();
  });
}

/* =========================
   Scroll reveal
========================= */

function initReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.1
    }
  );

  document
    .querySelectorAll("[data-reveal]")
    .forEach((element) => observer.observe(element));
}

init();
