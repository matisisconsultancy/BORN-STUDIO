const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const WORK='tools/_work';
const style = fs.readFileSync(WORK+'/style.css','utf8');
const defs  = fs.readFileSync(WORK+'/defs.svg','utf8');

// anim key -> {dur ms, fps, poster fraction}
const ANIMS = {
  an_ensamblaje: {dur:6000, fps:24, poster:0.85},
  an_barrida:    {dur:5000, fps:24, poster:0.90},
};
const CW=1600, CH=600, LOGO_W=1120;

(async()=>{
  const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  for(const [key,cfg] of Object.entries(ANIMS)){
    const svg = fs.readFileSync(`${WORK}/${key}.svg`,'utf8');
    const dir = `${WORK}/frames_${key}`;
    fs.rmSync(dir,{recursive:true,force:true}); fs.mkdirSync(dir,{recursive:true});
    const page = await browser.newPage({viewport:{width:CW,height:CH},deviceScaleFactor:2});
    const html = `<!doctype html><meta charset=utf-8><style>${style}
      html,body{margin:0;background:#F2EEE6}
      #cv{width:${CW}px;height:${CH}px;display:flex;align-items:center;justify-content:center;background:#F2EEE6}
      #cv svg.wm{width:${LOGO_W}px;height:auto;max-width:none;overflow:visible}
    </style>${defs}<div id="cv">${svg}</div>`;
    await page.setContent(html,{waitUntil:'load'});
    await page.evaluate(()=>document.fonts.ready);
    // pause all CSS animations so we can scrub deterministically
    await page.evaluate(()=>{document.getAnimations().forEach(a=>a.pause());});
    const N = Math.round(cfg.dur/1000*cfg.fps);
    for(let i=0;i<N;i++){
      const t = i/N*cfg.dur;
      await page.evaluate(ms=>{document.getAnimations().forEach(a=>{a.currentTime=ms;});}, t);
      await page.screenshot({path:`${dir}/f${String(i).padStart(4,'0')}.png`,
        clip:{x:0,y:0,width:CW,height:CH}});
    }
    // poster frame
    await page.evaluate(ms=>{document.getAnimations().forEach(a=>{a.currentTime=ms;});}, cfg.dur*cfg.poster);
    await page.screenshot({path:`${dir}/poster.png`,clip:{x:0,y:0,width:CW,height:CH}});
    console.log(`${key}: ${N} frames @ ${cfg.fps}fps`);
    await page.close();
  }
  await browser.close();
})();
