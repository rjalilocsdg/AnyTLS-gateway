# CFM Python 3.12 distribution. See README.md.
def _cfm_load_payload():
    import base64, hashlib, marshal, os, sys, zlib
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("CFM requires Python 3.12; deploy using the supplied Dockerfile")
    parts = (
        (50, 'v*(jnwBJRqLjv9~3k;0$Sk9sR{}J|Y@9U9$f5au4EE+20vAl4c$I*vSvmLJ4Kz|$Tl3rUm?(x@67uBPr(p~^Nk~Rk74Afx0$?pYlYIEObb(W`hyx'),
        (20, 'H4UKG$T>9e<SlcIfun+@MV1RvR`>s2xzM@Gy~RwKBffI;4mDR|Cofx}H_Wx85_1y%+sC#6L<+P{n9_b$$ieF?5A4NFguW_@u=Axom^H7Z9@gg%Nq'),
        (92, '1gH}-|I8JfWmTg}6JuS_awP>xlllL=oxN84CvG>?N;ad&{=h6-9=r4^&&#$;-%-VZl9q`OLSTOFXMAOF#h35l$e`Zr6Pm&{foqNe2gwU{WZx`_Z7'),
        (31, 'L;<dG;`JjQH7N{v^&P#?jQiW>!I_Wev7$HZ?kFvL=a$GSYQ3y*auww4AFwKn(DugIyKcsd%c2k$PZv+<~orL(ozo6&HkqWPugM8CrThcPn=Clbc?'),
        (32, '}O>?-k9zVB0V7Q*B8;g@(1tk={Wa{+-;^bPlzRL#RA<+@-Of9*g4i5$ma*=QpjUx(eMn>XA=j6em?rb9*OpK}qVbz@W$aFNVLL3X2vti?keCgNUc'),
        (48, 'rnpThy8O2o4`Tl3L<2VV>JxbsyqzeyWT1;2BT4eLp2d#*U~XC^^-Ls=b>Oicebo0?I!G=!l&DV`I1kxi@n4XMfjkJsLdASyq1dzOn0@n$g#_zL>b'),
        (84, 'jyAQQ915963UZsB80pT9_$fRMbgaigKs(Rq;gRQ~kZ|FjLWwpPqR<dYG!xeqAvgqO&OyKtY}_P4be5~{49HW7Vf!ziOfXfASBk0^&k+Qm9UpbXIc'),
        (79, 'P-;$l8Nm+i3SMnZq*Ub$g)Ml~&4#$SA8rlCbWhWvoRe1ZQXY2SHWnfb~WQ>y;WrPUCbJ`^VoZs|;s^_{adUB#9z>%2>H-rpZHrti}PVn|&7>PFF?'),
        (57, 'Y7Ly8*5*34kQJ}QT{DOLhFv;PN_F_%!4zjBc1Mf(U={iKqLE(l#Zlov}pkXPT-6j+Q@Yv_f-MV;X9`k)_Tk{3ZCfE_sbO$=Gqzj+=p<&43>Xz-|J'),
        (53, 'TU{L?FIvT_Ut_PKu@r8)4Dx!yoR}+zRC9LBok$dxN<jA0DuD_GaQur!rKF;R7`;1F8mYIK3v9L93aF&gC{*`pg(#DhVHT^yp0>a_EPPpuM-+@0l|'),
        (7, '&CArHsFvz*6Gc1_@WLAeGMe6SU<I|Me8)wq%=M)>cizZ$=Iz-fez{sJ5I<V$BbJP1}!fL}Sv_XCJK2VxUvQJDAvn1JNsZZJFq=Qq{vMc@>q_Jf=<'),
        (54, '~`2EL3WlW=KQ^zw^N?`qBefR#82C}f0!yTQ>NbttkqGr~gKWs|Q8X~&Va;!ewenHt}py6+G=EuBy4s1muk;UYuy%Qul~my<sksSxo#Swc$z4-#Ct'),
        (81, 'V<#X7fR_K`Y3Zh{T4=y`gP8MBlkjofYiFa9>!p_Z@|7-5^gW&Py(=Qhg|B%<?|wvcuxKaKKyTg$_8o8(bj^c9WS^Dctdz*SS!EH>Y&m+(pPpl0M^'),
        (19, 'I8Z~437xSr2xI!Ym63_aBl*@}?>jWaI*-sJ}!%qGtaS`L~kp)Jr)k(8CR1;UP?p`c_$7SNtN@?&PqFtAnWxRX^;2E!E#SxRS0!Zb@xxfZ}%ep~9d'),
        (25, '&9Ep@hg6Kjwz7`l_tIdip8CUxs`z#J+RvuIa+y;t4|ZU+CpGp3;=U4AV|fF&zViIa*hXuJ%Ui8Q-Cpg_8G`N3`Fzs>hCS+>5PbL)krMabwiQri0)'),
        (36, '!lAMgj}HJ?C&DT1HvPgF-UXTM8N;cm^-$20IzpC`#e%dC3=JfnCtWBin3((jJ+E@R5$@@0(m?$o4IKv#b-%cpF>UtM1=(A0lS>=&JU~ti(P5NM%0'),
        (8, 'sCB{N6x0aQ|E~INy~AC4srP)Y2v&{`=-J#)&APpS1y2Om*fRJ8=$a_M<x}&#oN>Y8hepIUrt+${9Wa+F$N$XJ}-9GKzOq#Q(d85P{hh8=V{4c)u!'),
        (73, 'SlH@lWq$;(i$$rbrY8$P}l>>pi2&DEH4|5VJuF*?)M$<N4kN9w}r3zSuis}CB>n!Lm^ak=*{iHbQD#d$Kmd0%t;RvIBO;QI+3^kE2uZ4o*eYvFla'),
        (49, 'H=VpdnHAxEGALW6p!sQ_|<CUnV@*D<?=#)V_@l+t|EQsx>Q2XC@$;%QrLKu!uS+Ei-Y>XmY1htY}Ht}Y^-TLHK!tN#+y^KjQw|61KU*y110Ji#Lv'),
        (93, 'bT0Ed=Whzl><VuyABD{Sm%g|fVtBh!_{pWBiY~oI$7(s_*TV;@8v@<%aFtpL6^+R2rGSk+16DlT*mH(QVvtaD;!;qSOBA|LZL#?Vs5K97CFJNA8%'),
        (80, 'oBKU15}NXIzjM80-Iel4^o#AS4|vuqxG9haE`CDnfG4zmW^K+eyQqDNS@7WAz2~VNrDzII)*7L6#=ncjM%i=gy+n2=K&ig2qnf!4rwXRlrTGr0q>'),
        (6, '1@!=yKH_vEuBe9%nlx*ZZ{jTM_l(ee(vI3n`lHXYuLy-~H@h`1|D7zc{98j+oZ$p{m(tVHZ^55coo_jr<vxF7cJDe3a~oQI+Ub8oe7%Uejk8dvYQ'),
        (55, 'bets9zjwFqYT%B6Od>gsT3xEs2z3r4Zd%9i^Vca*^Vin;mZ?%TYRdjpt0w@tkczTjF9GPj9$k^$e!Tq*uunp*YT;hpPrLD@HUsB=^JWB-g#8Wan6'),
        (59, '7q^k!E5g{GG}WHU4Lts1z)FvjG+&E)-{sJK2DXNeM<+<(Z6{^b$-+p6W6wQJLwZjR|g-qB+1?ZQcr?8s~DMa#$9WlMzs0%*<}PPkG&8O&T`r7FcL'),
        (89, 'EW_Si%&sQmA2`bUY@Zpyl9KhN%aoy~LADM~3?OHqV(aCgWD3ZOXv>$)ERtc3DxFJnKfybkM`8<k68mLrB8_bAAi3(D@#7MB2^s<LHCEIu-2jD^BK'),
        (95, '$TY{{c|}mSMv-H80Rt?~2FSZlTrTdwX2Ca5r&bhG3rGbZJDPL0trG=P!)ubnEDhd5rWyk8wTU@O_JVsqM>-NeD0DpV4U?>o>H9xD?;bE88Drf>)`'),
        (39, 'rJVkWrU_p+E=-fSYl@@2Z7B6SnakLf%$%Je2U>VQJMAORLCdK$TRRdY68y&65zp}WigFAV>N?#)}g6I=y7$_Ti4)n9%$_D)o}j8EkUoGE~38n)9H'),
        (65, '7}l-mK*duHv5Sg<pYlkFtQb5Ik$g1pjs&kxjbL(!`yPE7a>F%yF@%+DzrK{Y_o|HN<j7YndE98{CwE~!q&XsP2wIBu9n|Z%n^FlA(6+cX!+DVEi;'),
        (29, 'd>=cW!9T80nuH9TVYho^XSCa9#wQYDAa%ccQ$TpFXBt&?+KLEr(X|0^IBy|G8)V0w_QM}K`x{Oeyl-IkjBqU#W=DIfoT==XEkd`moQtauvDrZBYg'),
        (9, '!acADodtgpFBt(qdQ9<y5NSNEp)Pp2&4DPOPh1)C_%jJ&Wzq+5xQ;r5XYvr-xnhMn6YzcF6xB$i?a7wQ9>Qa4U-;I08Y0Q>lytVOV`Mmg9G>OW)b'),
        (38, 'GkZU`$R!zaW4Zm5CHwF3K+f-2?ek<gM<dy8cl@((<H6YKi>7jLwraXviy^3twy_K5cC<A@YGD$bmhco$fkyq#jo{i5Q7>@*-Q1Zm}?=DHmghqw||'),
        (47, '3K64dWez4Go6W^(m`Lc9yid0U-oz}t;d~%ERp4;BtKQ*e>jK^PXQz=bLcFVvl$X-Pi)s+~zIl9DU&Ie?cfGomM4NM~0Yz~ki5^iHznHjj4BDw~3h'),
        (87, '{K(=W>2){l^TQIS2TMsb;h#1LC>i*Ao+fgdr>wUox9G>JA4i<!kL+I*7)tAIzT!}8!x87K+75uSBTVnw@8REkwxyc$_r~)j7W#0;RTdm&PQoIA<L'),
        (69, '~gW)=jd@$jSr+Xn7<1<zBbYoW&pFCd?b(~TqR##GjoTkYn~-S}|^YS(ZCiTRpF)!f=0cpdH|1l%Ce6=uHFH0A?P&K3@Xu&J;huEfLt>ocn}2x)@%'),
        (88, 'sp9-3=cQ4B>A^F3dt!cCkHltFa``?XdjQN0}FKr!V#>T2_nfcDgdV32>aj4BsqUc1upiA66)Z*wsu0TCL%r&?W&C)h&0ynC8ru!1Xc-QO5jEjb5)'),
        (0, 'F_LZ3KBD>&cwV}ym;i=8jtdYm4$^SYzE5ANncu%Yq%L&ih}_JtBV??pf9;A`X`jFv{gmYHy@%|wXPy0QSe(h=*fWNV^BPZr`U>t-n`f}_i5ujYLC'),
        (33, 'htWMKM@zb-7y--^8ShoMI6y)2dh8qUEwW~3m$c07(o=v7wOG=qVmqO2sCdbgMlz9?sixKPmQb}rwj76EMIkP*Ra)E)TZI|l9528KyE_>@7=gOc{c'),
        (15, '2@_=Cv)sS<zD5@Qh8CM+FDZ_fh*s#ov+74dNY@SiH4FrhP$JY<8=x>}6dLkUuJ=fa$Ium4bR`a>zMBb08SANYVdMtJi1$Zon#G~aBr;LNMgVj;oj'),
        (86, '3$P-fpNJ<aygLuc|v!DJMsRkxqZBoDk`IQ*{x}IH*a{LW<ax$h8qhGFsrDU9y)*q&D!n45OiBIKW3zTl=8N-o(H|KVcT%_3TWFB-9o&SaanW6xi9'),
        (61, 'l`T=LHaYIB-2995jp9^E<wXdP>Z+Hj;BPcXdYyV6Gx^dd68QeyfmNE#gg9`M)8YX&;dx4MNio-3dIpj&oWdr&XX8U4Jt`OSc$e8&^B}>jKW}f)?4'),
        (63, '7#%J4MR!xs9Zu+;+C&I7kM=aSe=CxVM9=EW=8nC#yO4M+`5o_e4-ZFzbg(poqJtoU2Yi<TFxY@+-KEvkV!H=eeS;*STisLFM40BTC{xWykN;+;6J'),
        (23, 'VE@1S>D=uDV|qg9pMEhLpfW0qRAuBXkeGje#Y9+dU5w9QW&@wUO2+6hF;k?Adoe#ZfhRMkYXekdd3))!O1i`IxQ;SVnoel7HdIZSO;tBMM3+!kb2'),
        (56, 'XYLX&2x?{7_e^&ZJI)Cz78mmJXlw$KUeplN+TB-OBYd#evhZhtBzV{qD|7d!_QF!KK19W|E=EMM!IMrG`O@=)h$_InXtX8{Nu^z(2!*yCc=WcFY{'),
        (62, '+a;PE<@WG4;hDpw=p((5sx+9d8J9X4)?m;bE<ea@%D1x*m#hB3U^8W~yLJV+fq1Od+MZ9<^&yuI#869}Sd3j+b$zW^r0v{nMFjc0dDa1q%{DsZ8_'),
        (96, 'U%%@I2^?yga1C$jJD8FvweBm6Mc4-VL<jNO94R^!E#J1lZuSNFuDd%!vVnD%D5d<?x9+5*Rd)`XMoRY|rW)qkz@7T=}@CX85#IVOH0H3I'),
        (71, 'K}ZidgBG?-x_K->c!7WG$Q5N{5|_Hqo}#O(ANd!-JZh5xc}O={Bnt2<5j8wJ@(!wrD0>4v+{>nvyV$GgO`EMVv2>v;c%Ro(NR6Dz9;~qSR@A4Hgc'),
        (90, 'R0F-<I17NvM?Y84{bBS(S6-qU#L!4w>Ps!jc}m!sWmSL_5q@h|257}oNd~V8rCt}F1r{wmH#19DJr`H*FjCa;c5?(EP{lAC^MN8qFR}43asxKCG#'),
        (67, '0(HUW*oT2g-0<_C?NshcCRC;{1E@IzK8R`ykAmzTiKkceEvhDMYXYki_mT(LPe2l5gI76XP&-0YKqb6xCIt~r^fdN}U@KE~qF^<CjzQ0K>`R)TWE'),
        (14, 'U$#R|F(I_)&7oKcc2D%6Igk9JI`jpt>zRai`wpQ;^2Tx%q}_C2z1x-8_l#HG5MKRr-OS167X;ubwo#eMANqrU_LJv=G{%WNF+f7NfS#tK$<G-*4;'),
        (17, 'R|4i_tNhQBC4#<kaukrg}3;o7d1APC2S!w4^c&7pb7OOw{HfnyRF`%hQ+E&KnC;9y?=<XY=*a!aRh}qUcHxY0)S8<VI^Z^A44fJ0XNw?-?3ty9Yk'),
        (1, '&O*l^Y@;tZJm*wsS=ab9vNWdIMz_$C3?Iv6rp1D4O4#?-moeQXJa0spAoc*7S4E%FF}84f-}mb05Ybq00O4gU)%4Hzk2O=-Ukc?5fhh62R3aT06h'),
        (16, 'h>^vg2o0DY9SO)w_%4&7Zd$P%SxW?{il+4y0-uGy%n$Zrc~|(CZ$O2+rG77>a*w0R`;%I2LD(cL14!W@%%}gP3>Mny*_$n8j(CK7yB4p!NITNG~f'),
        (13, 'W7FeJ5a`50+8ZZ{_wTAX?UjMX;v%<T|Ql=$4|t3;#WaeY-a#W4tG_R$ri(T>=e?lDtgp(Dj65&;TT_A;EIyjgaXiqJWPDt!$sPl4&O`S5kOV_lO0'),
        (94, '@qDX-sJI99axHie-{WUm>hLd-W-yE~~=QdLTvP0AD2+7_f`a(v64ZGbx6uHcBbgc`oFrr$B>{<I35fBMVz`#K$qR4_BFe?EkH<800PtHtTKjIY`#'),
        (83, 'E$)y=Hh5&qy2pU<2Sdm#uZM(YqreFPu$ve|Iq6{Jc639YHHAhuOy~<8;OZ0VQqanPwz}2qaiHzVm5gYLOJIu{NzoEcU6!WBMv}%zp;CBYH1@8V>N'),
        (34, 'Yl5)M~8dD)&KvPF0nM^JFgI<^<v`|GQMLbCX*_>W$Y#qmyaXra|iTEA>DPoK)hsQmqUrQ~mVrfhuFP`I3S%*X?i+1}`msCqX~<v{l?x?+S8kKtTb'),
        (41, '|9)d@apaV@Py5>SnI=7k{kQsYDTtJv!n-Ts^kzLV$YUP+{t_Ee6N@P*Y|blq2ojBDFFf43SwbkB6iHr*MWO<A6~(@SmkU$m#rL13qjli|>8apNzJ'),
        (5, '3=W5J7-<DQDahUv`4uR|;(y`<L>u*x1ugguc%~<}^wg&tS3KQ~<i+_*h>R#?F9vM2tI#7}wqua96ymGVIDVYx&*|TS7Tl^~LQ=3Nx7x{91y2%|1='),
        (22, 'j$63@ZNL4A!K<jT@j)V0@YlYXTY}C{EgF;d^Patnz=`n>Dw#r^fk@n+fZtR7`wV0VOX_}-tT(c6yeIe1&dbaSQnky#%g0E$>3yOW2-ztWGC$wWbr'),
        (12, 'YtM=Mlq@;Z8o0<SW@-fF$l+p|%P}&W&95il#{@OZw!xotd<E(4>&5}_n){YOLRX9&ki{(icC9+t3FJ@;sKqdqqLju*#``z~7F}{kokL8*K5{StBX'),
        (75, 'Rvwi2B!38N&*I)!TOeSjd)E}OkqQd$rGIsx_11VtSvbS;-=0y^D*UySQ5TO`e2FPdc3%v;t75HD|1KG!PYb$0*$6$^PN9gXJV}VuNgaJsT!z53pM'),
        (28, 'fh+=(ZZ-ji&a{S)EklSuOlXhc2M41A{}+@03>Cq56dHfLngiUL>J?;!EDqBlpR^X6F3bDw!8YSyH~`FOhra3;}|p}hrsrs5g+N31BHi)E^H)~X|i'),
        (72, '?R0LWACzAxImsUG7<OQ5!9J6n~EM@L?i^dCzW1^fVk@8nTsyCNTOXiztFRq!4qT7kS?dH*2_A3IT#<J-Y4py-~wzN^95PE^GEkgHOmC&Q&P`H^`$'),
        (21, 'Q=9SJawD8FPqewa9c(tiTIGENv_;s71Sd-~Xu?Q)#(V>v!zqhU#Hgbd>azvjj+|E+UZFP>_pWoTh;_b-)w&`j!|hm*Su7%X)%`m1{3Z21lDrR@3W'),
        (43, 'W({Fd^9H5&$&5a@Lg^t5C1WYC?SdqM8MmqsK_`c`^V<`@1A<2o@Nz=LNmneJO)6nx32K96N0u~|2L*{%1F4^(YmfD5x?43FEN11izOE9SY_48N|o'),
        (51, '~jy!vudQa7oycnSgH=5ZcOJvBC5#8Zf%qy1A*ru69j0Uwnk3{oP=}AyxuC6LwsH0*YzHID^1VU2Jf{?`}L7#Z<3hV+n&V_JB;Nc*^8+Kjay82iTK'),
        (10, ';VwC1qdEvQzVQJdh+nan^AcLkE`DS=YDZ^?FqVHXwG+x{wny`?XSYw;1r=JS$hoDGD6SblQOSXT{df&e(w;=J`=<eSvg{ta%W?q04I8MsPfOqMNQ'),
        (64, '#O=Cw*?5QiFd9n7V12dpIQ5yVyTW2#LKp6;b_gjLX4+lr;pBfHR&aSqZMpua1Breyn<Kq{HjqoQ5~#-{VUv=0hUll~*gj1KtFlXSQx(M88$#UAQ?'),
        (11, 'Z}fu(ZbRbf1Qqs*hCQI_t%9K(1s5=KgfOcrck<1JYW?8~;(<+qTBX3axk}DT-`dSGP$>>O_!0$Xs2_%qtOy5;CpUg?5-2({dg$aCYFYI8X?nlMr6'),
        (85, 'O9GkWaLKyC=Ib;D9Fp3IZmGLT8pQet%6M)}K-jFBH+)S#YWiFJ$alnA&j5({_aYXm1pPutlNlsiq3^G4O7fzotG#M}z1DZ!7Y$Jx+@tcPegqjtLJ'),
        (68, 'O*J8t0d*aGTcS01M}LWAeqkff6M1ki+Hi3oP-n>(mXOK&q<lnFa|RGC1Hzb8~su-2F=!_*}UV!Ubid_#pS{9-*m|nHi?L8DYHo`xzD+4NC(TXjOH'),
        (42, 'K)^dogu`6QByR4XYnJlu!qF%;v^AEAs+ZuXj3E{YV7Yg#Ez?}5$9SqzuS0Myde=jkms!YZ2zeH6nONbvEl^c(Lt^mkma=V0CbWzir0e|9hWj^2B^'),
        (26, 'e(KT@Yk#Wi>0bM=(3c_rXoV<BD)K0gV36)8_NQgKJtj=M1p(k6wJZ2%cnq#wXxUH16Juwp%<Ihy7ZD1NMR|IgAwUcspDep%w`Y)^HRtNJV649k|V'),
        (24, 'WAzgx=xD`3DSnnc0I(;On+*Kb~~+#}kaeO>I|C_8lI8&j->VqkPpO@JtfNGZy|$cpk-(+tn}COoK!9?t(XOnM3tO-~BVmY7tVMZzWy1n=kMA0{DZ'),
        (3, 'LBv|Hhm(S^}Y5<SJnq)nTyn3>w-K3I)LuY?~h<F@pX(1%e-otYIn8mk6rhDjfCU`eU!7OysYcd;|xALt*zI20dj(4pQyXc^2)#ed*6qcwr}Fe+TW'),
        (30, '9b*;T^W<R}jb8whSY<6NtuJj#J_Y_;+Zz;#)Wwde-qKh`Y5<Q0qKAk#=(c}j$SmSHGkT;;V%x)s-0I_dtzW-(2q@}i@T^$rUy}zFt#IpGq+<s|rj'),
        (35, 'QO)EG)hr}NI)k$V6m$n7ujzvUqs2csasvC3aaxHAOSDI@Q<~*{YAo!G7+lLc^KW805vs^D`E~DDFCv)|4xa8wG(yuohHmY~c|r-xfo=@MwNvMmwu'),
        (70, 'q4d?kqg5Uw`WNGiYCn_>HqeZeZ-*Zm7c(x?Civm1pI~o^nQpeFr(S)_{J0gWH1(@!ILux%5bnCr>l)|>XR+q*w|CGKNAslZs|cjngQU6K;Ye=<L}'),
        (44, '~ja)ql#xn8{PA4W_{N+UIQr9aG5BulNw85D!eJPkc7(!d=64gN|Bv312YuJSv?Y+N{?ToSAyWgkJ6+ZFGRrs&z=#LwcE{L)9WZKc*;4Od<DmsnB^'),
        (58, 'lXM;R|83T>g_|3g)KVjbipeUOIkkk_~>^eQ%tLMh)}~g_$7o=<R6Q`lR(%ZAJx9;z5uPz)pF3k+%)ob6<6Eve1Ld5<*`jjnI)2Nvj79LGuDX_EMh'),
        (91, 'f#}SsQWN15#w53AAC%{JU*?o6RvlGd86Vkx$FSW|L<_2bQv@ZgvDKOXd9a;Elq3@fZolSu1t2w(nj7bmLcM;^qm1r}vQd&}sy%?!X4h!4jgxL9mq'),
        (74, 'Xl;@E}!LFZ%lt}^2_YPx&XD-wTQl!2gFGM(Vv2wyrqe}Vn|gES4is}eVv&8H=R0RIG`5lu`d<UFD`JAtt=&&#2QBhkz9K}=na-Il8VzZ`ulvIzHR'),
        (60, 'cdm%)t)4kU&W{cGDqFXBDwH9MXTX5M)7h^AvJl)YeYm_*1@29^9`13)jE0e1Kt1fxO5njY6>saoN!wocE4pL&{@_17BX(#z9BmnI8kuj+0{&m~aE'),
        (4, 'TRz`|Co#{V;wDJx;Pa<J;fJpqvcD-q#=K`8lA0no+kJx|6b_;OCv@U$qlDL0G~d@IJUDtOjM)qm489@QqL+f4`UPJJv%yo+fop=mK3=r1J@ivY1F'),
        (76, 'X=jJ$VrnJU5&W%t8{<e2>q*e@bN!klGLZ6<i(PMPkDM{_mkEKc#%b6;+@ep{KnV@(@#ZsV#&3<V-2dchD2qaJo1T!x4|Y-w)1)*2%rA9>Xe^@{;L'),
        (18, '#{g~{Pj~(nA$RP`@wp*77dX}{rbprxDD=k;LFZ>)-D9xCVC0N<`*v#JwB@!fxQhyIA-M`PBRgNn8OjtE&tMA5=%C{ly)w1pp)WO*qZLRIpikfD<q'),
        (66, '`w-z>)l<i?@Q9Oh^O8^M1%+cw2XDgDYxlPv!+9v`PN=F6R|BX1J=(rI#bm$W+KYeHrJ~X=9BE^lsdB&6}LB=d6WDv$W-?pZn(|cYtji<Eh2`AHLA'),
        (2, '6Naf#0*UlA8!|YmH1Dw9)J-WQ}JUavZ;cpzcz%qczOkY?#NGOW+TcF4qXaDT4Jc}@Y1!9%52XzGiFCmQ&qpV2hAJ-kj64fCoHC7VNDUkIE3>KBv7'),
        (37, 'PT%kLv$s?;3a0zcC`BQ2pMor>uZSn^%A&Y~sU(G}`vpw$Pq1VlsLh{#K5X$}>&FU|x`<yj}WD<yzpXU;$Yy$zN!K>PO2`#`Vk)1*Zu;!uE59lHkj'),
        (52, 'xi8V+6tPs6!UuxG-y_hsZsLOe_tS~7tS;hHZA%*PPXm4<4LhVZ#lX~}r;J>75zrxlYhWg9huNG_%wbNO>$;;{+G;`<q?-9j|tH25q(nhVxKa)CQj'),
        (46, 'BK27Z>uw!GAoTQp5RWNx;5>KBFH;vavBcQgN@2J38+eFD>lu#!$YR)}hei0KYaA?coqM2r^TS>i9&r3=5~w1yWL}nPD0C>@Qu0dAt|o=x6z>_24r'),
        (27, '111#5#G#yWb7QlQ@94p0}G-C9F%%&db4mrf%U%8@q1l@>m4!J~tRuO2?{2Wunwt_Pe6prUFE9X<am$_wAD#$~Gsna?WCFJ=+R(ZD_1gL7o&z<0MT'),
        (77, 'u2rfoSHoxWi*BV6LgG)3F9^6HrLTWdkZ?4n}vTnnlG3M}GQUp?dda$`mtU5diS{PR8t-m|$BkX%)hLT6>#Gny4<o3ieWirviE+D}FJB3w!3}r4c+'),
        (40, 'h{ZCDV`Wg$fe*i5Y1F!e@Sme*5kyt|2dPua0E9Nq4R!OuHj)(p9`mMP5Ys<-R^+^6C@&CgwHGXC0fW&%lHj}{f=?jvN!{OhrySwhm6N@=nwfH7US'),
        (78, 'y*Pms6S2Q(p<D;&S+*td#^oC@_~2>iyYL%i12wo?d3gKguyX*_0TrgHO{YQVx71u9P;ibjT0%K^!{baLH}pmjbMewb<dGvbySy)g!}su@g(Q9>@('),
        (82, 'aXCdqlZdnYTiOXQTRs%-s7vM#NJ62dMh755pxW+FRWjU>w7ogK~OZcXZW@$C6<!<h11W^)rt<|Oeodj^mF6&df2t3+Dni8pYPLuSJ2lYF%G8bQ4W'),
        (45, 'JT8gt^TglZi>cGdc2QJAMom!85r#DS>`sOvFZtHVXBA~eEqYL*zn74Y=}a+(fHGCF5>;-1uX*Y4M-B#aXiI6j*_8k9bor2(7E7rtI^tm$e-tWq4C'),
    )
    packed = base64.b85decode("".join(part for _, part in sorted(parts)))
    try:
        key = bytes.fromhex(os.environ["CFM_ENCRYPTION_KEY"])
        if len(key) != 32:
            raise ValueError
        compressed = AESGCM(key).decrypt(packed[:12], packed[12:], b'anytls_bridge.py')
    except (KeyError, ValueError):
        raise RuntimeError("Set CFM_ENCRYPTION_KEY to the 64-character build secret") from None
    except Exception as exc:
        raise RuntimeError("CFM payload authentication failed; check CFM_ENCRYPTION_KEY") from exc
    raw = zlib.decompress(compressed)
    if hashlib.sha256(raw).hexdigest() != '4cfa872374ee28644b176dbb6c10e0cf8ef3a62b150663c1ee84b17cbb22c239':
        raise RuntimeError("CFM module payload is damaged")
    exec(marshal.loads(raw), globals())
_cfm_load_payload()
del _cfm_load_payload
