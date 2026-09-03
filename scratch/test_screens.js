const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: "new"
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 800 });
    
    await page.goto('http://localhost:5024/bookings', { waitUntil: 'networkidle0' });
    await page.screenshot({ path: 'bookings.png' });
    
    // Click on VIEW DETAILS
    await page.click('.view-details-btn');
    await page.waitForTimeout(1000);
    await page.screenshot({ path: 'bookings_modal.png' });

    await browser.close();
    console.log("Screenshots taken.");
})();
