const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const WORK='tools/_work', OUT='assets/logos';
const style = fs.readFileSync(WORK+'/style.css','utf8');
const defs  = fs.readFileSync(WORK+'/defs.svg','utf8');

// key -> CSS render width in px (viewBox scales losslessly; DSF multiplies)
const STATIC = [
  ['wm_principal',1600],['wm_sin_slogan',1600],
  ['wm_ecorojo_slogan',1600],['wm_ecorojo',1600],['wm_base',1600],
  ['ic_negativo',900],['ic_construccion',900],['ic_doble',900],
];
const DSF = 3;

(async()=>{
  const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  for(const [key,w] of STATIC){
    const svg = fs.readFileSync(`${WORK}/${key}.svg`,'utf8');
    const page = await browser.newPage({viewport:{width:Math.ceil(w)+80,height:900},deviceScaleFactor:DSF});
    const html = `<!doctype html><meta charset=utf-8><style>${style}
      html,body{background:transparent!important;margin:0;padding:0}
      #stage{display:inline-block}
      #stage svg.wm{display:block;width:${w}px;height:auto;max-width:none}
    </style>${defs}<div id="stage">${svg}</div>`;
    await page.setContent(html,{waitUntil:'load'});
    await page.evaluate(()=>document.fonts.ready);
    await page.waitForTimeout(250);
    const el = await page.$('#stage svg.wm');
    await el.screenshot({path:`${OUT}/${key}.png`, omitBackground:true});
    const box = await el.boundingBox();
    console.log(`${key}.png  ${Math.round(box.width*DSF)}x${Math.round(box.height*DSF)}`);
    await page.close();
  }
  await browser.close();
})();
