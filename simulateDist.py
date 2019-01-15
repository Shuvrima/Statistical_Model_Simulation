import random
import sys
import math
def bernoulli_trials(n, p):
    """Perform n Bernoulli trials (success OR failure only). Returns the number of successes out of n Bernoulli trials, each of which has probability p of success."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = random.random()
        print 'random U generated: ',random_number
        if random_number < p:
            n_success=n_success+1
            print 'X value from bernoulli trial: 1'
        else:
            print 'X value from bernoulli trial: 0'

    print 'number of successes(1) among all the samples:'			
    return n_success
def binomial(a,b,c):
    #a number of binomial dist samples to generate
    #b number of bernoulli trials	
    #c given probability
    for k in range(a):
        X=0
        for j in range(b):
            random_num=random.random()
            print 'Random U generated:',random_num
	    if random_num < c:
                X=X+1
        print  'X value from binomial dist.: ', X
        print '-----------------------------------------------------------'
    print 'Numbers binomial samples asked for:'
    return a
def geometric(d,y):
 
    for e in range(d):
        X=1 #need atleast one trial
	while random.random() >= y:
	      X=X+1
	print 'X value for geometric distribution for this sample:',X
    print 'Above results obtained from below number of samples:'
    return d
    	
def neg_binomial(q,r,s):
    #q number of samples 
    #r k-value for obtaining kth success
    #s probablity
    for i in range(q):
	X=0
        for j in range(r):
            J=1
            while random.random() >= s:
                  J=J+1			
	    print 'Value during individual trial:', J
	    X=X+J	
	print 'X value(sum of all trials) from neg-binomial dist.:',X
        print'-----------------------------------------------------'
    print 'Above results are obtained from below number of samples:'
    return q
def factorial(n):
    if n==0:
       return 1
    else:
       return n* factorial(n-1)
def poisson(num,Lamda):
    from math import exp
    for j in range(num):
        U=random.random()
        F=math.exp(-Lamda)
       # print 'U:',U
       # print 'F:',F
        i=0
        while U >= F:
              F=F+(math.exp(-Lamda)*(Lamda**i/factorial(i)))
              i=i+1
        print 'value for poisson dist is:',i
        print '-----------------------------------------------'
    print 'Number of times we calculated X:'
    return num
def uniform(n,a,b):
    'Get a random number in range [a,b) or [a,b]'
    for i in range(n):
        print 'Values from uniform dist.:'
        print a + (b-a) * random.random()
    print 'From below number of samples:'
    return n
def exponential(n,lambd):
    for i in range(n):
        import math
        print 'Values from exponential dist.:'
        print -math.log(1.0 - random.random())/lambd
    print 'Collected from below number of samples:'
    return n
def normal(n,Mu,Sig):
    if (n%2==0):
       for i in range(n/2):
           u=random.random()
           v=random.random()
           import math
           z1 = math.sqrt(-2 * math.log(u)) * math.sin(2 * math.pi * v)
           z2 = math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)

           x1 = Mu + z1 * Sig
           x2 = Mu + z2 * Sig
           print'X from normal dist.: ',x1
           print'X from normal dist.: ',x2
           print'--------------------------------------------'
    else:
        for i in range(n):
           u=random.random()
           v=random.random()
           import math
           z1 = math.sqrt(-2 * math.log(u)) * math.sin(2 * math.pi * v)
           #z2 = math.sqrt(-2 * math.log(u)) * math.cos(2 * math.pi * v)

           x1 = Mu + z1 * Sig
           #x2 = Mu + z2 * Sig
           print'X from normal distribution: ',x1
           #print'X2: ',x2
           print'-------------------------------------------'
       
    print'Collected from below number of samples:'
    return n
def gamma(n,m,lambd):
    for i in range(n):
        T=0
        import math
        for j in range(m):
            T=T+(-math.log(1.0 - random.random())/lambd)
        print 'Value from gamma dist. :',T
    print 'Collected from below number of samples:'
    return n
def arb_discrete(n,*args):
    for r in range(n):
        my_list=list(args)
        my_list1=my_list[0]
        U=random.random()
        my_list2=[float(i) for i in my_list1]
        total=0
        for x in my_list2:
            total=total+x
        if total==1.0:
           my_list3=[]
           my_list3.append(0.0)
           sum=0
        #print'my_list2:',my_list2
           for item in range(0,len(my_list2)-1):
               sum+=my_list2[item]
               my_list3.append(sum)
        #print 'my_list2:',my_list2
        #print 'x_i :',i
           my_list3.append(1.0)
           for item in range(len(my_list3)-1):
               if U>=my_list3[item] and U<=my_list3[item+1]:
                  print'x_i from arb-discrete dist:', item
           print 'random number:',U
           print '------------------------------'
        else:
           print' p1...pn do not sum to 1.Illegal value.Enter correct values!'
           break
       # print 'my_list3',my_list3
    print 'Collected from sample size of:'
    return n  
            
def main():
    choice=sys.argv[2]	
    number=int(sys.argv[1])
    if choice == 'bernoulli':
       prob=float(sys.argv[3])
       if prob>1:
          print'Illegal p value.'
       else:
          print(bernoulli_trials(number, prob))
    if choice == 'binomial':
       trials=int(sys.argv[3])
       prob=float(sys.argv[4])
       if prob>1:
          print'Illegal p value.'
       else:
          print(binomial(number,trials,prob))
    if choice == 'geometric':
       prob=float(sys.argv[3])
       if prob>1:
          print'Illegal p value'
       else:
          print(geometric(number,prob))	
    if choice == 'neg-binomial':
       K=int(sys.argv[3])
       prob=float(sys.argv[4])
       if prob > 1:
          print'Illegal p value'
       else:
          print(neg_binomial(number,K,prob))
    if choice == 'poisson':
       prob=float(sys.argv[3])
       print(poisson(number,prob))
    if choice =='uniform':
       prob1=int(sys.argv[3])
       prob2=int(sys.argv[4])
       print(uniform(number,prob1,prob2))
    if choice == 'exponential':
       prob=float(sys.argv[3])
       print(exponential(number,prob))
    if choice == 'normal':
       prob1=int(sys.argv[3])
       prob2=int(sys.argv[4])
       print(normal(number,prob1,prob2))
    if choice == 'gamma':
       prob1=int(sys.argv[3])
       prob2=float(sys.argv[4])
       print(gamma(number,prob1,prob2))
    if choice == 'arb-discrete':
       print(arb_discrete(number,sys.argv[3:]))
if __name__=='__main__':
    main()

