/* =========================
   VORA — ML Lab
   在 index.html 裡選 ML API theme 時，由 app.js 呼叫：
   MLLab.show(navigation, theme) / MLLab.hide()
========================= */

const MLLab = (() => {
  const ML_API_ENDPOINT = "/mlapi/linearRegression";
  const ML_API_GRADIENT_ENDPOINT = "/mlapi/gradientStep";
  const PAD = 30; // 圖表內距（px）

  const $ = (id) => document.getElementById(id);

  const pageTitle = $("mlPageTitle");
  const pageDescription = $("mlPageDescription");
  const panelTitle = $("mlPanelTitle");
  const infoTheme = $("mlInfoTheme");
  const infoModule = $("mlInfoModule");

  const plotWrap = $("plotWrap");
  const plotCanvas = $("plotCanvas");
  const lossWrap = $("lossWrap");
  const lossCanvas = $("lossCanvas");

  const lrInput = $("lrInput");
  const lrValue = $("lrValue");
  const epochInput = $("epochInput");
  const epochValue = $("epochValue");
  const noiseInput = $("noiseInput");
  const noiseValue = $("noiseValue");

  const trainButton = $("trainButton");
  const stepButton = $("stepButton");
  const resetButton = $("resetButton");
  const randomButton = $("randomButton");
  const serverButton = $("serverButton");
  const gradientButton = $("gradientButton")
  const clearPointsButton = $("clearPointsButton");

  const statusText = $("statusText");
  const formula = $("formula");
  const serverFormula = $("serverFormula");
  const metricEpoch = $("metricEpoch");
  const metricPoints = $("metricPoints");
  const metricLoss = $("metricLoss");

  let initialized = false;
  let currentNavigation = null;

  const state = {
    points: [], // { x, y }，都在 0 ~ 1 之間
    w: 0,
    b: 0,
    epoch: 0,
    lossHistory: [],
    training: false,
    target: 0,
    rafId: null,
    hover: null, // 滑鼠目前在圖上的位置 { x, y }，離開圖表時是 null
    serverLine: null // 後端回傳的結果 { w, b }，用虛線畫出來比較
  };

  const plot = { ctx: null, width: 0, height: 0 };
  const lossPlot = { ctx: null, width: 0, height: 0 };

  /* ---------- Math ---------- */

  function predict(x) {
    return state.w * x + state.b;
  }

  // MSE = (1/n) Σ (ŷ - y)²
  function computeLoss() {
    const n = state.points.length;
    if (n === 0) return 0;

    let sum = 0;
    for (const p of state.points) {
      const error = predict(p.x) - p.y;
      sum += error * error;
    }
    return sum / n;
  }

  // 梯度下降一次：
  // ∂L/∂w = (2/n) Σ (ŷ - y)·x
  // ∂L/∂b = (2/n) Σ (ŷ - y)
  function gradientStep(learningRate) {
    const n = state.points.length;
    let dw = 0;
    let db = 0;

    for (const p of state.points) {
      const error = predict(p.x) - p.y;
      dw += error * p.x;
      db += error;
    }

    state.w -= learningRate * (2 / n) * dw;
    state.b -= learningRate * (2 / n) * db;
    state.epoch += 1;

    const loss = computeLoss();
    state.lossHistory.push(loss);
    return loss;
  }

  function predictServer(x) {
    return state.serverLine.w * x + state.serverLine.b;
  }

  function computeServerLoss() {
    const n = state.points.length;
    if (!state.serverLine || n === 0) return 0;

    let sum = 0;
    for (const p of state.points) {
      const error = predictServer(p.x) - p.y;
      sum += error * error;
    }
    return sum / n;
  }

  // 資料改變後，舊的後端結果就不準了
  function clearServerLine() {
    state.serverLine = null;
  }

  /* ---------- Training ---------- */

  function setStatus(text) {
    statusText.textContent = text;
  }

  function hasEnoughPoints() {
    if (state.points.length >= 2) return true;
    setStatus("至少需要 2 個資料點才能訓練。點擊圖表新增，或按 RANDOM DATA。");
    return false;
  }

  function startTraining() {
    if (!hasEnoughPoints()) return;

    const epochs = Number(epochInput.value);
    const stepsPerFrame = Math.max(1, Math.ceil(epochs / 180));

    state.training = true;
    state.target = state.epoch + epochs;
    trainButton.textContent = "PAUSE";
    setStatus("訓練中…");

    const loop = () => {
      const learningRate = Number(lrInput.value);
      let loss = computeLoss();

      for (let i = 0; i < stepsPerFrame && state.epoch < state.target; i++) {
        loss = gradientStep(learningRate);

        if (!Number.isFinite(loss)) {
          stopTraining();
          render();
          setStatus(
            "Loss 發散了：學習率太大，每一步都跨過最低點。調低 LEARNING RATE，再按 RESET W, B 重來。"
          );
          return;
        }
      }

      render();

      if (state.epoch >= state.target) {
        stopTraining();
        setStatus(`完成 ${epochs} 個 epochs，MSE = ${formatNumber(loss, 6)}。`);
        return;
      }

      state.rafId = requestAnimationFrame(loop);
    };

    state.rafId = requestAnimationFrame(loop);
  }

  function stopTraining() {
    state.training = false;
    cancelAnimationFrame(state.rafId);
    trainButton.textContent = "TRAIN";
  }

  function toggleTraining() {
    if (state.training) {
      stopTraining();
      setStatus(`已暫停在 epoch ${state.epoch}。按 TRAIN 繼續。`);
      return;
    }
    startTraining();
  }

  function stepOnce() {
    if (!hasEnoughPoints()) return;
    stopTraining();

    const loss = gradientStep(Number(lrInput.value));
    render();
    setStatus(
      `走了一步：w = ${formatNumber(state.w)}，b = ${formatNumber(state.b)}，MSE = ${formatNumber(loss, 6)}`
    );
  }

  function resetParams() {
    stopTraining();
    state.w = 0;
    state.b = 0;
    state.epoch = 0;
    state.lossHistory = [];
    render();
  }

  function clearPoints() {
    state.points = [];
    clearServerLine();
    resetParams();
    setStatus("資料已清空。點擊圖表新增資料點。");
  }

  /* ---------- Data ---------- */

  function random(min, max) {
    return min + Math.random() * (max - min);
  }

  // Box–Muller：產生常態分佈雜訊
  function gaussian() {
    const u = 1 - Math.random();
    const v = Math.random();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  }

  function generateRandomData() {
    const noise = Number(noiseInput.value);
    const trueW = random(-0.8, 0.8);
    const trueB = 0.5 - trueW * 0.5 + random(-0.1, 0.1);

    state.points = Array.from({ length: 40 }, () => {
      const x = random(0.05, 0.95);
      const y = trueW * x + trueB + gaussian() * noise;
      return { x, y: Math.min(0.98, Math.max(0.02, y)) };
    });

    clearServerLine();
    resetParams();
    setStatus(
      `產生了 40 個點，真實答案約 w = ${trueW.toFixed(3)}、b = ${trueB.toFixed(3)}。按 TRAIN 看模型能不能找回來。`
    );
  }

  /* ---------- Backend（可選） ---------- */

  async function trainOnServer() {
    if (!hasEnoughPoints()) return;
    stopTraining();

    const epochs = Number(epochInput.value);
    const learningRate = Number(lrInput.value);

    try {
      serverButton.disabled = true;
      serverButton.textContent = "TRAINING...";

      const response = await fetch(ML_API_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          module: currentNavigation ? currentNavigation.id : "linearRegression",
          points: state.points,
          learningRate,
          epochs
        })
      });

      // 先檢查狀態碼：404 / 405 時後端回的是 HTML，不能當 JSON 解析
      if (!response.ok) {
        throw new Error(`後端回應 ${response.status}`);
      }

      // 後端格式：{ success, message, data: { w, b, epochs, lossHistory } }
      const body = await response.json();

      if (body.success === false) {
        throw new Error(body.message || "Request failed");
      }

      const result = body.data ?? body;

      if (!Number.isFinite(Number(result.w)) || !Number.isFinite(Number(result.b))) {
        throw new Error("後端回傳的資料沒有 w、b");
      }

      // 後端結果另外存，不覆蓋前端訓練的 w、b
      state.serverLine = { w: Number(result.w), b: Number(result.b) };

      render();

      const dw = Math.abs(state.w - state.serverLine.w);
      const db = Math.abs(state.b - state.serverLine.b);

      setStatus(
        `後端（虛線）：w = ${formatNumber(state.serverLine.w)}，b = ${formatNumber(state.serverLine.b)}，` +
        `MSE = ${formatNumber(computeServerLoss(), 6)}。` +
        `和前端（實線）相差 Δw = ${formatNumber(dw, 4)}，Δb = ${formatNumber(db, 4)}。`
      );
    } catch (error) {
      console.error("ML API Error:", error);
      setStatus(`後端錯誤（${error.message}）。前端的 TRAIN 仍然可以使用。`);
    } finally {
      serverButton.disabled = false;
      serverButton.textContent = "TRAIN ON SERVER";
    }
  }

  async function gradientOnServer() {
    if (!hasEnoughPoints()) return;
    stopTraining();

    const epochs = Number(epochInput.value);
    const learningRate = Number(lrInput.value);

    try {
      gradientButton.disabled = true;
      gradientButton.textContent = "TRAINING...";

      const response = await fetch(ML_API_GRADIENT_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          module: currentNavigation ? currentNavigation.id : "linearRegression",
          points: state.points,
          learningRate,
          epochs
        })
      });

      console.log("QOO");
    } catch (error) {
      console.error("ML API Error:", error);
      setStatus(`後端錯誤（${error.message}）。前端的 TRAIN 仍然可以使用。`);
    } finally {
      gradientButton.disabled = false;
      gradientButton.textContent = "Gradient ON SERVER";
    }
  }

  /* ---------- Canvas ---------- */

  function setupCanvas(canvas, target) {
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();

    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);

    target.ctx = canvas.getContext("2d");
    target.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    target.width = rect.width;
    target.height = rect.height;
  }

  function resizeCanvases() {
    setupCanvas(plotCanvas, plot);
    setupCanvas(lossCanvas, lossPlot);
    render();
  }

  function toPixel(x, y) {
    return [
      PAD + x * (plot.width - PAD * 2),
      plot.height - PAD - y * (plot.height - PAD * 2)
    ];
  }

  function toData(px, py) {
    return [
      (px - PAD) / (plot.width - PAD * 2),
      1 - (py - PAD) / (plot.height - PAD * 2)
    ];
  }

  function drawPlot() {
    const { ctx, width, height } = plot;
    if (!ctx || width === 0) return;

    ctx.clearRect(0, 0, width, height);

    // Grid
    ctx.lineWidth = 1;
    ctx.strokeStyle = "rgba(255,255,255,0.07)";
    for (let i = 0; i <= 10; i++) {
      const [gx] = toPixel(i / 10, 0);
      const [, gy] = toPixel(0, i / 10);

      ctx.beginPath();
      ctx.moveTo(gx + 0.5, PAD);
      ctx.lineTo(gx + 0.5, height - PAD);
      ctx.moveTo(PAD, gy + 0.5);
      ctx.lineTo(width - PAD, gy + 0.5);
      ctx.stroke();
    }

    // Axes
    const [ox, oy] = toPixel(0, 0);
    ctx.strokeStyle = "rgba(255,255,255,0.5)";
    ctx.beginPath();
    ctx.moveTo(ox, PAD);
    ctx.lineTo(ox, oy);
    ctx.lineTo(width - PAD, oy);
    ctx.stroke();

    // Tick labels
    ctx.fillStyle = "rgba(255,255,255,0.42)";
    ctx.font = '10px "IBM Plex Mono", monospace';
    ctx.textAlign = "center";
    ctx.fillText("0", ox, oy + 16);
    ctx.fillText("0.5", toPixel(0.5, 0)[0], oy + 16);
    ctx.fillText("1  x", toPixel(1, 0)[0], oy + 16);
    ctx.textAlign = "right";
    ctx.fillText("0.5", ox - 6, toPixel(0, 0.5)[1] + 3);
    ctx.fillText("y  1", ox - 6, toPixel(0, 1)[1] + 3);

    const lineIsValid =
      Number.isFinite(state.w) &&
      Number.isFinite(state.b) &&
      Math.abs(state.w) < 1e6 &&
      Math.abs(state.b) < 1e6;

    // Residuals（每個點到預測值的誤差）
    if (lineIsValid) {
      ctx.save();
      ctx.setLineDash([3, 4]);
      ctx.strokeStyle = "rgba(255,255,255,0.28)";
      ctx.beginPath();
      for (const p of state.points) {
        const [px, py] = toPixel(p.x, p.y);
        const [, qy] = toPixel(p.x, predict(p.x));
        ctx.moveTo(px, py);
        ctx.lineTo(px, qy);
      }
      ctx.stroke();
      ctx.restore();
    }

    // Regression line（裁切在圖表範圍內）
    if (lineIsValid) {
      ctx.save();
      ctx.beginPath();
      ctx.rect(PAD, PAD, width - PAD * 2, height - PAD * 2);
      ctx.clip();

      const [x0, y0] = toPixel(0, predict(0));
      const [x1, y1] = toPixel(1, predict(1));

      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(x1, y1);
      ctx.stroke();
      ctx.restore();
    }

    // Server line（虛線 + SERVER 標籤）
    if (state.serverLine) {
      ctx.save();
      ctx.beginPath();
      ctx.rect(PAD, PAD, width - PAD * 2, height - PAD * 2);
      ctx.clip();

      const [sx0, sy0] = toPixel(0, predictServer(0));
      const [sx1, sy1] = toPixel(1, predictServer(1));

      ctx.setLineDash([8, 6]);
      ctx.strokeStyle = "rgba(255,255,255,0.75)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(sx0, sy0);
      ctx.lineTo(sx1, sy1);
      ctx.stroke();
      ctx.restore();

      const labelY = predictServer(0.97);
      if (labelY >= 0 && labelY <= 1) {
        const [lx, ly] = toPixel(0.97, labelY);
        ctx.fillStyle = "rgba(255,255,255,0.75)";
        ctx.font = '10px "IBM Plex Mono", monospace';
        ctx.textAlign = "right";
        ctx.fillText("SERVER", lx, ly - 8);
      }
    }

    // Points
    for (const p of state.points) {
      const [px, py] = toPixel(p.x, p.y);
      ctx.fillStyle = "#111110";
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(px, py, 4, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    }

    drawHover(lineIsValid);
  }

  // 滑鼠座標：十字線 + 數值標籤 + 該 x 的預測值
  function drawHover(lineIsValid) {
    if (!state.hover) return;

    const { ctx, width, height } = plot;
    const { x, y } = state.hover;
    const [hx, hy] = toPixel(x, y);

    // 十字線
    ctx.save();
    ctx.setLineDash([2, 3]);
    ctx.strokeStyle = "rgba(255,255,255,0.35)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(hx, PAD);
    ctx.lineTo(hx, height - PAD);
    ctx.moveTo(PAD, hy);
    ctx.lineTo(width - PAD, hy);
    ctx.stroke();
    ctx.restore();

    // 軸上的刻度值
    ctx.font = '10px "IBM Plex Mono", monospace';
    ctx.fillStyle = "#ffffff";
    ctx.textAlign = "center";
    ctx.fillText(x.toFixed(2), hx, height - PAD + 28);
    ctx.textAlign = "left";
    ctx.fillText(y.toFixed(2), 2, hy + 3);

    // 這個 x 對應的模型預測值 ŷ（畫在迴歸線上）
    const lines = [`x  ${x.toFixed(3)}`, `y  ${y.toFixed(3)}`];

    if (lineIsValid) {
      const yHat = predict(x);
      lines.push(`ŷ  ${formatNumber(yHat)}`);

      if (yHat >= 0 && yHat <= 1) {
        const [, py] = toPixel(x, yHat);
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.rect(hx - 4, py - 4, 8, 8);
        ctx.stroke();
      }
    }

    if (state.serverLine) {
      lines.push(`srv ${formatNumber(predictServer(x))}`);
    }

    // 數值標籤（靠近邊緣時翻到另一側，避免超出圖表）
    const lineHeight = 14;
    const boxWidth = 92;
    const boxHeight = lines.length * lineHeight + 10;

    let bx = hx + 14;
    let by = hy - boxHeight - 10;
    if (bx + boxWidth > width - 4) bx = hx - boxWidth - 14;
    if (by < 4) by = hy + 14;

    ctx.fillStyle = "rgba(17,17,16,0.92)";
    ctx.strokeStyle = "rgba(255,255,255,0.6)";
    ctx.lineWidth = 1;
    ctx.fillRect(bx, by, boxWidth, boxHeight);
    ctx.strokeRect(bx + 0.5, by + 0.5, boxWidth - 1, boxHeight - 1);

    ctx.fillStyle = "#ffffff";
    ctx.textAlign = "left";
    lines.forEach((text, index) => {
      ctx.fillText(text, bx + 8, by + 16 + index * lineHeight);
    });
  }

  function drawLoss() {
    const { ctx, width, height } = lossPlot;
    if (!ctx || width === 0) return;

    ctx.clearRect(0, 0, width, height);

    ctx.strokeStyle = "rgba(255,255,255,0.13)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, height - 0.5);
    ctx.lineTo(width, height - 0.5);
    ctx.stroke();

    const history = state.lossHistory.filter(Number.isFinite);

    if (history.length < 2) {
      ctx.fillStyle = "rgba(255,255,255,0.42)";
      ctx.font = '10px "IBM Plex Mono", monospace';
      ctx.textAlign = "left";
      ctx.fillText("尚未訓練", 0, height / 2);
      return;
    }

    const max = Math.max(...history) || 1;
    const stride = Math.max(1, Math.floor(history.length / width));

    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 1.5;
    ctx.beginPath();

    for (let i = 0; i < history.length; i += stride) {
      const x = (i / (history.length - 1)) * width;
      const y = height - 4 - (history[i] / max) * (height - 12);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }

    ctx.stroke();
  }

  /* ---------- Render ---------- */

  function formatNumber(value, digits = 3) {
    if (!Number.isFinite(value)) return "∞";
    if (Math.abs(value) >= 1e4) return value.toExponential(2);
    return value.toFixed(digits);
  }

  function updateMetrics() {
    const sign = state.b >= 0 ? "+" : "−";

    formula.textContent =
      `ŷ = ${formatNumber(state.w)}x ${sign} ${formatNumber(Math.abs(state.b))}`;

    if (state.serverLine) {
      const serverSign = state.serverLine.b >= 0 ? "+" : "−";
      serverFormula.textContent =
        `ŷ = ${formatNumber(state.serverLine.w)}x ${serverSign} ${formatNumber(Math.abs(state.serverLine.b))}`;
    } else {
      serverFormula.textContent = "—";
    }

    metricEpoch.textContent = state.epoch;
    metricPoints.textContent = state.points.length;
    metricLoss.textContent = state.points.length
      ? formatNumber(computeLoss(), 6)
      : "—";
  }

  function render() {
    drawPlot();
    drawLoss();
    updateMetrics();
  }

  /* ---------- Events ---------- */

  function bindEvents() {
    lrInput.addEventListener("input", () => {
      lrValue.textContent = Number(lrInput.value).toFixed(3);
    });

    epochInput.addEventListener("input", () => {
      epochValue.textContent = epochInput.value;
    });

    noiseInput.addEventListener("input", () => {
      noiseValue.textContent = Number(noiseInput.value).toFixed(2);
    });

    trainButton.addEventListener("click", toggleTraining);
    stepButton.addEventListener("click", stepOnce);
    resetButton.addEventListener("click", () => {
      resetParams();
      setStatus("w、b 已歸零。按 TRAIN 重新訓練。");
    });
    randomButton.addEventListener("click", generateRandomData);
    serverButton.addEventListener("click", trainOnServer);
    gradientButton.addEventListener("click", gradientOnServer);
    clearPointsButton.addEventListener("click", clearPoints);

    // 左鍵：新增資料點
    plotCanvas.addEventListener("click", (event) => {
      const rect = plotCanvas.getBoundingClientRect();
      const [x, y] = toData(event.clientX - rect.left, event.clientY - rect.top);

      if (x < 0 || x > 1 || y < 0 || y > 1) return;

      state.points.push({ x, y });
      clearServerLine();
      render();
      setStatus(`新增點 (${x.toFixed(2)}, ${y.toFixed(2)})，共 ${state.points.length} 個。`);
    });

    // 滑鼠移動：更新座標顯示
    plotCanvas.addEventListener("pointermove", (event) => {
      const rect = plotCanvas.getBoundingClientRect();
      const [x, y] = toData(event.clientX - rect.left, event.clientY - rect.top);

      const inside = x >= 0 && x <= 1 && y >= 0 && y <= 1;
      state.hover = inside ? { x, y } : null;

      // 訓練中每一幀都會重畫，不用額外重畫
      if (!state.training) drawPlot();
    });

    // 滑鼠離開：隱藏座標
    plotCanvas.addEventListener("pointerleave", () => {
      state.hover = null;
      if (!state.training) drawPlot();
    });

    // 右鍵：刪除最近的資料點
    plotCanvas.addEventListener("contextmenu", (event) => {
      event.preventDefault();

      const rect = plotCanvas.getBoundingClientRect();
      const mx = event.clientX - rect.left;
      const my = event.clientY - rect.top;

      let nearest = -1;
      let nearestDistance = 14;

      state.points.forEach((p, index) => {
        const [px, py] = toPixel(p.x, p.y);
        const distance = Math.hypot(px - mx, py - my);
        if (distance < nearestDistance) {
          nearest = index;
          nearestDistance = distance;
        }
      });

      if (nearest >= 0) {
        state.points.splice(nearest, 1);
        clearServerLine();
        render();
        setStatus(`刪除一個點，剩 ${state.points.length} 個。`);
      }
    });

    // 區塊從隱藏變成顯示、或視窗大小改變時，重新計算 canvas 大小
    const observer = new ResizeObserver(resizeCanvases);
    observer.observe(plotWrap);
    observer.observe(lossWrap);
  }

  /* ---------- Public ---------- */

  function show(navigation, theme) {
    currentNavigation = navigation;

    pageTitle.innerHTML = `Train a<br><span>${navigation.name}.</span>`;
    pageDescription.textContent = navigation.welcomeMessage;
    panelTitle.textContent = `${navigation.name} Lab`;
    infoTheme.textContent = theme.name;
    infoModule.textContent = navigation.description;

    if (!initialized) {
      bindEvents();
      generateRandomData();
      initialized = true;
    }

    requestAnimationFrame(resizeCanvases);
  }

  function hide() {
    if (initialized) stopTraining();
  }

  return { show, hide };
})();
