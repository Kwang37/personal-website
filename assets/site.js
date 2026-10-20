document.addEventListener('DOMContentLoaded',()=>{
 const isZh=document.documentElement.lang.toLowerCase().startsWith('zh');
 const menu=document.querySelector('[data-menu]'),links=document.querySelector('.nav-links');
 if(menu&&links){menu.addEventListener('click',()=>{const o=links.classList.toggle('open');menu.setAttribute('aria-expanded',String(o));});links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{links.classList.remove('open');menu.setAttribute('aria-expanded','false');}));}
 const filters=[...document.querySelectorAll('[data-filter]')],cards=[...document.querySelectorAll('.work-card[data-type]')];
 filters.forEach(b=>b.addEventListener('click',()=>{filters.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));cards.forEach(c=>c.dataset.hidden=String(b.dataset.filter!=='all'&&!c.dataset.type.split(' ').includes(b.dataset.filter)));}));
 const mails=isZh?[
 {title:'紧急密码重置要求',sender:'security-team@signin-care.org',detail:'要求员工通过陌生链接验证登录凭据，发件人域名与预期组织不匹配。',risk:'需要 IT 审核',state:'隔离并交由人工审核',safe:false},
 {title:'明天的排班更新',sender:'coordinator@clinic-example.org',detail:'来自预期发件人的常规排班通知，没有要求提供密码或敏感信息。',risk:'可能是常规邮件',state:'进入收件箱 / 可继续审核',safe:true},
 {title:'导出患者名单请求',sender:'vendor-support@external-help.org',detail:'非预期的患者名单导出要求，可能涉及受保护健康信息泄露。',risk:'潜在 PHI 风险',state:'隔离并交由人工审核',safe:false}
 ]:[
 {title:'Urgent password reset required',sender:'security-team@signin-care.org',detail:'Asks staff to verify their credentials through an unfamiliar link; the sender domain does not match the expected organization.',risk:'Needs IT review',state:'Quarantine for review',safe:false},
 {title:'Tomorrow’s staffing update',sender:'coordinator@clinic-example.org',detail:'Routine shift information from an expected sender, without requests for credentials or sensitive information.',risk:'Likely routine',state:'Inbox / reviewable',safe:true},
 {title:'Request to export patient list',sender:'vendor-support@external-help.org',detail:'Unexpected request for a patient list. Potential PHI exposure even if the language looks professional.',risk:'Potential PHI risk',state:'Quarantine for review',safe:false}
 ];
 const mailBtns=[...document.querySelectorAll('[data-mail]')],detail=document.getElementById('mail-detail');
 if(detail&&mailBtns.length){const show=i=>{const m=mails[i];mailBtns.forEach((b,j)=>b.setAttribute('aria-pressed',String(i===j)));detail.innerHTML='<div class="overline">'+(isZh?'模拟决策展示':'Illustrative decision walkthrough')+'</div><h3>'+m.title+'</h3><p class="small">'+m.sender+'</p><p>'+m.detail+'</p><span class="risk '+(m.safe?'safe':'')+'">'+m.risk+'</span><p><strong>UI action:</strong> '+m.state+'</p>';};mailBtns.forEach((b,i)=>b.addEventListener('click',()=>show(i)));show(0);}
 const path='https://github.com/UW-INFO442-AU25/GreenTail-G2/blob/main/';
 const journeys={
 quiz:{title:isZh?'01 / 引导式发现':'01 / Guided discovery',text:isZh?'五步 React 问卷收集宠物信息、需要避开的原料、喂养偏好、环境关注点与预算。QuizContext 在各步骤之间传递答案，无需强制账号注册。':'A five-step React quiz collects pet details, ingredient restrictions, feeding preferences, environmental priorities and budget. QuizContext carries answers across steps without requiring an account.',file:'src/QuizContext.jsx'},
 recommend:{title:isZh?'02 / 将匹配逻辑变得清晰':'02 / Fit over one-size-fits-all',text:isZh?'加权匹配结合宠物需求、预算与可持续性信息；结果页和比较页帮助用户理解推荐原因。':'Product matches rank pet suitability alongside budget and sustainability using an explicitly weighted scoring function. Results and comparison views explain the choices.',file:'src/utils/matchingAlgorithm.js'},
 map:{title:isZh?'03 / 寻找附近可购买的选项':'03 / Find in-store options',text:isZh?'React-Leaflet 地图弹窗根据 ZIP code 和品牌筛选模拟商店。门店及库存信息仅为演示数据。':'A React-Leaflet modal filters modeled nearby stores by ZIP code and selected brands. Store inventory and location data are simulated, not live availability.',file:'src/components/StoreMapModal.jsx'},
 learn:{title:isZh?'04 / 在购买前提供知识':'04 / Educate before purchase',text:isZh?'针对初次养宠者的教育模块嵌入 YouTube 内容，帮助用户先理解营养与喂养知识，再比较产品。':'The first-time-owner education flow integrates embedded YouTube guides for shoppers who need context before choosing products.',file:'src/components/YouTubeVideo.jsx'}
 };
 const tabs=[...document.querySelectorAll('[data-journey]')],journey=document.getElementById('journey-panel');
 if(journey&&tabs.length){const show=k=>{const j=journeys[k];if(!j)return;tabs.forEach(b=>b.setAttribute('aria-selected',String(b.dataset.journey===k)));journey.innerHTML='<div class="overline">'+(isZh?'用户流程 / 仓库证据':'User journey / repository-backed')+'</div><h3>'+j.title+'</h3><p>'+j.text+'</p><div class="source-row"><a class="source" target="_blank" rel="noopener noreferrer" href="'+path+j.file+'">'+(isZh?'查看源代码':'View source')+' ↗</a></div>';};tabs.forEach(b=>b.addEventListener('click',()=>show(b.dataset.journey)));show('quiz');}
 const langs=[...document.querySelectorAll('[data-lang]')],sentence=document.getElementById('locale-example');
 if(sentence&&langs.length){const phrases={en:'Create interactive stories with text, symbols, emoji, and code.',zh:'和我们一起用文字、符号、表情和代码创作互动故事吧！'};const show=k=>{langs.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.lang===k)));sentence.textContent=phrases[k];sentence.lang=k==='zh'?'zh-CN':'en';};langs.forEach(b=>b.addEventListener('click',()=>show(b.dataset.lang)));show('zh');}
 const save=document.getElementById('privacy-save'),result=document.getElementById('privacy-result');
 if(save&&result)save.addEventListener('click',()=>{try{localStorage.setItem('portfolio-greentail-privacy-demo','prefers-sustainable-options');result.textContent=isZh?'已保存在当前浏览器。本次演示不上传偏好。':'Saved in this browser. The portfolio demonstration does not transmit this preference to a server.';}catch(e){result.textContent=isZh?'当前环境无法访问 localStorage。':'Browser storage unavailable in this context.';}});
});