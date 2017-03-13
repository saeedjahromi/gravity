import particle as pr
import initialize as ini
import force as frc


# Defining the Initial condition

lx=10
ly=10
par_num=6
max_mass=20
dt=0.01
rc=0.1
max_iter=1000

pr.par_list=ini.initialize(par_num, lx, ly, max_mass)

pr.merged_par_list(pr.par_list, rc)

# for p in pr.par_list:
#     print p
OutputFile = open('OutputFile.xyz', 'w')
for t in range(max_iter):
    print "Iteration %d" % t
    frc.update_particle_list(pr.par_list, dt)
    pr.merged_par_list(pr.par_list, rc)    
    OutputFile.write ("%d\n" % par_num)
    OutputFile.write ("MD\n")
    for i in range(par_num):
#         OutputFile.write ("Ar  %12.8f  %12.8f  %12.8f \n" % pr.par_list[i].x, pr.par_list[i].y, 0.0)
        OutputFile.write('{} {} {} {}\n'.format('Ar', pr.par_list[i].x, pr.par_list[i].y, 0.0))
#         OutputFile.write ("%12.8f\t"% pr.par_list[i].x)
#         OutputFile.write ("%12.8f\t"% pr.par_list[i].y)
#         OutputFile.write ("%12.8f\n"% 0.0)


      

