// Slide number in the header, Super Stack style: [04] Cloudflare Gatekeeper for Vibe Coders ────
// Shared by every cf-slide-XX.html. The number comes from the file name, so a new
// slide only needs a script tag pointing at assets/slide-no.js and a .label header.
(function(){
  var m = location.pathname.match(/slide-(\d+)([a-z]?)\.html$/i) || (document.documentElement.getAttribute('data-slide')||'').match(/^(\d+)([a-z]?)$/i);
  if(!m) return;
  var no = String(parseInt(m[1],10)).padStart(2,'0') + (m[2]||'').toUpperCase();
  var stage = document.getElementById('stage');
  if(!stage) return;

  var old = stage.querySelector('.page');
  if(old) old.remove();

  var css = document.createElement('style');
  css.textContent =
    '.label.numbered{gap:22px}'+
    '.label.numbered::before{display:none}'+
    '.slide-no{flex:none;height:50px;min-width:72px;padding:0 14px;display:flex;align-items:center;justify-content:center;border-radius:12px;'+
      'font:800 30px/1 Inter,system-ui,sans-serif;letter-spacing:-.01em;color:#fff;'+
      'background:linear-gradient(160deg,rgba(255,255,255,.14),rgba(0,0,0,.6));border:2px solid rgba(255,255,255,.85);'+
      'box-shadow:0 0 18px rgba(255,255,255,.3),inset 0 0 12px rgba(255,255,255,.1);'+
      'animation:slideNoIn .7s .1s cubic-bezier(.3,1.5,.5,1) both}'+
    '.slide-line{position:relative;flex:none;width:520px;height:2px;margin-left:8px;'+
      'background:linear-gradient(90deg,rgba(255,255,255,.75),rgba(255,255,255,.25) 60%,transparent);'+
      'transform-origin:left;animation:slideLineIn 1s .5s cubic-bezier(.2,.8,.2,1) both}'+
    '.slide-line::before{content:"";position:absolute;left:0;top:-3px;width:150px;height:8px;border-radius:8px;'+
      'background:linear-gradient(90deg,#F6821F,rgba(246,130,31,.35));box-shadow:0 0 14px rgba(246,130,31,.7)}'+
    '@keyframes slideNoIn{from{opacity:0;transform:scale(.5)}to{opacity:1;transform:none}}'+
    '@keyframes slideLineIn{from{transform:scaleX(0)}to{transform:scaleX(1)}}'+
    '@media (prefers-reduced-motion:reduce){.slide-no,.slide-line{animation:none}}';
  document.head.appendChild(css);

  var label = stage.querySelector('.label');
  var b = document.createElement('div');
  b.className = 'slide-no';
  b.textContent = no;
  if(label){
    label.classList.add('numbered');
    label.prepend(b);
    var line = document.createElement('i');
    line.className = 'slide-line';
    label.appendChild(line);
  }else{
    b.style.cssText = 'position:absolute;right:62px;top:22px;z-index:20';
    stage.appendChild(b);
  }
})();
