import json,csv,re,statistics,datetime,collections
import os
HERE=os.path.dirname(os.path.abspath(__file__))
A=os.path.join(HERE,'..','data')+'/'
rows={r['id']:r for r in csv.DictReader(open(A+'princess-tower-all-210-listings.csv'))}
S={str(x['id']):x for x in json.load(open(A+'raw/search-results-210.json'))}
D=json.load(open(A+'raw/detail-pages-47.json'))
now=datetime.date(2026,11,27)
def norm(t): return re.sub(r'[^a-z ]','',(t or '').lower())
# copy-paste: shingle overlap
def sh(t):
    w=norm(t).split(); return set(tuple(w[i:i+6]) for i in range(len(w)-5))
shs={i:sh(S[i].get('description')) for i in S}
out=[]
for i,dd in D.items():
    r=rows[i]; s=S[i]; desc=(s.get('description') or '')+' '+(s.get('title') or '')
    f={}
    vs=float(r['vs_tower_median_pct'] or 0); price=float(r['price_aed']); size=float(r['size_sqft'])
    f['F1_above_median']=vs>25
    tx=[float(t['amount']) for t in (dd.get('tx') or {}).get(r['type'] if r['type']=='rent' else 'buy',[]) or [] if abs(t['size']-size)<=5]
    reg=(price/statistics.median(tx)-1)*100 if tx else None
    f['F2_above_registered']=reg is not None and reg>25
    # photos with a different unit
    pg=r['photo_group']; diff=False
    if pg:
        for j,o in rows.items():
            if j!=i and o['photo_group']==pg and (abs(float(o['size_sqft'])-float(r['size_sqft']))>20 or o['baths']!=r['baths']): diff=True
    f['F3_photos_other_unit']=diff
    hol=bool(dd.get('dtcm')) or bool(re.search(r'holiday|bills included|no emirates id|dtcm|valid for the current month|serviced',desc,re.I))
    f['F4_holiday_in_yearly']=r['type']=='rent' and hol
    permit=bool((dd.get('rera') or {}).get('permit_validation_url'))
    f['F5_no_permit_or_badge']=(not permit) or r['verified']!='True'
    cp=any(len(shs[i]&shs[j])>=0.5*max(1,min(len(shs[i]),len(shs[j]))) and rows[j]['broker']==r['broker'] and (rows[j]['size_sqft']!=r['size_sqft'] or rows[j]['beds']!=r['beds']) for j in S if j!=i and shs[j] and shs[i])
    f['F6_copy_paste']=cp
    f['F7_charm']=bool(re.search(r'(899|999|888|499)$',str(int(price))))
    f['W1_over90d']=int(r['age_days'])>(90 if r['type']=='rent' else 180)
    av=dd.get('avail'); f['W2_stale_avail']=bool(av) and (now-datetime.date.fromisoformat(av[:10])).days>60
    f['W3_cheap']=vs<-15
    out.append(dict(id=i,type=r['type'],beds=r['beds'],broker=r['broker'],price=price,vs=vs,reg=None if reg is None else round(reg),verdict=r['verdict'] or 'Trustworthy',**f))
json.dump(out,open(os.path.join(HERE,'flags.json'),'w'),indent=1)
c=collections.defaultdict(collections.Counter)
for o in out:
    for k,v in o.items():
        if k[:1] in 'FW' and k[1].isdigit() and v: c[k][o['verdict']]+=1
for k in sorted(c): print(k,dict(c[k]))
print(collections.Counter(o['verdict'] for o in out))
