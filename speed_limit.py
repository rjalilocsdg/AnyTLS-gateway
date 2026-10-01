# CFM Python 3.12 distribution. See README.md.
def _cfm_1975014dd03fb76a():
    import base64, hashlib, marshal, os, sys, zlib
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("CFM requires Python 3.12; deploy using the supplied Dockerfile")
    parts = (
        (5, 'u`GWHK<kldJ``1;f`x5^PKsbAuqzK@S{I8SPc42Sd;L?cDAo|-)72%qANga>?jIx<zRD)V=X#8|D3)O7eYY;E7x#EsnCZ9#>I4<Q_@*&@JT?k-6VWWH8ufAV'),
        (0, '+fPM0llheA=%VJ<(;HAXKq_C|qY?gNn6y@2eS236SP<@6a#_;yg}={OwKm3{nBKbOXf|E)yP=UDhda;kyd->|-NX9IKjw64IHDxZpl?|EouL%u1cy}5Y!{gg'),
        (12, '08<MYw6DuW7buk(gHZSCFJRAOh@i=kKpC5^FP$DE|J%X2t~)7kf1_aUQO<A$TJtYLKG*NEJFGV%k`*elbtuHXwmdC&L)Kv%;8S}}x~Zn_1deNx^g(R2ekSUC'),
        (20, '3dqet>lUOa_o9dx0$IG2E625+1FjlgkUp@iW*9Z+Y#HO4krUlemj$R0Jp'),
        (15, '4yEih$aA5Cj*G9sVv<0gUr>Rign#mnI{}V=bOeGq=<efyryE8;6lJF)O_)4oYR%NxL!V^fjYi2qg<WOdTAE3MhELN``jo6RU%}mry*(z+J4bdH;tuBHjikVS'),
        (4, '-_k0n%F2IQj^iY9V~2LPxqtr84XiXbo4PvJ0b&e(uD0Co+KZJy0O0amaKnNR+-k~ye(8&_Y9+5n;}P0+Cz{MJ{y=ci)8$+7$x$@n*Q%?giz*V7>PXq=zW&U8'),
        (17, 'Qxf8ZQ*0GC%(OHzeaP^h_bV#0|8CHVv@q25zL%jK<$W`oP5O>;wY}pRI{JvGfU#=<FSezDlDV?jPM`hs$EDrutoUemzoZ`3xR{bGW*_c4J7r0q13?)2FC_JU'),
        (8, 'e_%H>d>fY`S34~uB<3c0?GTM>K_&Acz8MpO$)ef=$oReJPl=B`@grYPcZ-IMRKc%;hIvR$cOQ%>x{ugsq6%4EI_Hs7F)+6Y3iK?_u_g{u5AY`d<u0OwLvM4m'),
        (6, 'Pja~fQ6yecF{*&K{~9N2l{owWj&~K5D-Qh--!oJaVDPw)W0Jss0^k;-u=GM@_eQU*rE*h?HJ8Ea3_ghYEqtz~DC)kjB040SJpcG;NmGYcE+cNpNi~!RQXsJ6'),
        (7, '#zFkubH^mpl!yv%T;1`iuNyfgLwzKxopD0n9O;83O=*BY?f8ihpKu)zEKp6p@@Y5k1+c~H!xUf4gV%00wY&>>%%c;d-N525QJy~{Y(eL%Df_1iES~DcxVeIM'),
        (9, 'BjvP0e6SObh;VG^)L*4sv$R2S)enjt1MH*vb=muoM057(JGjcAR#=tCfJrb!hn#`J%!3kRm}t`U`=<pCEK&zm(<+HPPK{8&M$tUV;_-nM8J5Z1dk1_#!&$ik'),
        (16, 'g>R-T101wimfuK*)4e$|-n>1RA;l8R+1oUuxgv=<YJVfYgKj)Ar=CTuANB@eT<V`NDUtEzrpAUr(&!!?qWd9&w)9$lm>+DW1Vf`faO_K`dTc~(@E=SSdtGds'),
        (1, 'BY?#bU5gBW%t<%ubcC~xtC6l8P|erR934Z;^Bd{^@{=9HRpOW7ZkTv%!1@t<<4KRHA7ZrF%<=W^%e9lXQ=^hx_nS++e4{iz`b{CxeD%pNb`DO{>RA<2DMfW;'),
        (11, ';2tXSr6!~Ot~l7^@W^vZ@BOq;eoh|5dFzsuP^3bsnb<_F&^E@|t7@KY8bukpdA?oWxT@B4MXT4u4QT~gY6e-rNX@;K#X{3`o@hj(OJi@LnTWiLzp-;?01Ps*'),
        (2, 'ox%ePzN+-M1R;o98Ne(D$`8U0L|Cd2P7)e%M++=1b;gd021Ic?Q@MaID<U>9jPyISR^9+1CfgbSJ>@Knx_@0R65sPuZI;23gntP#Tv1Kl&VOQ*IYudW4t{tE'),
        (10, 'v}t<+=IRtE!;?0MwEGRl8ha@<umgxabLM*((f1S`tRQsZSB36`-oh7_=}^~+Hri#2W!eSVaPT1tOm`twh<qK|k$J}@zC~d2VpD8oohFB_y;rt~Ps5JDtPjC_'),
        (13, 'g8NVj+f2@58Bv?!0|)8j=9FN}(7d=_GSGH;8LuJZ%;gme!Rn*(-m?TdAk;W#e5(lTmf-4|Vi_`18M7F>zmcSs-IddCb$wo#;SlCk-Htr*MmlpYxJd~nlQq1o'),
        (14, '^1H*qO5_yMLd4jOO%jEY66zo7{}FwoLZ4s7V_j*{ul#CR)){p8qw;*nG6GkwcE>OrvAAuQSc~QtC1QE%A9a$@g2g8u+ym&z&7Fu|HU+GAB4#W`)HZtiLS|=e'),
        (3, '$c$$ZZ(0~@YPpF^XqkJ^KtBvGC=AnP<TvzZnoU*9V8rUq8dU!({N!E?%HTPexafiK0*X5<rVM)miJ!i(Wy}wMgIV3eDZKExk$YCD_1SG1?*~bORWw~_7N002'),
        (19, 'A&$#fow6K`>GuBeTy9ehe#ZiZha(M_{Q`$;-QDofTBtNb-h!z3YjXNwBAF9_*w2Q^O}#x9!Z|Bcw&4?q6=`Ze4*NqFP+WrwK#<-EeC0ehdi?HBJ+QHKIL)=Z'),
        (18, 'Qyd$z_G@l`*G)IqU3C005{hwlx~7(|MruvGi)E@@L;v_I1y1WAh_yq=!rPuXIA&!bi5q~Uuka*$=;EzeF9fab$#)D=*#7Tm=#6_Zw}qwjxi<gXX>@ey?D-1{'),
    )
    packed = base64.b85decode("".join(part for _, part in sorted(parts)))
    try:
        key = bytes.fromhex(os.environ["CFM_ENCRYPTION_KEY"])
        if len(key) != 32:
            raise ValueError
        compressed = AESGCM(key).decrypt(packed[:12], packed[12:], b'speed_limit.py')
    except (KeyError, ValueError):
        raise RuntimeError("Set CFM_ENCRYPTION_KEY to the 64-character build secret") from None
    except Exception as exc:
        raise RuntimeError("CFM payload authentication failed; check CFM_ENCRYPTION_KEY") from exc
    raw = zlib.decompress(compressed)
    if hashlib.sha256(raw).hexdigest() != 'e326b136d78e0162f196f9ba6007e9672f9f8025ee7a04730a30d4e5a5dbf45e':
        raise RuntimeError("CFM module payload is damaged")
    exec(marshal.loads(raw), globals())
_cfm_1975014dd03fb76a()
del _cfm_1975014dd03fb76a
