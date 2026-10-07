const APP_CONFIG = {
  defaultTheme: "llm-api",

  themes: [
    {
      id: "llm-api",
      name: "LLM API",
      shortName: "LLM",
      icon: "◉",

      // 右邊要顯示哪一種內容："chat" 或 "ml"
      view: "chat",

      navigation: [
        {
          id: "weather",
          name: "Weather",
          label: "天氣",
          icon: "☼",
          description: "Weather API",
          placeholder: "Ask about weather, temperature or forecasts...",
          welcomeMessage:
            "Welcome. I can help you check weather conditions, temperature and forecasts."
        },
        {
          id: "store",
          name: "Store",
          label: "商店",
          icon: "＋",
          description: "Store API",
          placeholder: "Ask about products, stores or prices...",
          welcomeMessage:
            "Welcome. I can help you search products, compare prices and find stores."
        }
      ]
    },
    {
      id: "ml-api",
      name: "ML API",
      shortName: "ML",
      icon: "◈",

      view: "ml",

      navigation: [
        {
          id: "linearRegression",
          name: "LinearRegression",
          label: "線性迴歸",
          icon: "∕",
          description: "LinearRegression API",
          placeholder: "Practise LinearRegression",
          welcomeMessage:
            "Click the plot to add points, then train a line that fits them."
        }
      ]
    }
  ]
};
