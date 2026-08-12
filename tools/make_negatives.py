#!/usr/bin/env python3
"""Recolor the final positive SVGs into negative (for dark bg) and on-red
variants. Positive palette: ink #1B1720 letters, #4A454F slogan text,
#8A8590 ghost stroke, #C4122E red dot/line."""
W="tools/_work"
def recolor(src, mapping):
    s=open(f"{W}/{src}.svg",encoding="utf-8").read()
    for a,b in mapping.items(): s=s.replace(a,b)
    return s
# negative (on dark): cream letters, keep red dot & ghost
NEG={"#1B1720":"#F2EEE6","#4A454F":"#B7B2BA"}
# on red bg: cream letters+slogan, pink ghost, ink dot/line
ONRED={"#1B1720":"#F2EEE6","#4A454F":"#F2EEE6","#8A8590":"#E39AA2","#C4122E":"#1B1720"}
out={
 "wm_principal_neg":recolor("wm_principal",NEG),
 "wm_principal_onred":recolor("wm_principal",ONRED),
 "wm_solo_neg":recolor("wm_solo",NEG),
 "wm_solo_onred":recolor("wm_solo",ONRED),
}
for k,v in out.items():
    open(f"{W}/{k}.svg","w",encoding="utf-8").write(v)
    print("wrote",k)
