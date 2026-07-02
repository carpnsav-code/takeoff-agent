// Render a takeoff-diagram HTML file to a PNG using the pre-installed Chromium.
// Part of the standard takeoff-diagram workflow.
//
// Usage:
//   NODE_PATH=$(npm root -g) node render-diagram.js <input.html> <output.png> [widthPx]
//
// The script screenshots the <svg> element so the PNG is tightly cropped to the
// diagram (no page margins). Increase widthPx for a sharper export.

const { chromium } = require('playwright');

(async () => {
  const [, , inHtml, outPng, widthArg] = process.argv;
  if (!inHtml || !outPng) {
    console.error('usage: node render-diagram.js <input.html> <output.png> [widthPx]');
    process.exit(1);
  }
  const width = parseInt(widthArg || '2240', 10);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width, height: 1400 }, deviceScaleFactor: 2 });
  const url = inHtml.startsWith('file://') ? inHtml : 'file://' + require('path').resolve(inHtml);
  await page.goto(url);
  await page.waitForTimeout(600); // let the background plan image decode
  const svg = await page.$('svg');
  await (svg || page).screenshot({ path: outPng });
  await browser.close();
  console.log('wrote', outPng);
})();
