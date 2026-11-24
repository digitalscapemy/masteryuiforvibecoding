// Shared runtime for every slide: fit the 1920×1080 stage, talk to the deck, copy buttons.
(function(){
  var stage = document.getElementById('stage');
  function fit(){ stage.style.setProperty('--s', Math.min(innerWidth/1920, innerHeight/1080)); }
  addEventListener('resize', fit); fit();

  // clicks on buttons/links stay inside the slide; anywhere else advances the deck
  var INTERACTIVE = 'button,a,input,select,textarea,label,[data-tap]';
  var inDeck = window.top !== window;
  addEventListener('click', function(e){
    if(e.target.closest(INTERACTIVE)) return;
    if(inDeck) parent.postMessage({deck:'click'}, '*');
  });
  addEventListener('keydown', function(e){
    if(e.target.closest('input,textarea')) return;
    if(inDeck){ e.preventDefault(); parent.postMessage({deck:'key', key:e.key}, '*'); }
    else if(e.key==='r' || e.key==='R') location.reload();
  });

  // [data-copy] buttons copy the text of the element they point to
  document.querySelectorAll('[data-copy]').forEach(function(b){
    b.addEventListener('click', function(){
      var src = document.querySelector(b.getAttribute('data-copy'));
      var text = src ? src.textContent.trim().replace(/^[“"]|[”"]$/g,'') : '';
      var done = function(){ var t=b.innerHTML; b.textContent='Copied ✓'; b.classList.add('on'); setTimeout(function(){ b.innerHTML=t; b.classList.remove('on'); },1400); };
      if(navigator.clipboard && window.isSecureContext){ navigator.clipboard.writeText(text).then(done, fallback); } else fallback();
      function fallback(){ var ta=document.createElement('textarea'); ta.value=text; document.body.appendChild(ta); ta.select();
        try{ document.execCommand('copy'); }catch(_){} ta.remove(); done(); }
    });
  });
})();
