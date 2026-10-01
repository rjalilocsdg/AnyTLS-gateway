# CFM Python 3.12 distribution. See README.md.
def _cfm_77f7df45a7cdcbc3():
    import base64, hashlib, marshal, sys, zlib
    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("CFM requires Python 3.12; deploy using the supplied Dockerfile")
    parts = (
        (9, 'tY5M(-wTyD8{xQTWAEQlieN6u=9z~DYozoiZ1EVtEqkI~b5l)ZiRZ+B%Pf2BBhhiCDm;)@}1**x)1w+J6K17=S$>7d42lZNeYIivNRZzYn3jd5)%'),
        (4, 'bc>MgVLXRhvB;@?&=Cb@ay8;u&3h-aiM-bW&=zte0j2P{ojp?*1tEU`dp$-7{^1boKhA)1ZcwHHYmXJuGbf&EauL0Hn#CSZsQXr_G1APkpv5=KqP'),
        (0, '$(HZ?1j}evIN^bHdP;EOq2i7Dn^y65cp*8n5Cw)KBSz`^KFjo+E&O^PzG8+GNyh{PB0%gpR}8Ef5VWf*i|ASa-up>K0cIqwV*;T#4o0nROP4BDrB'),
        (6, '%aVxDVT)49iSBg$ECT0A1TIhjfG2*DgF`o@8nD6+#F5wTJCZVu^=@{52p$SyzLelZq+Q?=gA7O|OuanYFS<Jz@8`&LtdqL}fG0m@J(XxT^t=$I?l'),
        (12, '@yRK*CD%D%lD!g-GQmD972lnnlMWTv#`FF<+N6U1DvfNwn6gFOR+067%YTU^~dhh~i4mA>kc}90SK*1wT+IfhX#DP>OnsMt1*5GdIpfdhXw;gEPe'),
        (14, 'IiAs35O`Ck-2c%IvMP*BOkzJTQ#IwP9X$Y`ImjL}b4m$e`-0g-8Dmqb-4rcT9##Jm3PwSyqzNi{bxudL5r`}4YvWVX*MBK``p+3wYbfs|!8jO2Ir'),
        (10, ')xzJ^QlGk=7;&RBh;Q2rh6%thwiE58bD;D6dAv%w`21}cOVWxrNd_Dha**JnYn75=Ne8)arb^^l_lztP__`MRS0=c>Zl@ru;G+=mP?SadhcLUuW_'),
        (7, 'VXeh<MQQ?XZ2JvChO|=#mh1MYZV~en`{By5pg-1oeV+SIEZb*A>1>fK{h(oQ={y(;dZVr-$H8IMAcPMLu7GD%!>R9I~^Byr4sU&k({z80m$lH11k'),
        (19, 'QO!AKV8Cu%(d&aR!?qpSqLwpgf6^{HyQ=Cx2=J9&15CTkzq?E$o#xeS_9c@v?7K~x}ztW$_v#zR)@Xw1Dah=<vNb)F!{Wu6XUD%c4o0e3KT;jhXj'),
        (16, 'x_aYb@FGg<w`pwUQ~D&MtIH3C&Mo)ntT&jYhc0K}+S>25{r?op7-|KTHcD6R%TId!GO>5v8!S9gT9)C?5-zfA9AA$rvQ(>Fcdb*gf>0INaAOi=S_'),
        (1, 'X{=kICKwvXF@hTbO)|Hr1<s;;mmhRAb;D{XGwXADC0~m-ZV&2FOQ#c?-68lnDyEX@a^>V6mgB)=7eQ%A$ZJs=X3mdh?*R9@e_C-X&Ha-G>#kCU%;'),
        (15, '@CYkj`Ksm7imG+J+mmI-MUO6Zv<)Q)pxb@3Y2Zjkumn#lq&uw|xQQK~xtbT<18}l};|zuk%>2!D@*TF?m|yB{3A1td$qsoqGdPvTbYE$-dTu(>Kx'),
        (18, 'iy^$E;+i_Iy)!`4eNTE5K`Oseu(FfQJE(g4VYu8<*g`THv9bp(>I&lNIW}dwT!aPRu70m$iMD`*p2F{r?(zLvT(czEL@U`=I;xRN@qv}vejSY;?%'),
        (2, 'Q;Bs&&`j-~Aqm7;uK9N&}t`6Mz04?i(k^}h52A8~3i7v4QzH84qtcF^1{_>OtV*ycx1>K-`kcIDNzK;&nEy(qf2G1nx*MDJrHivGh0KLVXg8remW'),
        (3, '%h%#WOdMGgi56~GXyZ1xk#DJ>7IqtUd{hjgiKmB!2T+Qm$6N6FXW)=PPJPdbw8F315X#Ee^3iG)t5O{c33g0K^z%H8Jg6Yq4`WL)A~oP_KISxl5s'),
        (20, '#0+&X0b7V|ZWI4uyV{Wd$-flVmlpM-_mHP7@q&*FCWt_Ona(+sA5O)PA9zce6dgdF3|~VrhnwGpoo{n4DRilkLrk{kdtXR0MGUa$Cc&y_NpvwHFg'),
        (5, '62OPpsW$U|_|Q5*09C*Zy2HN^e>Jy57VxSBPPNzUTs3W?+&9hDUJPmU25Ss{7$<GjgTZ^ul@dr1YHF5MqeD3F*U_zOU;fH$7R8$HewAyKARcDg)&'),
        (21, 'wA`1sl>`<z@%>g9%%lz*Flpa!zTL?4L7gq5uq9U^~Jo9!?>&9%GBGI{D=4{s0poNiZ1NTm'),
        (17, 'cT^~T06Nw~>BSaOzkiS36$1e@sj$G+M!msFSx?wya0Ej`3ehH}*mk&q{pDOAu6zIBS73QO3>V~}m4y;5ba^Da&?D_2NeJRA2v_X~fHA{-1=0iOK;'),
        (8, 'UK`87eArp6ILr`nW4Z>Z(s`q4k*3FjrwFG08t8;SD3s{`kdvXTZ*Z#Nldq=2iNa@$VLF5xFDpAT#C{?J=mv4s}r&9GLS;}l^O8$ZV?AUvb=}iJTD'),
        (13, '9RC9wCt~FhdapwE)l2f0QrW<X=Q8g?sGu9wZgEacX`XFw^eE|{-7h7^j`VQkJv8Ha-I&&Ug&39!Kh#-Ul$t76^#m^m|po%7V;ck*)XRj{VUI6+9}'),
        (11, 'J){r=snfJN%-=q_zgvtD-*|d1oxOPg<?XjjSoqy)JULk{E|H8<dU%?Lu4|3KacQZ-uo9_VqG=R_5VuFko8Hz2cor3*-6WEhHJj5w^i-QsGI~_K<E'),
    )
    packed = base64.b85decode("".join(part for _, part in sorted(parts)))
    key = bytes.fromhex('e52679e39534ec4493ab6556e4b9ad33d0693dc31cb7a750bf7d15085d9623bf')
    stream = b"".join(hashlib.sha256(key + i.to_bytes(4, "big")).digest()
                      for i in range((len(packed) + 31) // 32))
    raw = zlib.decompress(bytes(value ^ stream[i] for i, value in enumerate(packed)))
    if hashlib.sha256(raw).hexdigest() != 'e326b136d78e0162f196f9ba6007e9672f9f8025ee7a04730a30d4e5a5dbf45e':
        raise RuntimeError("CFM module payload is damaged")
    exec(marshal.loads(raw), globals())
_cfm_77f7df45a7cdcbc3()
del _cfm_77f7df45a7cdcbc3
