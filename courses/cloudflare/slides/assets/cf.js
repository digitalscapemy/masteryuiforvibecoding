// Shared helpers for the Cloudflare slides:
//  - injects the SVG symbols used everywhere (#cf cloud, #shop house, #bot, #user)
//  - opens / closes the PRO note (top-right)
//  - [data-go] buttons jump to another slide in the deck
(function(){
  var sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true">'+
    '<symbol id="cf" viewBox="0 0 64 40"><path d="M50.5 38H12.5C6.2 38 1 32.9 1 26.6c0-5.6 4-10.3 9.4-11.2C12 8.2 18.4 3 26 3c6.6 0 12.3 3.9 14.8 9.6 1.4-.6 2.9-.9 4.5-.9 6.1 0 11.1 4.6 11.7 10.6 3.9 1.2 6.9 4.9 6.9 9.2C63.9 36.3 58.4 38 50.5 38z"/></symbol>'+
    '<symbol id="shop" viewBox="0 0 64 64"><path d="M8 28v30h48V28" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linejoin="round"/><path d="M4 28 10 8h44l6 20z" fill="currentColor" opacity=".9"/><path d="M4 28c0 4 3.5 7 7 7s7-3 7-7c0 4 3.5 7 7 7s7-3 7-7c0 4 3.5 7 7 7s7-3 7-7c0 4 3.5 7 7 7s7-3 7-7" fill="none" stroke="#000" stroke-width="2.4"/><rect x="26" y="40" width="12" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="3.4"/><circle cx="32" cy="18" r="5" fill="#000"/></symbol>'+
    '<symbol id="bot" viewBox="0 0 48 48"><rect x="8" y="14" width="32" height="26" rx="8" fill="none" stroke="currentColor" stroke-width="3.4"/><circle cx="18" cy="27" r="3.6" fill="currentColor"/><circle cx="30" cy="27" r="3.6" fill="currentColor"/><path d="M24 14V6M18 34h12M4 24v8M44 24v8" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/><circle cx="24" cy="5" r="3" fill="currentColor"/></symbol>'+
    '<symbol id="user" viewBox="0 0 48 48"><circle cx="24" cy="15" r="9" fill="none" stroke="currentColor" stroke-width="3.4"/><path d="M7 44c1.5-9 8.5-14 17-14s15.5 5 17 14" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/></symbol>'+
    '<symbol id="lock" viewBox="0 0 24 24"><rect x="4.5" y="10.5" width="15" height="11" rx="2.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></symbol>'+
    '<symbol id="server" viewBox="0 0 48 48"><rect x="6" y="6" width="36" height="14" rx="4" fill="none" stroke="currentColor" stroke-width="3.2"/><rect x="6" y="26" width="36" height="14" rx="4" fill="none" stroke="currentColor" stroke-width="3.2"/><circle cx="14" cy="13" r="2.4" fill="currentColor"/><circle cx="14" cy="33" r="2.4" fill="currentColor"/><path d="M24 13h12M24 33h12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></symbol>'+
    '</svg>';
  document.body.insertAdjacentHTML('afterbegin', sprite);

  document.querySelectorAll('.pro > button').forEach(function(b){
    b.addEventListener('click', function(e){ e.stopPropagation(); b.parentElement.classList.toggle('open'); });
  });
  document.addEventListener('click', function(e){
    if(!e.target.closest('.pro')) document.querySelectorAll('.pro.open').forEach(function(p){ p.classList.remove('open'); });
  }, true);

  document.querySelectorAll('[data-go]').forEach(function(b){
    b.addEventListener('click', function(){
      if(window.top!==window) parent.postMessage({deck:'goto', slide:b.dataset.go}, '*');
      else location.href = 'cf-slide-'+b.dataset.go+'.html';
    });
  });
})();
