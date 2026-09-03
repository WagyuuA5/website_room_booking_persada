const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: "new"
    });
    const page = await browser.newPage();
    
    await page.goto('http://localhost:5024/bookings', { waitUntil: 'networkidle0' });
    const html = await page.content();
    fs.writeFileSync('bookings.html', html);
    
    await browser.close();
    console.log("HTML saved.");
})();
