# CFM Python 3.12 distribution. See README.md.
def _cfm_load_payload():
    import base64, hashlib, marshal, os, sys, zlib
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    if sys.version_info[:2] != (3, 12):
        raise RuntimeError("CFM requires Python 3.12; deploy using the supplied Dockerfile")
    parts = (
        (20, '%Jf>!_|Mjf`+B^3Wp@V1T4@I`G=&ocbJ>QNrVaE<(E^!915`n@!AW=DjWd3O-*3rB*g~CHZk_Qj7%3kv!)$xl9)a+dS|COFD<`a`!a*Tcf9b5ld|'),
        (16, '1XY5%dDu5^gN7xb$kmZWDM1yXWo!qJ-<1BB~1UmO!fnl`wKLTq>S^Vl=Xzvml!;;DlGSiZ!!U<P~#k+3JBTB&i`^pdSMyIqJlS6VyfDb6i;hLVWt'),
        (2, 'x4^0BWmbCAT(8-N$jbs9Rr3g@P8N^tL@hR1eOt5pF<rY^)Cy`VQOx>TO69=wH@)+pZHJZyt*j~0VNbMBE=(8_RVsh(k@Cev>acEgWaBO!3_2wQ4p'),
        (6, 'w<nUC^yf#qg=DaX%{i_kp1LTVMI@;ckX6SH)w)IR*gRHdApJ=Mb0?0zwuCO}%v^8Su0X%H_7n>bf7v4nP3*DP7p(bG1fum4bwH->#p!Wa-ZU`(tL'),
        (19, '>@reVYy2cKuKy%)vbT%>02!$WrnEz3Q*@IN(>%%koJu?W73z;KrA#U8gTso+D>EPKWe?FZW#?n-8Yus^;ANVi^I3r*?!;er=sx*t@FU&u$`yQ&3v'),
        (0, '^hdz8I@PYdcw;lUQ=^Y#3iJ}u3fGGov^EHPyYXfk8Z-L^C`UrJ((pFxd?_60Dq)3fw_b#A<!!i9tyz!`^GP=95_AN<nqe8oT0oN?JV3~j-p#VTms'),
        (13, '+3Hn2Ke!K#XC-K9E4A$euo4BBvEpzLD1$qjLQd#ywU|M8WCzw9>alCCCBcA{}4AVqfN75SjtEolhV?UpaXM!!U1Q=S<ertgaNH@Bene5c5lU;5kv'),
        (8, 'uZYuJU+}3DKa7C-Xcy^VAgmQiQSVm^ZJ9GxVxbyh*O{zj8sm^c2;@hITP|v&_ukS(gdhvGBoQ?`K5K2%)~m6;l|B|pfULeV3`*qL$ISt3)nrr$;o'),
        (11, 'e8m7~XSaJkJ7?8)SNh|Dalw(3D2~jDA8^Aj`zt&-qr@8{$25mNg<jtn_8a3~^mlKHi}#b0)|b6-dSE^Fv0Y%Y^h-@$O2Jv|UVGYmRz4C$<@<>;#n'),
        (5, 'o<-?RKF@Pj6B|(R+b3EmlD|;{3l*9X^~Fbnu6(;|=W8*;F(S{ZU&y1#QX;CfJc19gI1@TQi}_FFp}x!P=FezKmyh8)DlMcg@#z;z3##yKgY7x7&g'),
        (18, '`~P^o2TU#8)mS`YUj(%ZXN_i<mHdGON#`6@jXjj%8_P&_T{r@)Z+6pvlOtvVV3;@pd2TLWFtVU=xu5_^fk%H)X`~L0feNTe{k_kp<%<czgm$uE0J'),
        (12, 'P@%15OodT19?;|%&dT*4ZMgzxx-t>|RgL=mH-Z7<xj5Pe34M#&jcPIPj%-dopSh|lpw?z}UND6EO<D!!<hLV?dVoWo`LunaqHG4w*BzF{?<e)CCL'),
        (7, 'nA)kEN@AQmgH@51yCF8tHTYbsHdZYG(+K?~7Eu*#ksh>8>R5OfH`~AVJNv%=dwsLba{&kTnUe^Xt1k^ql4~dIQ^l5O7FN*4w<)F~MtQ~MDdj3xR_'),
        (9, 'KYo9JCU>+MW_8?I#--LctJj~(11!qJ^HrrG2StmAOMce_=n>ZWC@#1fm>mjqv;*T7y;>q|zG0c9AV;}*Tm`I9hY7myTrU%uWIl52FDH1?JHV3Cx^'),
        (15, 'a5KcohkT2`i~yAxHGal-$zR$elj6oW{Lq$~61$zG2*p7kBe(GwLOmOwX4o8J)?HQTEd2f&&8JS?BwvgKz_5&uBaexfJ-$)C?}@MdoKQOh&-7WMPb'),
        (1, '^{Wdcr=z0u0nNSc-Fq%=(z+64b!~dI}{P80TT9Le^EpM$;Px*a8^z^*;d{if`ZG8?(ZgU6?)aR(g+!z0gGY%L0cF4K|etOD>QDS+c74ikC$)FJY7'),
        (10, ')T>NQ#sNgFSnC-H7>Y*^8-RpA-t9(;wdFOa_B}XWe|D6OYX?6A6#Ao=PP~%JB-a2e8Z+4U$x4}-0suN^qLz6*E`yP$$6z{;SwyDAz4x7om6YCGn|'),
        (17, 'Qj-|)KJY?Ln-2Bnfahg1|JUX2Sa;BE7a_69auw;NeezlcTyMw?;NZ?IQYu^EOi=rTU+L{i*UTVB$Kn-1-TuY#K$r6tLUp-9U?qq)6t|^bsJvJL9q'),
        (21, '13bAk(KNV|I)A0s%Ss&eRs5{Vs)=Xp$&y(bT3^^-LV;3;JM^&3Gqfv-6@)3g29a+XoVozRcO(D3+Pz8gL5u4_p<r_6?Z9Ko=^|vEMe*rv'),
        (4, 'xSNVWz;pU>V7_AAPZgI5ZQ!bdqolDEvO{zojIv&qM1yw*`j?>+zzYcXFb5<Q?;1y~7bJIL*fcEf=@0sa(UXlfhOhVYz*9@|e63s73C->jp5T{S1d'),
        (14, '+f>e0h|(i(ja&&so(-L~c772|v}-ys)4CsM=b6f3@I_>wi241HKC@DW85<0)CCudS69a1+9)Bq~XzBEsTxqU|3L`h|4Xu>@$pvP=F1_$lP=HzqRF'),
        (3, '-u#K+D^om<Q=ZXWY*sQ4W!HlB%!TM33|32O%6#K_PxJeM!gnbwEN#qk`#cP&o&A)R*_KD9sKknd(`0rTwAz3@g25<vIOcvH#t_kt#IVLoq86BJ5&'),
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
_cfm_load_payload()
del _cfm_load_payload
