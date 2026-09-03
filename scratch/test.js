const puppeteer = require('puppeteer');

(async () => {
    console.log("Launching browser...");
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    
    page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
    page.on('pageerror', err => console.log('BROWSER ERROR:', err.toString()));

    console.log("Navigating to http://localhost:5024/bookings");
    await page.goto('http://localhost:5024/bookings', { waitUntil: 'networkidle0' });
    
    console.log("Clicking VIEW DETAILS...");
    try {
        await page.waitForSelector('.view-details-btn', { timeout: 3000 });
        await page.click('.view-details-btn');
        await page.waitForTimeout(1000);
    } catch (e) {
        console.log("Could not click view details:", e.message);
    }

    console.log("Navigating to http://localhost:5024");
    await page.goto('http://localhost:5024', { waitUntil: 'networkidle0' });
    
    console.log("Clicking + Booking Baru...");
    try {
        await page.waitForSelector('.btn-primary', { timeout: 3000 });
        await page.click('.btn-primary');
        await page.waitForTimeout(1000);
    } catch (e) {}

    await browser.close();
    console.log("Done");
})();
