(()=>{
  'use strict';
  const prefKey='kaibo-portfolio-language-v1';
  const current=()=>document.documentElement.lang.toLowerCase().startsWith('zh')?'zh':'en';
  function getPref(){try{return localStorage.getItem(prefKey);}catch(e){return null;}}
  function setPref(value){try{localStorage.setItem(prefKey,value);}catch(e){}}
  function target(lang){
    const path=location.pathname,isChinese=current()==='zh';
    const file=path.endsWith('/')?'index.html':(path.split('/').filter(Boolean).pop()||'index.html');
    const destination=lang==='zh'?(isChinese?file:'zh/'+file):(isChinese?'../'+file:file);
    return destination+(location.hash||'');
  }
  function choose(lang){setPref(lang);if(lang===current()){document.querySelector('.lang-dialog-backdrop')?.remove();document.body.classList.remove('lang-modal-open');return;}location.assign(target(lang));}
  function switcher(){
    const nav=document.querySelector('.nav-inner')||document.querySelector('nav .wrap');
    if(!nav)return;
    const holder=document.createElement('div');holder.className='lang-switch';holder.setAttribute('aria-label','Language / 语言');
    holder.innerHTML='<button type="button" data-site-lang="en" aria-pressed="'+(current()==='en')+'" aria-label="Switch to English">EN</button><button type="button" data-site-lang="zh" aria-pressed="'+(current()==='zh')+'" aria-label="切换到中文">中文</button>';
    holder.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>choose(b.dataset.siteLang)));
    nav.append(holder);
  }
  function welcome(){
    const backdrop=document.createElement('div');backdrop.className='lang-dialog-backdrop';
    backdrop.innerHTML='<div class="lang-dialog" role="dialog" aria-modal="true" aria-labelledby="lang-dialog-title"><div class="hello">KAIBO WANG / PERSONAL WEBSITE</div><h2 id="lang-dialog-title">Welcome. 欢迎。</h2><p>Choose your preferred language to explore my work.<br>选择你希望使用的语言，浏览我的项目和经历。</p><div class="lang-options"><button type="button" data-choose="en">English<span>View portfolio in English →</span></button><button type="button" data-choose="zh">简体中文<span>以中文浏览项目案例 →</span></button></div></div>';
    document.body.append(backdrop);document.body.classList.add('lang-modal-open');
    backdrop.querySelectorAll('[data-choose]').forEach(b=>b.addEventListener('click',()=>choose(b.dataset.choose)));
    backdrop.querySelector('button')?.focus();
  }
  function init(){switcher();const pref=getPref();if(pref!=='zh'&&pref!=='en')welcome();else if((location.pathname.endsWith('/index.html')||location.pathname.endsWith('/'))&&current()==='en'&&pref==='zh')location.replace(target('zh'));}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();