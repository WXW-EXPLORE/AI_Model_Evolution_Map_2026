(()=>{
'use strict';
const DATA=ATLAS_DATA;
const $=id=>document.getElementById(id);
const escapeHTML=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const month=d=>{const [y,m]=d.split('-').map(Number);return (y-2017)*12+(m-1)};
const ym=d=>d?.replace('-',' / ')||'';
const familyById=Object.fromEntries(DATA.families.map(x=>[x.id,x]));
const modelById=Object.fromEntries(DATA.models.map(x=>[x.id,x]));
const skills=DATA.skills;
let currentTab='timeline', activeSkill='', showAll=false, geo='all', range='2023', zoom=1, query='', selectedId=null;
const xmlns='http://www.w3.org/2000/svg';
function svgTag(name,attr={},child=''){const at=Object.entries(attr).map(([k,v])=>` ${k}="${escapeHTML(v)}"`).join('');return `<${name}${at}>${child}</${name}>`}
const color=d=>familyById[d]?.color||'#4b8d86';
function skillDots(arr,x,y,max=4){return arr.slice(0,max).map((t,i)=>svgTag('circle',{cx:x+i*10,cy:y,r:3.3,fill:skills[t]?.[1]||'#abc'})).join('')}
function setTab(tab){currentTab=tab;document.querySelectorAll('.nav').forEach(n=>n.classList.toggle('active',n.dataset.tab===tab));document.querySelectorAll('.tab-panel').forEach(e=>e.classList.toggle('active',e.id==='panel-'+tab));if(tab==='matrix')renderMatrix();if(tab==='harness')renderHarness();if(tab==='benchmark')renderBenchmark();if(tab==='timeline')requestAnimationFrame(()=>renderModels(false));closeDetail()}
function shade(s,n){return s.length>n?s.slice(0,n-1)+'…':s}
function renderModels(keepScroll=true){
 const viewport=$('mapViewport'),prevX=viewport.scrollLeft,prevY=viewport.scrollTop;
 let families=DATA.families.filter(f=>f.id!=='技术源流'||range==='2017');
 if(geo==='china')families=families.filter(f=>f.region==='china');
 if(geo==='global')families=families.filter(f=>f.region==='global');
 if(!showAll&&geo==='all')families=families.filter(f=>['OpenAI','Anthropic','Google Gemini','Meta Llama','Alibaba Qwen','DeepSeek','Mistral','Google Gemma','Moonshot Kimi','Z.ai GLM'].includes(f.id)||(range==='2017'&&f.id==='技术源流'));
 $('focusBtn').textContent=showAll?'☷ 仅看主要家族':'☷ 展示全部家族';
 const start=month(range+'-01'),end=month('2026-12'),mScale=range==='2025'?61:range==='2023'?40:21;
 const LEFT=198,HEAD=74,ROW=108,NODE_W=140,NODE_H=29, width=LEFT+(end-start)*mScale+NODE_W+36,height=HEAD+ROW*families.length+30;
 let out=`<title>AI 模型家族时间轴；横轴月份，纵轴机构，点击节点查看细节。</title>`;
 out+=`<rect width="${width}" height="${height}" fill="#fcfdfc"/>`;
 for(let year=Number(range);year<=2026;year++){
   const x=LEFT+(month(year+'-01')-start)*mScale;
   out+=svgTag('rect',{x,y:0,width:12*mScale,height:height,fill:year%2===0?'#f4f8f7':'#fbfcfb'});
   out+=svgTag('line',{x1:x,y1:52,x2:x,y2:height-18,stroke:'#dce7e4','stroke-width':1});
   out+=svgTag('text',{x:x+10,y:29,fill:'#3d605b','font-size':16,'font-weight':750,class:'map-text'},String(year));
   [4,7,10].forEach(m=>{const qx=x+(m-1)*mScale;out+=svgTag('line',{x1:qx,y1:52,x2:qx,y2:height-18,stroke:'#edf2f0','stroke-dasharray':'3 6'});});
 }
 out+=svgTag('text',{x:22,y:29,fill:'#84938f','font-size':11,class:'map-text'},'研发机构 / 模型家族');
 const nodePositions=[];
 families.forEach((f,ix)=>{
  const y=HEAD+ix*ROW;
  out+=svgTag('rect',{x:0,y:y-12,width:width,height:ROW,fill:ix%2?'#fff':'#f9fbfa','fill-opacity':.62});
  out+=svgTag('line',{x1:0,y1:y+ROW-12,x2:width,y2:y+ROW-12,stroke:'#e5ece9'});
  out+=svgTag('rect',{x:20,y:y+33,width:4,height:24,rx:2,fill:f.color});
  const label=shade(f.label,24);
  out+=svgTag('text',{x:34,y:y+46,fill:'#2b4540','font-size':12,class:'map-text lane-name'},escapeHTML(label));
  const mod=DATA.models.filter(d=>d.family===f.id&&month(d.date)>=start&&month(d.date)<end).sort((a,b)=>month(a.date)-month(b.date));
  const ends=[-200,-200,-200];let pos=[];
  mod.forEach(d=>{
    let x=LEFT+(month(d.date)-start)*mScale;
    let track=ends.findIndex(e=>x>e+7);
    if(track<0){track=ends.indexOf(Math.min(...ends));}ends[track]=x+NODE_W;
    const ny=y+2+track*31;
    pos.push({d,x,y:ny});nodePositions.push({d,x,y:ny});
  });
  // Within-family chronological connector; illustrative family continuity, not direct checkpoint ancestry.
  for(let i=1;i<pos.length;i++){
    const a=pos[i-1],b=pos[i],x1=a.x+NODE_W-4,y1=a.y+NODE_H/2,x2=b.x+4,y2=b.y+NODE_H/2;
    if(x2>x1+8)out+=svgTag('path',{d:`M ${x1} ${y1} C ${x1+Math.min(35,(x2-x1)/2)} ${y1} ${x2-Math.min(35,(x2-x1)/2)} ${y2} ${x2} ${y2}`,stroke:f.color,'stroke-opacity':'.55','stroke-width':1.6,fill:'none','stroke-linecap':'round'});
  }
 });
 for(const {d,x,y} of nodePositions){
   const f=familyById[d.family],dim=(activeSkill&&!d.skills.includes(activeSkill))||(query&&!(`${d.name} ${d.family} ${d.summary}`.toLowerCase().includes(query.toLowerCase())));
   const isOpen=d.access.includes('开放')||d.access.includes('开源')||d.access==='论文';
   const groupCls=['node',dim?'dim':'',selectedId===d.id?'selected':''].filter(Boolean).join(' ');
   const textName=shade(d.name,18);
   out+=`<g class="${groupCls}" data-id="${escapeHTML(d.id)}" role="button" tabindex="0" aria-label="${escapeHTML(d.name+' '+d.date)}">`;
   out+=`<title>${escapeHTML(d.name+' · '+d.date+' · '+d.skills.map(x=>skills[x][0]).join(' / '))}</title>`;
   out+=svgTag('rect',{class:'node-bg',x,y,width:NODE_W,height:NODE_H,rx:5,fill:isOpen?'#eff8f4':'#fff9f5',stroke:isOpen?'#a5d1c2':'#dfcabb'});
   out+=svgTag('rect',{x,y:y+3,width:3,height:NODE_H-6,rx:1.5,fill:f.color});
   out+=svgTag('text',{x:x+9,y:y+12.2,fill:'#314943','font-size':10.6,'font-weight':700,class:'map-text'},escapeHTML(textName));
   out+=skillDots(d.skills,x+12,y+21,5);
   out+=svgTag('text',{x:x+NODE_W-8,y:y+23,fill:'#8e9d96','font-size':9,'text-anchor':'end',class:'map-text'},escapeHTML(d.date.slice(5)));
   out+='</g>';
 }
 const svg=$('modelSvg');svg.setAttribute('viewBox',`0 0 ${width} ${height}`);svg.setAttribute('width',Math.round(width*zoom));svg.setAttribute('height',Math.round(height*zoom));svg.innerHTML=out;
 $('mapTitle').textContent=`${families.length} 条家族泳道 · ${nodePositions.length} 个模型节点`;
 $('mapSub').textContent=`${range}—2026.11 / 各节点是代表性发布，不是完整产品版本列表`;
 $('zoomPct').textContent=Math.round(zoom*100)+'%';
 if(keepScroll){viewport.scrollLeft=prevX;viewport.scrollTop=prevY;}else{viewport.scrollLeft=0;viewport.scrollTop=0}
 }
function openModel(id){const d=modelById[id];if(!d)return;selectedId=id;renderModels(true);openDetail('model',d)}
function openDetail(type,d){
 const container=$('detailContent');
 let summary='',title='',org='',date=d.date,fields=[],url='',pills=[];
 if(type==='model'){
 title=d.name;org=familyById[d.family]?.label;summary=d.summary;url=d.source;pills=d.skills.map(s=>({text:skills[s][0],color:skills[s][1]}));
 fields=[['发布月份',d.date],['模型家族',org],['公开方式',d.access],['架构路径',d.architecture],['信息类型','代表性研究定位 / 非统一实测排名'],['来源类型',d.evidence]];
 }else if(type==='harness'){
 title=d.name;org=d.origin;summary=d.desc;url=d.url;pills=[{text:d.kind,color:'#438779'},{text:d.skill,color:'#d18a66'}];fields=[['初次公开月份',d.date],['机构',d.origin],['分层类别',d.kind],['主要用途',d.skill]];
 }else{title=d.name;org=d.kind;summary=d.desc;url=d.url;pills=[{text:d.kind,color:'#438779'}];fields=[['首次公开月份',d.date],['测量对象',d.kind],['独立于模型','必须注明协议、工具与评测版本']];}
 container.innerHTML=`<div class="detail-date">${escapeHTML(date)}</div><h2 class="detail-title">${escapeHTML(title)}</h2><div class="detail-org">${escapeHTML(org)}</div><div class="detail-pills">${pills.map(p=>`<span class="detail-pill" style="border-left:3px solid ${p.color}">${escapeHTML(p.text)}</span>`).join('')}</div><div class="detail-summary">${escapeHTML(summary)}</div><div class="detail-table">${fields.map(([a,b])=>`<div class="detail-tr"><span>${escapeHTML(a)}</span><b>${escapeHTML(b)}</b></div>`).join('')}</div><div class="detail-warning">本地图标示的是研究定位，不是通过同一实验协议复现的性能分数。模型系列迭代不自动等于对前一代权重进行持续训练。</div><a class="detail-link" href="${escapeHTML(url)}" target="_blank" rel="noopener noreferrer">打开原始资料 / 官方说明 ↗</a>`;
 $('detailBackdrop').hidden=false;$('detailDrawer').classList.add('open');$('detailDrawer').setAttribute('aria-hidden','false');
 }
function closeDetail(){$('detailBackdrop').hidden=true;$('detailDrawer').classList.remove('open');$('detailDrawer').setAttribute('aria-hidden','true')}
function renderMatrix(){
 const all=DATA.families.filter(f=>f.id!=='技术源流');const codes=Object.keys(skills);
 let s=`<table class="matrix-table"><thead><tr><th>模型家族</th>${codes.map(c=>`<th>${escapeHTML(skills[c][0])}</th>`).join('')}</tr></thead><tbody>`;
 for(const f of all){const vals=DATA.models.filter(d=>d.family===f.id);s+=`<tr><td><div class="family-side"><i style="background:${f.color}"></i>${escapeHTML(f.label)}</div></td>`;
 for(const c of codes){const n=vals.filter(d=>d.skills.includes(c)).length;s+=`<td><span class="matrix-cell ${n?'has':''}" title="${escapeHTML(f.label)}: ${n}个收录节点带此标签">${n?'●':'·'}</span></td>`;}s+='</tr>';
 }s+='</tbody></table>';$('matrixArea').innerHTML=s;
}
function renderGeneric(svgId,items,categories,startStr,endStr,type){
 const left=185,head=65,row=83,NODE_W=140,NODE_H=29,start=month(startStr),end=month(endStr),scale=44,w=left+(end-start)*scale+NODE_W+27,h=head+row*categories.length+30;
 let html=`<rect width="${w}" height="${h}" fill="#fcfdfc"/>`;
 for(let y=Number(startStr.slice(0,4));y<=Number(endStr.slice(0,4));y++){let x=left+(month(y+'-01')-start)*scale;html+=svgTag('line',{x1:x,y1:39,x2:x,y2:h,stroke:'#e0e9e5'});html+=svgTag('text',{x:x+8,y:25,'font-size':15,'font-weight':700,fill:'#3d6b63'},String(y))}
 categories.forEach((cat,i)=>{
   const cy=head+i*row;html+=svgTag('rect',{x:0,y:cy-11,width:w,height:row,fill:i%2?'#fff':'#f4f8f6'});
   html+=svgTag('text',{x:18,y:cy+31,'font-size':12,fill:'#315750','font-weight':700},escapeHTML(cat));
   const r=items.filter(d=>d.kind===cat&&month(d.date)>=start&&month(d.date)<end).sort((a,b)=>month(a.date)-month(b.date));let ends=[-100,-100];
   for(const d of r){const x=left+(month(d.date)-start)*scale;let t=ends.findIndex(e=>x>e+5);if(t<0)t=ends.indexOf(Math.min(...ends));ends[t]=x+NODE_W;const y=cy-4+t*33;const id=items.indexOf(d);
   html+=`<g class="node" data-type="${type}" data-index="${id}" role="button" tabindex="0"><title>${escapeHTML(d.name+': '+d.desc)}</title><rect class="node-bg" x="${x}" y="${y}" width="${NODE_W}" height="${NODE_H}" rx="5" fill="#f3f8f5" stroke="#add0c3"/><text x="${x+9}" y="${y+13}" font-size="10.8" fill="#2d534a" font-weight="700">${escapeHTML(shade(d.name,19))}</text><text x="${x+9}" y="${y+24}" font-size="9" fill="#859a90">${escapeHTML(d.date)}</text></g>`;}
 });
 const svg=$(svgId);svg.setAttribute('viewBox',`0 0 ${w} ${h}`);svg.setAttribute('width',w);svg.setAttribute('height',h);svg.innerHTML=html;
}
function cards(id,items){const arr=items.slice().sort((a,b)=>month(b.date)-month(a.date));$(id).innerHTML=arr.map(d=>`<article class="info-card"><div class="date">${escapeHTML(d.date)} · ${escapeHTML(d.kind)}</div><h3>${escapeHTML(d.name)}</h3><p>${escapeHTML(d.desc)}</p><a href="${escapeHTML(d.url)}" target="_blank" rel="noopener noreferrer">官方项目 / 文献 ↗</a></article>`).join('')}
let didHarness=false,didBench=false,didMatrix=false;
function renderHarness(){if(didHarness)return;renderGeneric('harnessSvg',DATA.harness,['开发框架','数据/RAG','多Agent','Agent Harness'],'2022-01','2027-01','harness');cards('harnessCards',DATA.harness);didHarness=true}
function renderBenchmark(){if(didBench)return;renderGeneric('benchmarkSvg',DATA.benchmarks,['知识','代码','数学','科学','多模态','对话','Agent系统','工具调用','评测平台'],'2020-01','2026-01','benchmark');cards('benchmarkCards',DATA.benchmarks);didBench=true}
function exportSVG(){const id=currentTab==='harness'?'harnessSvg':currentTab==='benchmark'?'benchmarkSvg':'modelSvg',svg=$(id);if(!svg||!svg.innerHTML){setTab('timeline');return;}const copy=svg.cloneNode(true);copy.setAttribute('xmlns',xmlns);const xml='<?xml version="1.0" encoding="UTF-8"?>\n'+new XMLSerializer().serializeToString(copy);const blob=new Blob([xml],{type:'image/svg+xml;charset=utf-8'});const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download=`AI_${currentTab}_2026.svg`;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000)}
function renderQuickOverview(){
 const representatives={
 'OpenAI':['GPT-4','GPT-4o','GPT-5','GPT-6 Astra'],
 'Anthropic':['Claude 1','Claude 3.5 Sonnet','Claude 4 (Opus/Sonnet)','Claude Fable 5.2'],
 'Google Gemini':['Gemini 1.0','Gemini 1.5 Pro','Gemini 3 Pro','Gemini 3.8 Flash'],
 'Meta Llama':['Llama 2','Llama 3','Llama 4 Scout/Maverick',null],
 'Alibaba Qwen':['Qwen 1','Qwen2.5 / Coder / Math','Qwen3','Qwen3.8'],
 'DeepSeek':[null,'DeepSeek-V3','DeepSeek-R1','DeepSeek-V4 Pro / Flash'],
 'Moonshot Kimi':['Kimi / Moonshot v1',null,'Kimi K2','Kimi K2.5'],
 'Z.ai GLM':['ChatGLM-6B','GLM-4','GLM-4.5','GLM-5.3 / Flash'],
 'Mistral':['Mistral 7B','Codestral','Mistral Large 3','Mistral Small 4'],
 'Google Gemma':[null,'Gemma 1','Gemma 3','Gemma 4']};
 let html='<div class="quick-table"><div class="quick-year">MODEL FAMILY</div>';
 html+=[2023,2024,2025,2026].map(y=>`<div class="quick-year">${y}${y===2026?' · 最新':''}</div>`).join('');
 for(const [f,names] of Object.entries(representatives)){
   const ff=familyById[f];html+=`<div class="quick-family"><i style="background:${ff.color}"></i>${escapeHTML(ff.label)}</div>`;
   names.forEach((name,idx)=>{
     const d=DATA.models.find(m=>m.name===name&&m.family===f);
     html+=`<div class="quick-cell ${idx===3?'latest':''}">`;
     if(d)html+=`<button class="quick-pill" data-model="${escapeHTML(d.id)}" style="--fcolor:${ff.color}" title="${escapeHTML(d.name+' / '+d.date+' / '+d.skills.map(s=>skills[s][0]).join(', '))}"><span class="quick-name">${escapeHTML(d.name)}</span><span class="quick-skill-dots">${d.skills.slice(0,3).map(s=>`<i style="background:${skills[s][1]}" title="${escapeHTML(skills[s][0])}"></i>`).join('')}</span></button>`;
     else html+='<span class="quick-empty" title="本年度未选代表节点"></span>';
     html+='</div>';
   });
 }
 html+='</div><div class="mini-caption">年度代表选取不代表全年只发布一款模型，也不表示同年度内的先后顺序；精确到月的节点在下方时间图中查看。</div>';
 $('quickOverview').innerHTML=html;
 $('quickOverview').addEventListener('click',e=>{const b=e.target.closest('.quick-pill');if(b)openModel(b.dataset.model)});
}
const filterHtml=[''].concat(Object.keys(skills)).map(s=>`<button class="skill-filter ${!s?'active':''}" data-skill="${s}">${s?`<i style="background:${skills[s][1]}"></i>${escapeHTML(skills[s][0])}`:'全部方向'}</button>`).join('');$('skillFilters').innerHTML=filterHtml;
$('skillFilters').addEventListener('click',e=>{const el=e.target.closest('.skill-filter');if(!el)return;activeSkill=el.dataset.skill;document.querySelectorAll('.skill-filter').forEach(b=>b.classList.toggle('active',b===el));renderModels()});
document.querySelectorAll('.nav').forEach(b=>b.addEventListener('click',()=>setTab(b.dataset.tab)));
$('timeRange').addEventListener('change',e=>{range=e.target.value;zoom=1;renderModels(false)});
$('geoRange').addEventListener('change',e=>{geo=e.target.value;renderModels(false)});
$('focusBtn').addEventListener('click',()=>{showAll=!showAll;renderModels()});
$('modelSearch').addEventListener('input',e=>{query=e.target.value.trim();renderModels(true);if(query.length<2)return;let found=DATA.models.find(d=>d.name.toLowerCase().includes(query.toLowerCase())&&month(d.date)>=month(range+'-01'));if(found){const node=Array.from($('modelSvg').querySelectorAll('.node')).find(n=>n.dataset.id===found.id);if(node){const view=$('mapViewport');const x=node.getBBox().x*zoom,y=node.getBBox().y*zoom;view.scrollTo({left:Math.max(0,x-view.clientWidth/2),top:Math.max(0,y-view.clientHeight/3),behavior:'smooth'})}}});
$('clearFilters').addEventListener('click',()=>{range='2023';geo='all';showAll=false;activeSkill='';query='';zoom=1;$('timeRange').value=range;$('geoRange').value=geo;$('modelSearch').value='';document.querySelectorAll('.skill-filter').forEach(b=>b.classList.toggle('active',b.dataset.skill===''));renderModels(false)});
$('modelSvg').addEventListener('click',e=>{const node=e.target.closest('.node');if(node?.dataset.id)openModel(node.dataset.id)});
$('modelSvg').addEventListener('keydown',e=>{const node=e.target.closest('.node');if((e.key==='Enter'||e.key===' ')&&node?.dataset.id){e.preventDefault();openModel(node.dataset.id)}});
for(const [elementName,type] of [['harnessSvg','harness'],['benchmarkSvg','benchmark']]){
$(elementName).addEventListener('click',e=>{const node=e.target.closest('.node');if(node){const arr=type==='harness'?DATA.harness:DATA.benchmarks;openDetail(type,arr[Number(node.dataset.index)])}});
$(elementName).addEventListener('keydown',e=>{const node=e.target.closest('.node');if(node&&(e.key==='Enter'||e.key===' ')){e.preventDefault();const arr=type==='harness'?DATA.harness:DATA.benchmarks;openDetail(type,arr[Number(node.dataset.index)])}})}
$('zoomIn').addEventListener('click',()=>{zoom=Math.min(1.7,zoom+.15);renderModels()});$('zoomOut').addEventListener('click',()=>{zoom=Math.max(.7,zoom-.15);renderModels()});
$('closeDrawer').addEventListener('click',closeDetail);$('detailBackdrop').addEventListener('click',closeDetail);document.addEventListener('keydown',e=>{if(e.key==='Escape')closeDetail()});$('exportBtn').addEventListener('click',exportSVG);
renderQuickOverview();$('countM').textContent=DATA.models.length;$('countF').textContent=DATA.families.length;renderModels(false);
window.__atlasDebug=()=>({models:DATA.models.length,families:DATA.families.length,harness:DATA.harness.length,benchmarks:DATA.benchmarks.length,tab:currentTab,svgNodes:$('modelSvg').querySelectorAll('.node').length});
})();