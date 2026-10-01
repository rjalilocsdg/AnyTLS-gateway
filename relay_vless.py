# CFM Python 3.12 distribution. See README.md.
def _cfm_load_payload():
    import base64, hashlib, marshal, os, sys, zlib
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("CFM requires Python 3.12; deploy using the supplied Dockerfile")
    parts = (
        (10, '>(@JTtiY8lrjMa5OaC$V20{X-2E#oeEY!%KRDQB{Uegst5(vg<xseF<1Uz)=McFX=m_?BTad)Dgxv<iovoPxiLKLRjaLuTF-+1i4Lg0zjF=feh@H'),
        (7, 'cg^XAmG4e~BY`AWOXTZA{^sXMNMWe`LNVk1ZM4}%udG%hzGna-`HbZk^elYQ6+2=nkpHYi|mDlty%7X~QstR7hQi9Sw?g4T}QZ^wDJx%He`4rKiD'),
        (79, 'O'),
        (78, ')9kX6>VjGYFbsi-^A)Z<8Zt2b80B{8Dgl<J&In4$}eQ?S`W-2nhvY^E1X~FV5S4r3~=xl=x9LNmYX@nyRlKQvVoa4vG#k_KG5noQPZ0J(9hQZL*B'),
        (69, '5x@l}39@6jY9b53uJM2h~)Vayf4>IchbW@B%ZGy7MSeBkN*_6l1Cb!!@M&PaGq*}xXNl)Q+NZlCKOLFQuaL4DJ&Z14sm(gU2EOZ~KN+bn(d{dHJH'),
        (39, '}Up*|=GR%r9)uz!<X@;OkvkjsbiofW3ZNRo`M^8R$I*%O}3p<O)YwBdr}_z#PcHDtFSj1nF0UBEhPT}5vR@EuN!(%7#tp=+7*vt@rdy+WzHr8k7A'),
        (60, ';6%zersRv6iVZ@wi4~>!U5F){7)9Q<$fQHjfQdYhf)iPlYnje-@cJS`J;HD#PW%Ni(KqyV^D_SVcQFEJmbOsk`G?9mvc>qts*TE(L&e^i&F8jOR='),
        (19, '^-^8nn;F04gq%C|2`XD?}q-9*@jG__!7hWS1@9`D8!P!g=U$=)dvrM{(F!EHr*KxL<5_$Up0b}~BKm|l|T9eOj_u`T5H64e_4bI}pQGq*tN$^Z^-'),
        (14, 'A|+;&<;{t0NcSv(#U0cYopkjSv`_`~fr&wwqOz&71OyT9&SDXY=+B~Vp_bRRTTE9_-tm|}=(vsK2V0+VVf*BV^qur-?8zB~dibl~h5lK(sQ+d=#f'),
        (67, 'x^tw1?zMn3fkMC&@Vd4stmuF%F8sRaTnlo<>1A-}INMVe4v;HF@nBNgSb6LqRzxH{`6mt(FM7?**s~^r+o@v%>z0tDzjF+YY$dx;yL+5uO;Mi-K3'),
        (57, '9yiNn*#HuHUJj`Q|7Z?Q7khw{s`QaH7RzE9vnO+@A@L2-}*1~PtX8Qnb+|+_x`x3DRz1-&vH;j)=aYEQ8QbYO&#Xu$DslfauHRpg5Mf;}<ShxFou'),
        (18, '+jhvt=41jC^ktcZ~&;vyNMb4l{qN}m$su>cZD|+Uk-+;@R7S_m+uCM?r6^k%e_zH%z^by2)nELBs2TY*SAq{ZZN@8EyQwFyqdUb4?9NKlU@#qONI'),
        (32, '?8UqX_!n!mW#&+E6ZR@~(>eKju%k-5C@^BGgO^`veKL%-?24(a&P6J-T!$>wT<)k8w*4&r6#(-S03*}1VU$uTfK-orOMOg&HzD|bYYQpP(0va0y9'),
        (3, 'Iy`&>Y<AxCC{m!-nKsxq#$GJSOou)@|wkSa`HT&|NNjE1ycm*QpIKTs^8OIfTSTK*6nlrz4Ew%!Hio#1F36?DINeoGQ9{vOe3yx7V*yNrV4g7A5^'),
        (31, '%wq3&MmZ&l%OBIj~TJIVe;|33%v;#0C!aD73Y~11Ay$%4m$X`2_>m&4lE1p?ojz@EZl|7)dxg6=|AiZrw^#A3-cbO)^2edWVhU74k+RXeJ|>911~'),
        (76, 'G^X6sfMa18RQ4i(1X*ZO>ya0LY~_McS4tJu!Q9RLPh71K83#{+2eKrA=xjj8*j}6ZX;KtI1xj(t0&4rtpS$RL1@|)?V<AEqF}Q%wuA57>5=V_&`i'),
        (66, 'feDujx(P%~FBHc!_aHG8cUQD}$9FIcadUasn+ve<BfjyJ#ER*RZGXMwsL&lZUCCC1Y<Z>WftU@XjsXJn0kaVhfFmqdPrl))9;{bWlPGMTeZV=^&g'),
        (73, 'yp(w$q6tj&tA~*Xa>xi0>Nt-7wULpXlNZ`*2BEmfPqkeE(m2huli`%d-68G&geJVTeio1YA5rSRZ*Co`tm1q2Se_wSR=Q&uG=V|@=S)lk(|n|)Mc'),
        (56, '8?I{4<jYK^Y4*GC&$v5q~s(9resmhcGi<K(3NzG0j|B7rCUxibR!IJoKPrY>_G~PlM~6S8`y>J6qjQDqN~G9U}Own}d~NeLk?rf2=P}X7vluHT4}'),
        (44, '1=cCt%gVRIg~o`BH<pi-t!RPKY}?a9jV0($dnz`}29;Cto|%Nm%5r_~q#7LQGG(%{WK@x+j7Rqz29e2?xi7|3>$`{ibFKjKkniY%lacErcHU)H?*'),
        (53, 'Pb9Yco48Hd6y?u06{`yU4u>UOWN!VI;m5a4c^gg$1Kz|5JsGS_R-aSGQ*?9>gN`<<vU!a--=%l1lw}bXddN`xVU32fsWP~SQkA<C?}x0ZRS(`A{2'),
        (52, 'C{g*eepG<v8zay>~0j?41LM%l4k)8CNqa&gq*u<Q<dqw3W#IhrC1<NYS$XjMa^gRl-fsG-_5q+4<!z;SL%vQEal1&chwu&W|bI}`_yQZ5$Q6r{XH'),
        (27, 'VX=lHPD(Jxfj;wVhjT^`{&dp;y59a@6_Db0RFFJsv5yY+3CcDhX*F}y@C~(3ePWl3Azz)BZ-sfhwkD%#^1>Qr~3Kzp}Nq>gZa8uuQ=M*jb$b(<R<'),
        (34, 'qWRWpdZ@%Xla(;L^SDoM5;Ntq)gpTBY9zSOpky~}vre(a|5D@YMu_H)%u>C^)Drm82udDBpi2#=`IXWaPlyh)*<1JId^qfRI9BnK$f&@hEpJZ6yB'),
        (42, 'S`eE%TX+`-8a~j6C+x)HmykIGe0l`xTtm`3A*w273j}a*!9d2qsXRk1%PEcdo#2`3<Zhe6`*ZnTdf5TPsrUy@~uN^@e+e5f0f}dlezKQj5%KS6W<'),
        (58, '}@h;k#N9Ikaj0EY?wAEyl*XCgR~;V)2$)V2twmnUD5Z913p{YIX&b?Qs~M+rj*SSU#-QV@mh5dGjP3fH(l#G14PWT@^*Q8m2UZ0oVZ?f^}j^d)T<'),
        (21, '2ZKEN3Dek#o3>tpi_Xp^*G@+&7IK#aMZ6&z21wr;8;F7_&^wQyjUfmEzUE>iJD04qG1PJiD7l5I$l+_3-HwYr!vskoCxWefIK)iWoNnfv8?1u_}~'),
        (62, '}m(%#9sZzAs&=|()CYd5HsS1j0)T{ob#q)R594kjq?<4qnE20ETu_BwcUJ<~yJiWS$CMdIJQA`uNF$f*Q_(cFlPhqRU#<W-?v=lM^C`2jHAX;B7$'),
        (2, '#8%FMB)p{b+a?!61kyqeba8~Pbv5PHiMrJuCqrCBT?Je5WUqlbVk$a2Xl2R?<bFPHL<YDRh<5|!^oQI}p<82?<VX9zSfAH=`%8bB|gFf}up=?8yU'),
        (16, 'g-9sn%BdG@TI`k6CI*FBL=rjX|%z4BOON3eLcVJnAm7zF}ZqSgIJ}^an08%@lf$<`|f1!H*2&<aiGuvie3!I7^;*vW)yoG$_S_dB+_erXJFbxOd>'),
        (38, 'ZaJCD0p5A>PbRIq7zZ77jQ_2V1G<6Y^rxt!c3;-h94DYn#r6Maj^Vb0VZ1!>@<uQRG@L%HZ<$1j%~BAXP{6UhTJM$p3mBIdA^t)hJF|ZO>1;wk)0'),
        (68, '@%IuKT*vH<(8#ceBbF3Vexarb!bcj^+ckaz;W?*e8cV6gm%@m^jt&PSP@@XMdx9hjg`sKxe9~4upP8;Q$9rEGA;g2Hhd?Ju@-jU?AM-)HFL?Nmt-'),
        (41, 'anZK^qNjT2fkrk$H8Bff#f|mNe<BkTh9b!oH^Z<C=I6YsEN_fHM|1|4+PPG+sdB#DC5?W7v}Q0~%wE>olE1#ZpZ`eTY<e0aDJk1;F)sh0)3?8O7i'),
        (43, 'Sq_eDsB*Nuke*`7JG?7g20+U4htm_(QEesf)<;qx8@CnY<E*HQ^zAc5A(`~q%`@uWp8}fzO^KR)gC+R;oU>7@ap0$VNe|rinQ97$-rM#$t`PiFoV'),
        (45, 'YWp(`ax^Ysal&3bJUg&8(ZO{G7d99n<_`|U6DQGIoNDAm#AyPAer5PGue@;UpfO$xIRoKkfezysvrYJapr|r5*sa^nK3bXZ!Ri(|B2hF8Hn$Qc$7'),
        (0, 'I8{wmw=WSj@|*1ARtz-0lDbeVWrTj3QL`6ee}szRar1cxl^@%>@`B`s%_z$|_eLoJ!eAcfVnde|^u5zRBS+3WBaydKM5UFOtOulE7@EJqYjiP2&U'),
        (22, '6lw)NNC}BtW)1-16-VP>XtZ(=QBej7YXK<a|QOOUR$3OMm@$QkvwtDp5qqwtK5ZTpQZ!a@K^ipgvcY&rd;lA@KxA=`e*$5=Ifs`0zC%fY+F~J-K!'),
        (24, 'a<yX<eHW4d9qZw+yY<XApqGP7|ri@<q9v^T1ob<wPwbRQhEYWLl>M=BtJJ|%6$GQ>b0A>wl24_d+M?gBL#g$iR8JAM~a`z(06GS;3Vg_Q4y8`F$9'),
        (9, '3C?HL{Ul0iIuE2?cI5;_ybmh>!)Gd4DnG~Xqrss0Rcb~$qYg~>*XW5L=PPKWl(WX;Ue4e1uI*@?p3M?DvQo>#YPAUa@cQKhBNL9SNv*L=2|kc;~~'),
        (30, '7b*5Ht2J`>mhNpanmLwu2%0kzb=PSnDXN)l{n0NB$%2!0FFzQ5=#GXy+g=;6|8>YLs!FA?j}9s|yHESiB(-zcvj5>lOjcl-G2YmOkD5C_uK-t^+u'),
        (20, 'm&r3^|2mrICxm&WNXluF(|-_Xz<|dJ1}4t28#hDPOe-1doow~7BP!Gr)mG2~*Kwy1?+STmn(8O812%ESFEwqJo^c0#^@1ZiA`~nIgMmfQ(mNxIBb'),
        (1, 'w##k*56<Df=W+9V^Ggg}l-!CfFG+{3H|+-%rep5Eqhl0Di6@b)C-vmqeo+d_Q3JLDEtA)qiBQ)cU}x>IeF0c&=GCOmFxSZ)Hvp(NJ?L!Fof3{_aI'),
        (64, 'STCWq)xc*zE%h#V8n4}1(154d&}aQx|g2_k%oc${rOD7nUCq_J69q@G)HR@BYJFqV1G!((>cO__y!gPG1VfTCAGjSTR1aIb%BRQ=on4W(Zt%V8FC'),
        (61, 'tls>igP5UUf3nQEYq7^_&5m2v}$oiz~7XY)aU;hc<d-iM$9ZfcFDAE%*)#dX$Tv$(Wmjm0c*8L^a7HMbum&2v&YNO8=8TvfFNAE{dfe&x_j6Kw_`'),
        (51, 'pjGp$Se6^l_pvpb9Y$O{|^#fZH35vbXhyb6o?Vph%=Vv&y2H!=58BBSWj%QuZ3-1L@i%#~ybJYV>@e+bg&Q6EpRIn~UuyJ1p!mX0`imcXXBR1{!F'),
        (71, 'W3<?@dW?xZXJo0S3M-_;RhpX^ZrVX=7f52%74C@m+X66C+?6NI>@@D#5}r2_2c~SAZdX99C&*O2~3o_fu=|SyWG^wr4?GP%k!z9S*R7Z=R>K8|^D'),
        (47, '1WSA6WMoA!GZDsPlx9aDWOzZ3+b}LGM7!%g`fcSg$Qo9T$GRTUX58wrps(5HTK@zvIBkk<}U7aHNXLr;L#+3Hlu#cX_>?`sj?UN{EPCgBSiIm*(4'),
        (5, 'qT2AtFnhAFHxT}m&Tlpt`DYN#U!smn%RB>h(TeHc*(Cc-tjIycE^d%~Ykfv6n2}(ez5l-#%J;M8308#gVHWhOrc%vvpo9M2nK~olmsdrypD4RdJ^'),
        (23, '}p}h5bVILm1|bJz32*)#h#bR;N4=iS2r*98r^DtIHdXzFUYp@vDP4vM~FUnOt0yh6yJ6wxXHyczii>+4&s8peM|6hhuVIvD)f77b}HQ{xuca(oQx'),
        (12, 'Nh$11#_b&3B*K>7SulVoYryzpa^5g_#twG9y{?3+_i{^pWQVS~aA*!wpA=1%F%?e8l#*nlP!q<51cNWG64xHhgSYw_s^?6vVSO=*ct0B4wG(Tl2g'),
        (35, '#MRjF@=lh&aza(Wu|i>Kdw^UWu(BSS@{;C{S>e}d1VlG+<^9HcAYmoDxku5*x5BI8kzG8hI}#)CU+(T#q)XtRy`Y{V*+7>{a^T!#cyD=viHM>b6E'),
        (33, '~CI8s5NjzfcX|>l?+qxb-h}3u%<9`C%ulfvZG@T8#5?ub4|GodysENTf(WYwN)X>4Bv)sbx>|G&#HnszjTJe%p0vht<+H(c{q;EkE8Xy9$9-_-bb'),
        (54, 'FNj$vy`<OD_7VMH3SEO-XBbTTo9or`!ZqdNeiOE2702ElJd2H)HH;m%#{^utTTXU7x6*(BQ}2%*EYCsD&Vg~j{t7T?2AjT7m@a};!GSfP3|7$|1}'),
        (25, 'xO4~JW5g+|8!A(67-5;KUH8RY14$t_-PGfkcGU&b9#Y{`f;43c#q7<)O)IIU<Wb9&b)kB9T@c0S#=|Rh4f@W!F$-Nw)PO926lwu$TR+yb7>#p4-~'),
        (28, '{0ZL@{&`dOxXwY0FBUGZH@rt6>2$NbF$2DSw4`zjQ4HZy=CRDX@1doxq;P@stAfFhF<jOwjqR5CZ}A=+49sQ`b~!u<rV7b?h4Q5h+{o{v|g3Xt!o'),
        (36, 'qHIWPQb;@+buF-tQAY0VbR}8GcAKV(p91n}&I)eGuP{cll=Ua8W@;l6N3lRjU2g<%WjE?l|FUNvY@}-J9ho$#uWnjL`r-@-T;OyrTkOPmfy}eAZ%'),
        (63, 'r5P-L1pk4@erh`*CXH(_?_?ue{I=D_#87(Wlf+n5R)#-{*8%{qD8IIK`T}FGR)w4jOo#cSmG*FIkJ_OaObfEXx0%EA1zvP=-UKC-TOhselAB|$th'),
        (6, 'kZpR^D|iT0wULN!lC-$LVR~n89tI^;LjP%aP(9)Zr2ZiIBQw>WCH-*?)vwFz0YHWna^kmqVYS4eD?i<xgqdOH$O1>5G@^`V%PV*L??LY3IZH-30u'),
        (50, 'A_lm^w9uYb3u=KVu)c+EO?GLg6oBSv<y<h-?%H#Vi5(e*2v&^YJ5Z40cS&<pu%@x#<PEpN1L*myE>-m?<w@Ej?+!4O{ogz{TmZ%gx2tGfDWx583x'),
        (37, '!u_=`MM*DIpDNv(r_L%z1brAr*o@jk~M#2Utj4`m-F+v2*jsGefQ%pws<l-?X!O+jMKWQxy0j0hH2wl#+7koYOMLb@M6NLS8-!qXj#Klcw@C#qr!'),
        (49, 'J~2rIx5`5+2bZ0-Q-AB#L@ckrUJsCZiuS3mAFYa|7w)0R0EkZh3TQ4`P3Wy=*wzjvd;GU;lHw0{xn9R=`;SpAjN1RyEtU@SbrlFW7D6}q^`VcW~E'),
        (48, 'uC~z$D0#2pOI{|@1FFu&*RWy4bRvYc!QT_Yu{0l*~1!f0nJi?Jp}&gF5c5!M`Bsm1HK}UA974Q=tWgfSoLHKFtC+A$5fE?s~DX!N)WD+Wu+Z|iX5'),
        (77, '_Fc5_I7A1e+AMNXX+_S^!dAUt7(5r2<AJ*e^BvMw^Oh{Q7fUcjQs!}lVk`tMH@_P4ldNh#9c{7N#py7+EPk=LE{R0<^_{_B>fc$(QXWftE`Q~}tC'),
        (65, 'XYudqxziHGApIN&HMG8wM#+sWy1_+>5YF-jXwGehQ!l?S8EjrbzX3R~yKc9$y2bbein6Qw|8{nXdW#RlF|&Y6?d?R%O+PNlGbHm3kT*WUJ=MU8<&'),
        (29, 'Y=D^XAqsE%#Ps+P8ZhF6U}fKzB?ND;&QeUmuizGE4xJv8`%pXfBN7rR+<S{B7VR9#lY3S3a=IX<c6O_QImegYX>HHwE>`D?d)#k)>Oa_a^3p$Yfv'),
        (40, 'v0msg(EZ3r*-?)!rJ3Y;EltO`NtH^YlHc_)Cuh>|#5NkY{2~PoeFsYbq|F1D5ahfhJZMo7cppHE_Qzlu{nPnPSLjxbom_uNiqkd-GADtPhl=w~PV'),
        (15, 'w#=KjGUlU7JA4qng2zm2No+G32BDV>Lf+j(m+Z8z&)o0EMfPObf-1pY?M6!mDV3VWa_`hlE%A!JCqK_x5;Z;#be7x#FVix8D1C2RWU^1z%D!4`4P'),
        (13, '^>fyn=Y*`PQWThWC#yDS6-rhWS9%R${)$n_R$f$zS6`BVdy|I2Enh;76cAcOU*x$4Qn*wM9VgZl$BmFnp`kCF5kuj@HD+nVa#v{HpArpyfb>Xp&g'),
        (46, 'prKfYHu!k!%y&TMfQrXtCFK$HkB?{wz<M=wi`=fxz#e9z`LaH7Je+tTW@(ybZp-@vvtifG=#EzK1UEGJ@lF4s>NxpY5o_WMFH#f=J-@!8@eCMmq3'),
        (74, '1y)WZS6swPL1+#t8$;~t981+7YpprJ5(@_5nDLy<&S)gLqQY{qAEy$Ndmmt;L7z>4=cT}^)|U%OgaWM7YVnuB}nZOuE;_ljVnyZ@d@HIw2lmu%^*'),
        (4, 'AD*cx{iZ9(ol+1t~C4br%OKPEiWxz*tz8HBh%*sW?MQE?(oV*Qg2&Szr3;iE3%(k|t4K;4@-(^MDvOP=!DCw}d5gQ(}pjh#&1JJyNIyZ&AxxgIkY'),
        (11, '<3AMOf&$3xG`qSKBQEKKHB$!&rgLNN#6XD&wFK@7AEbc`u@}V}d8|s3oSLE2$MVFZB(e+MQB{N+1MWV}PvURoyjh`OALj0_H(sklIlTB?R>*$+;p'),
        (59, 'uol#}~H5+Lm{HsN`uQBjtRt=ijcfEj{I*m0naq~VD!mRI>|Xue@!sw25=IBu4?&ocD7-O-gGx$O$?BQXH7<A1!V&SZB>kEFSKIpn5~D*>!0IykaD'),
        (75, 'Yeu;p$>t^w4KwEsk-rttrdKcPS1bdOuD=0o05RZ0;T7xFlrrkcf_2@e%HAk;JAlS%p>XItru;Q>GL)Z|S>>`=`d2UVuDtsr{ea?~Uj@Q-c!|m~uj'),
        (26, 'LN3g3YBVu19(A$Xo3#qudofD&s7IF#?HF)2Vi(FS*-Z17{-motczDqTXr_Cp8Ia7PZ+U=T@8%vhJ24TEi~+6B(iZcv90Y{Eg(EO}WvCxViCY$#=4'),
        (70, 'c~bp#8#FX*^j<$K`4OgoD2qNWVi;l5?9U4grkKK&Jb9Iuv%#3fU%ZaI6~nxRfL1m*jvXUJIz#bi)xo_PB>$9(rn$4WTuGLaGH|B}rWWMG3sg$T%W'),
        (8, 'r}G@FFCbCPDlr6P(cCpCqe-A_lZtN-UCArv4`ZmY058t>zo`U&VAJde+$Cl7TPm*Cb+KD)VXn@EP3CJrWmG-E%G({qDW{588HPCZ$yNqHok_&u&_'),
        (55, 'Wq>oF=s;1hlQ`O8CaS%srDaFib@|M?5g+7FsWk~_k+hM7ZWBm5En3|4)Q+odFXFy`tpE>?jKmmTAuuoydV;P{PyVwJjc^HPvC_pkQLqD%raVs|ze'),
        (17, '5ap2%0ukBvxJcJfe6HmkaRdT;wO!!%oW~68pwG`^Rky7S!XpBuemzUuCrWpyxw&dx2-`6dZljJpI_hnst5oN`L!JQ~f3mDtuk|0M45D+ciA?OYHC'),
        (72, 'p^_KvAvw6~}tw=%semDxnM@Qlvt%ygG8{;v3)$OnDEqr<t2A|=gd0%<KPzaH9>v}J6Q%4SWE&X4<B-=9K8X6O1Pgn#aSU`FxgL3hnkG@G~$O2eCE'),
    )
    packed = base64.b85decode("".join(part for _, part in sorted(parts)))
    try:
        key = bytes.fromhex(os.environ["CFM_ENCRYPTION_KEY"])
        if len(key) != 32:
            raise ValueError
        compressed = AESGCM(key).decrypt(packed[:12], packed[12:], b'relay_vless.py')
    except (KeyError, ValueError):
        raise RuntimeError("Set CFM_ENCRYPTION_KEY to the 64-character build secret") from None
    except Exception as exc:
        raise RuntimeError("CFM payload authentication failed; check CFM_ENCRYPTION_KEY") from exc
    raw = zlib.decompress(compressed)
    if hashlib.sha256(raw).hexdigest() != 'a6e45df862f3c9b6dc7537536dfa94b75bf3a9eefe5c9e330857ea4c77e657fc':
        raise RuntimeError("CFM module payload is damaged")
    exec(marshal.loads(raw), globals())
_cfm_load_payload()
del _cfm_load_payload
