const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: "new"
    });
    
    const page = await browser.newPage();
    
    // override localStorage
    await page.goto('http://localhost:5024/beranda', { waitUntil: 'networkidle0' });
    
    await page.evaluate(() => {
        const btns = Array.from(document.querySelectorAll('button'));
        const target = btns.find(b => b.textContent.includes('Lihat'));
        if(target) target.click();
    });
    
    await new Promise(r => setTimeout(r, 1500));
    const html = await page.content();
    require('fs').writeFileSync('beranda_popup.html', html);
    
    await browser.close();
    console.log("HTML dumped.");
})();
