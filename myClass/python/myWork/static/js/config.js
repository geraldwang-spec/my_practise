const APP_CONFIG = {
  defaultTheme: "llm-api",

  themes: [
    {
      id: "llm-api",
      name: "LLM API",
      shortName: "LLM",
      icon: "◉",

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
    }
  ]
};
