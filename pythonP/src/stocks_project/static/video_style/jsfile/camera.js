let videoTrack;
const video = document.getElementById('video');
const canvas = document.getElementById('helper-canvas');
const ctx = canvas.getContext('2d', { willReadFrequently: true });
const rgbText = document.getElementById('rgb-text');
const colorBox = document.getElementById('color-box');

const wbLogicSwitch = document.getElementById('wb-logic-switch');
const manualSettings = document.getElementById('manual-settings');
const wbSlider = document.getElementById('wb-slider');
const tempDisplay = document.getElementById('temp-display');

// 監聽開關切換
wbLogicSwitch.addEventListener('change', (e) => {
  if (e.target.checked) {
    // 切換到「手動」
    manualSettings.style.display = 'block';
    applyWB('manual', wbSlider.value);
  } else {
    // 切換到「自動」
    manualSettings.style.display = 'none';
    applyWB('continuous');
  }
});

// 監聽數值拉桿
wbSlider.addEventListener('input', (e) => {
  tempDisplay.innerText = e.target.value;
  applyWB('manual', e.target.value);
});

// 封裝相機控制函數
async function applyWB(mode, value) {
  // 這裡放入您之前的 track.applyConstraints 邏輯
  // console.log(`目前設定模式：${mode}, 數值：${value || '自動'}`);
  if (!videoTrack) return;
  try {
    // const constraints = {
    //   advanced: [{
    //     whiteBalanceMode: mode,
    //     exposureMode: mode === 'manual' ? 'manual' : 'continuous',
    //     colorTemperature: parseInt(value),
    //   }]
    // }
    const settings = {
      whiteBalanceMode: mode,
      exposureMode: mode === 'manual' ? 'manual' : 'continuous',
    }

    if (mode == 'manual' && value) {
      settings.colorTemperature = parseInt(value);
    }
    // else {
    //   constraints.advanced[0].colorTemperature = parseInt(value);
    //   constraints.advanced[0].exposureMode = 'continuous';
    // }

    const constraints = {
      advanced: [settings]
    }
    await videoTrack.applyConstraints(constraints);
    console.log(`sync HW ${mode} @ ${value || 'Auto'}K`)

  } catch (err) {
    console.error("can't to use white balance setting:", err)
  }
}

async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: "environment", width: 640, height: 480 },
      audio: false
    });
    video.srcObject = stream;

    videoTrack = stream.getVideoTracks()[0];
    const settings = videoTrack.getSettings();
    const capabilities = videoTrack.getCapabilities();

    console.log("當前設定:", settings.colorTemperature);
    console.log("支援範圍:", capabilities.colorTemperature.min, "-", capabilities.colorTemperature.max);
    console.log("調整步進:", capabilities.colorTemperature.step);

    if (capabilities.colorTemperature) {
      wbSlider.min = capabilities.colorTemperature.min;
      wbSlider.max = capabilities.colorTemperature.max;
      tempDisplay.innerText = wbSlider.value
    }
    // if (capabilities.whiteBalanceMode?.includes('manual')) {
    //   // await track.applyConstraints({
    //   //   advanced: [{
    //   //     whiteBalanceMode: 'manual',
    //   //     colorTemperature: 4500
    //   //   }]
    //   // });
    //   console.log('white balance maunal mode (4500K)');
    // }

    // 開始循環讀取數值
    requestAnimationFrame(updateFrame);
  } catch (err) {
    alert("無法開啟攝像頭，請檢查權限或是否為 HTTPS 環境" + err.message);
  }
}

function updateFrame() {
  if (video.readyState === video.HAVE_ENOUGH_DATA) {
    // 將影像繪製到隱藏的畫布
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    // 取得中心點 (320, 240) 的 1x1 像素數據
    const p = ctx.getImageData(canvas.width / 2, canvas.height / 2, 1, 1).data;
    const r = p[0], g = p[1], b = p[2];

    // 更新 UI
    rgbText.innerText = `R: ${r}, G: ${g}, B: ${b}`;
    colorBox.style.backgroundColor = `rgb(${r},${g},${b})`;
  }
  requestAnimationFrame(updateFrame);
}

init();

