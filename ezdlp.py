import sympy
import binascii

m = 19
c = 199533304296625406955683944856330940256037859126142372412254741689676902594083385071807594584589647225039650850524873289407540031812171301348304158895770989218721006018956756841251888659321582420167478909768740235321161096806581684857660007735707550914742749524818990843357217489433410647994417860374972468061110200554531819987204852047401539211300639165417994955609002932104372266583569468915607415521035920169948704261625320990186754910551780290421057403512785617970138903967874651050299914974180360347163879160470918945383706463326470519550909277678697788304151342226439850677611170439191913555562326538607106089620201074331099713506536192957054173076913374098400489398228161089007898192779738439912595619813699711049380213926849110877231503068464392648816891183318112570732792516076618174144968844351282497993164926346337121313644001762196098432060141494704659769545012678386821212213326455045335220435963683095439867976162
n = 335215034881592512312398694238485179340610060759881511231472142277527176340784432381542726029524727833039074808456839870641607412102746854257629226877248337002993023452385472058106944014653401647033456174126976474875859099023703472904735779212010820524934972736276889281087909166017427905825553503050645575935980580803899122224368875197728677516907272452047278523846912786938173456942568602502013001099009776563388736434564541041529106817380347284002060811645842312648498340150736573246893588079033524476111268686138924892091575797329915240849862827621736832883215569687974368499436632617425922744658912248644475097139485785819369867604176912652851123185884810544172785948158330991257118563772736929105360124222843930130347670027236797458715653361366862282591170630650344062377644570729478796795124594909835004189813214758026703689710017334501371279295621820181402191463184275851324378938021156631501330660825566054528793444353


fl=sympy.discrete_log(n,c,m)
print(binascii.unhexlify(hex(fl)[2:]))#十六进制输出
#十六进制转ascii码
ag = fl
al = []
for i in range(0, len(ag), 2):
    b = ag[i:i + 2]
    al.append(chr(int(b, 16)))
flag = ''.join(al)
print (flag)

