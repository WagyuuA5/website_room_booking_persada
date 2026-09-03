const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: "new"
    });
    
    const pages = ['/', '/bookings', '/status', '/history', '/settings'];
    
    for (const p of pages) {
        console.log("Testing " + p);
        const page = await browser.newPage();
        try {
            await page.goto('http://localhost:5024' + p, { waitUntil: 'networkidle0' });
            await page.waitForTimeout(1000);
            
            // Try to click any popup triggers
            if (p === '/') {
                // Beranda has "Ruangan Tersedia" and "Menunggu Persetujuan"
                try { await page.click('button:contains("Lihat")'); } catch (e) {}
            }
        } catch (e) {}
        await page.close();
    }

    await browser.close();
})();
