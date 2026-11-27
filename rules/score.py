import json,collections,sys
import os
HERE=os.path.dirname(os.path.abspath(__file__))
out=json.load(open(os.path.join(HERE,'flags.json')))
F8={'176035638':'sale listing says "for rent"','165059354':'title and body give different floors','175557756':'unfurnished in title, furnished in body','114610923':'size matches no other 3BR','177811402':'twin listing says tenanted','177811349':'twin listing says vacant','176064041':'availability date 16 months before posting','179160264':'"Big Price Drop" with no price change','152822434':'size unusual for a 2BR','169246380':'same penthouse listed twice','171950867':'same penthouse listed twice','167438609':'same penthouse listed twice','169275339':'"Agents welcome": listing agent may not hold the mandate'}
W=dict(F1_above_median=30,F2_above_registered=20,F3_photos_other_unit=40,F4_holiday_in_yearly=30,F5_no_permit_or_badge=20,F6_copy_paste=15,F7_charm=5,F8_contradiction=20,W1_over90d=5,W2_stale_avail=5,W3_cheap=5)
def score(o):
    o['F8_contradiction']=o['id'] in F8
    s=100; hit=[]
    for k,w in W.items():
        if o.get(k): s-=w; hit.append(k)
    if o['W3_cheap'] and (o['F3_photos_other_unit'] or o['F6_copy_paste']): s-=10; hit.append('BAIT')
    return max(0,s),hit
def band(s): return 'Short list' if s>=85 else ('Not sure' if s>50 else 'Likely misleading')
M={'Trustworthy':'Short list','Suspicious':'Not sure','Likely misleading':'Likely misleading'}
cm=collections.Counter(); res=[]
for o in out:
    s,h=score(o); b=band(s); cm[(o['verdict'],b)]+=1; res.append((o['verdict'],s,b,o['id'],o['type'],o['beds'],o['vs'],o['reg'],h))
for r in sorted(res,key=lambda r:(r[0],r[1])): print(r)
print(cm)
print('agree',sum(v for (a,b),v in cm.items() if M[a]==b),'/',len(out))
json.dump(res,open(os.path.join(HERE,'scores.json'),'w'))
