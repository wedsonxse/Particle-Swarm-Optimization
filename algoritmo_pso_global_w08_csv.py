#---------IMPORT DAS DEPENDENCIAS----------

from __future__ import division
import random
import math
import pandas as pd

global num_dimensions
num_dimensions = 30
results = pd.DataFrame()
resultsValue = pd.DataFrame()

#---------FUNCOES A OTIMIZAR---------------

def sphere(x):
    total = 0
    for i in x :
        total += i**2
    return total

def rastrigin(x):
    total = 0
    for i in x:
        numero = 2*3.1415*i
        p = (numero/180)*math.pi
        total+= (i**2) - (10 * math.cos(p)) + 10
    
    return total

def rosenbrock (x):
    total = 0
    for i in range(0,(len(x)-1)):
        total += 100*(x[i+1] - x[i]**2)**2 + (x[i] - 1)**2
    
    return total

#----------MAIN---------------------------
#---------Classe particula instanciada para todo o enxame -----------
class Particle:
    def __init__(self, x0):
        self.position_i = []
        self.velocity_i = []
        self.pos_best_i = []
        self.err_best_i = -1
        self.err_i = -1
        for i in range (0, num_dimensions):
            self.velocity_i.append(random.uniform(-30,30)) #rosenbrock
            #self.position_i.append(random.uniform(-100,100)) #esfera
            #self.position_i.append(random.uniform(-5.12,5.12)) # rastrigin
            
            self.position_i.append(random.uniform(-30,30)) #rosenbrock
            #self.position_i.append(random.uniform(-30,30)) #esfera
            #self.position_i.append(random.uniform(-5.12,5.12))#rastrigin

    # avaliar a melhor solucao atual
    def evaluate(self,costFunc):
        self.err_i=costFunc(self.position_i)

        #checagem pra testar se a posicao encontrada agora é a melhor individual
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i
            self.err_best_i = self.err_i

    # atualização da velocidade da particula
    def update_velocity(self, pos_best_g):
        w = 0.8
        c1 = 2.05
        c2 = 2.05
        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()
            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    #atualizar a posição da particula e correcao da posicao dela pra dentro dos bounds 
    def update_position(self, bounds):
        for i in range(0,num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]
            
            #caso saia do limite superior do bound...
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]
                
            #caso saia do limite inferior do bound...
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = bounds[i][0]

class PSO():
    global cost_vector_rosenbrock
    cost_vector_rosenbrock = [None] * 10000
    
    global cost_vector_sphere
    cost_vector_sphere = [None] * 10000
    
    global cost_vector_rastrigin
    cost_vector_rastrigin = [None] * 10000
    
    def __init__ (self,costName, costFunc, x0, bounds, num_particles, maxiter):

        err_best_g = -1
        pos_best_g = []
        swarm = []
        
        for i in range (0, num_particles):
            swarm.append(Particle(x0))
            
        i=0 # iniciar loop de otimização
        while i < maxiter:
            # ciclar atraves das particulas do enxame e avaliar o valor de fitness
            for j in range (0, num_particles):
                swarm[j].evaluate(costFunc)
             
                #determinar se a particula atual é a melhor globalmente
              
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position_i)
                    err_best_g = float(swarm[j].err_i)
                        
            #ciclar atraves do enxame e atualizar as velocidades e posições
            for j in range(0, num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
            
            
            if costName == "sphere" :
                cost_vector_sphere[i] = (err_best_g)
            elif costName == "rastrigin" :
                cost_vector_rastrigin[i] = (err_best_g)
            elif costName == "rosenbrock" :
                cost_vector_rosenbrock[i] = (err_best_g)
                
            i += 1
             
        if costName == "sphere" :
            print ("melhor fitness da esfera:: " + str(err_best_g))
        if costName == "rastrigin" :
            print ("melhor fitness da rastrigin:: " + str(err_best_g))
        if costName == "rosenbrock" :
            print ("melhor fitness da rosenbrock:: " + str(err_best_g))

if __name__ == "__PSO__":
    main()

n_sim = 30

initial = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
#valores dos bounds para cada função
bounds_sphere = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100)]
bounds_rosenbrock = [(-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30), (-30,30)]
bounds_rastrigin = [(-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12) ]
i = 0
for j in range (0, n_sim):

    #PSO("sphere",sphere,initial,bounds_sphere,num_particles = 30, maxiter = 10000)
    #PSO("rastrigin",rastrigin,initial,bounds_rastrigin,num_particles = 30, maxiter = 10000)
    PSO("rosenbrock",rosenbrock,initial,bounds_rosenbrock,num_particles = 30, maxiter = 10000)
    

    
    results[f'sim_{j}'] = cost_vector_rosenbrock #vector de gbest especifico
            
results.to_csv(f'pso_rosenbrock111_global_{n_sim}_fixed_w.csv', index=False)    
    