import doctest
import math

class Conjunto():
    #
    def decimal_base_dos(self,numero):
        resultado=[]
        
        fin=False
        while not fin:
            resto=numero % 2
            cociente=int(numero/ 2)
            
            resultado.insert(0,resto)
            if cociente>1:                
                numero=cociente
            elif cociente==0:    
                fin=True
            else :                                
                resultado.insert(0,cociente)
                fin=True
                                        
        return resultado    
    
    def subconjunto_asociado(self,i,conjunto_base):
        resultado=[]
        
        base_dos=self.decimal_base_dos(i)
        for i in range(len(base_dos)-1,-1,-1):            
            if base_dos[i]==1:                
                resultado.append(conjunto_base[len(base_dos)-1-i])
                    
        return resultado                
    #                        
    def potencia(self,A):
            
        aux_A=list(A)
        
        resultado=[]
        for i in range(2**len(aux_A)):
            resultado.append(set(self.subconjunto_asociado(i,aux_A)))  
                                          
        return resultado
    
class Espacio_Topologico:
    #
    """ 
     Conjunto base         
    """
    
    X=set()
    """ 
    Familia de suconjuntos 
    """
    ABIERTOS=[]
    
    """ 
    d : X x X -> R
    
    Implementado con un diccionario
    {
        (a,b) : d(a,b)
    }
    """
    
    d={}
    #
    def __init__(self,X,ABIERTOS,d):
        
        self.X=set(X)
        self.ABIERTOS=ABIERTOS
        self.d=d        
    #
    def es_un_espacio_topologico(self):
        """
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_topologico()
        True
        >>> X={1,2,3,4,5};T=[set([]),X,{1},{1,2},{1,3,4},{1,2,3,4}];d={};Espacio_Topologico(X,T,d).es_un_espacio_topologico()             
        True
        >>> X={1,2,3,4,5};T=[set([]),X,{1}];d={};Espacio_Topologico(X,T,d).es_un_espacio_topologico()        
        True
        >>> X={1,2,3};T=[set([]),X,{2}, {3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_topologico()        
        True
        >>> X={1,2,3};T=[set([]),X,{1}, {3}, {1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_topologico()        
        True
        >>> X={1,2,3};T=[set([]),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_topologico()        
        True
        
        """        
        #
        if self.ABIERTOS==[]:            
            return False                

        if not set([]) in self.ABIERTOS:            
            return False

        if not self.X in self.ABIERTOS:
            return False
        
        for abierto in self.ABIERTOS: 
            if not abierto.issubset(self.X):
                return False            
        #    
        for A in self.ABIERTOS:
            for B in self.ABIERTOS:                        
                if not A.intersection(B) in self.ABIERTOS:                        
                    return False
        #    
        for A in self.ABIERTOS:
            for B in self.ABIERTOS:    
                if not A.union(B) in self.ABIERTOS: 
                    return False                    
        return True    
    #
    def son_topologias_equivalentes(self,X2,T2):
        """
        X2:set
        T2:[set1, set2, ....]
        
        #>>> X1={1,2};T1=[set([]),X1,{1}];d1={};X2={'a','b'};T2=[set([]),X2,{'a'}];Espacio_Topologico(X1,T1,d1).son_topologias_equivalentes(X2,T2)
        True
        """        
        if not len(self.X)==len(X2):
            return False
        
        if not len(self.ABIERTOS)==len(T2):
            return False
        
        
        aux_X1=list(self.X)
        aux_X2=list(X2)
        sustituciones=dict()
        for i in range(len(aux_X1)):
            sustituciones[aux_X2[i]]=aux_X1[i]
            
        T3=[]                
        for abierto in T2:
            aux=set()
            for a in abierto:
                aux.add(sustituciones.get(a))
            T3.append(aux)    
        
        return self.ABIERTOS==T3
    #
    def es_una_topologia_mas_fina(self,T2):
        """ 
        T es más fina que T2 si todo abierto de T2 esta en T
        """
        for t in T2:
            if not t in self.ABIERTOS:
                return False
            
        return True    
    #
    def topologia_relativa(self,A):
        """ 
        A:set
        
        >>> X={1,2,3,4,5};T=[set([]),X,{1},{1,2},{1,3,4},{1,2,3,4}];d={};A={1,3,5};Espacio_Topologico(X,T,d).topologia_relativa(A)             
        [set(), {1, 3, 5}, {1}, {1}, {1, 3}, {1, 3}]
        """
        resultado=[]
        if A.issubset(self.X):
            for abierto in self.ABIERTOS:
                resultado.append(A.intersection(abierto))
                
        return resultado    
    #
    def es_un_subespacio_de(self,X,T):
        """ 
        X: set
        T: [set1,set2,...]
        
        >>> X1={1,2};T1=Conjunto().potencia(X1);d={};X2=X1;T2=[set(),X2];Espacio_Topologico(X1,T1,d).es_un_subespacio_de(X2,T2)
        True
        >>> X1={1,2,3,4,5};T1=[set([]),X1,{1},{1,2},{1,3,4},{1,2,3,4}];d={};X2={1,3,5};T2=[set(), {1, 3, 5}, {1}, {1}, {1, 3}, {1, 3}];T2=[set(),X2];Espacio_Topologico(X1,T1,d).es_un_subespacio_de(X2,T2)             
        True
        
        """
        
        if not X.issubset(self.X):            
            return False
            
        if not Espacio_Topologico(X,T,{}).es_un_espacio_topologico():
            return False
            
        return True
    #
    def es_un_abierto(self,A):        
        """
        A:set
        
        >>> X={'a','b','c','d','e','f'};T=[set([]),{'a'},{'a','b','c','d','e','f'}];d={};Espacio_Topologico(X,T,d).es_un_abierto({'a'})
        True
        
        """        
        if  self.es_un_espacio_topologico() :
            if A in self.ABIERTOS:
                return True
            
        return False
    #
    def es_cerrado(self,A): 
        """
        A:set
        
        Un conjunto cerrado es el complemento de un conjunto abierto en un espacio topológico
        
        Un conjunto es cerrado si y solo si es igual a su clausura topológica
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={};M={1,2};Espacio_Topologico(X,T,d).es_cerrado(M)
        True

        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={};M={1};Espacio_Topologico(X,T,d).es_cerrado(M)
        True
        """      
        if self.es_un_espacio_topologico():        
            if self.X.difference(A) in self.ABIERTOS:
                return True     
            
        return False
    #
    def es_clopen(self,A):
        """ 
        A:set
        """
        return self.es_un_abierto(A) and self.es_cerrado(A)
    #    
    def coTopologia(self):
        """
        X={'a','b','c','d','e','f'};T=[set([]),X];d={};Espacio_Topologico(X,T,d).coTopologia()
        [{'e', 'c', 'd', 'b', 'a', 'f'}, set()]
        
        """ 
        resultado=[]
        if self.es_un_espacio_topologico():            
            for abierto in self.ABIERTOS:
                resultado.append( self.X.difference(abierto) )
                    
        return resultado
    #   
    def es_un_entorno(self,a,A):
        """
        A:set
        
        A es un entorno de a sii a pertenece a un abierto contenido en A
        
        >>> X={'a','b','c','d','e','f'};T=[set([]),X];d={};Espacio_Topologico(X,T,d).es_un_entorno('a',X)
        True
        >>> X={1,2,3};T=[set(),{1},{1,2},{1,3},X];d={};Espacio_Topologico(X,T,d).es_un_entorno(1,{1,2}) 
        True
        >>> X={1,2,3};T=[set(),{1},{1,2},{1,3},X];d={};Espacio_Topologico(X,T,d).es_un_entorno(1,{1,3}) 
        True
        """
        if not A.issubset(self.X):
            return False
        
        for abierto in self.ABIERTOS:
            if a in abierto and abierto.issubset(A):
                return True
            
        return False
    #
    def es_un_entorno_abierto(self,a,A):
        """
        A:set
        
        A es un entorno abierto de a sii A es un entorno de A y A es abierto
        
        >>> X={'a','b','c','d','e','f'};T=[set([]),X];d={};Espacio_Topologico(X,T,d).es_un_entorno_abierto('a',X)
        True
        """
        if not A.issubset(self.X):
            return False
        
        
        for abierto in self.ABIERTOS:
            if a in abierto and abierto.issubset(A):
                if self.es_un_abierto(A):
                    return True
            
        return False
    #
    def es_un_entorno_cerrado(self,a,A):
        """
        A:set
        
        A es un entorno abierto de a sii A es un entorno de A y A es cerrado
        
        >>> X={'a','b','c','d','e','f'};T=[set([]),X];d={};Espacio_Topologico(X,T,d).es_un_entorno_cerrado('a',X)
        True
        
        >>> X={1,2,3};T=[set(),{1},{1,2},{1,3},X];d={};Espacio_Topologico(X,T,d).es_un_entorno_cerrado(1,X)
        True
        """
        if not A.issubset(self.X):
            return False
        
        for abierto in self.ABIERTOS:
            if a in abierto and abierto.issubset(A):
                if self.es_cerrado(A):
                    return True
            
        return False
    #
    def es_un_entorno_conexo(self,a,A):
        """
        A:set
        
        A es un entorno abierto de a sii A es un entorno de A y A es conexo
        
        >>> X={'a','b','c','d','e','f'};T=[set([]),X];d={};Espacio_Topologico(X,T,d).es_un_entorno_conexo('a',X)
        True
           
        """
        if not A.issubset(self.X):
            return False
        
        for abierto in self.ABIERTOS:
            if a in abierto and abierto.issubset(A):
                if self.es_conexo(A):
                    return True
            
        return False
    #
    def es_un_entorno_denso(self,a,A):
        """
        A:set
        
        A es un entorno abierto de a sii A es un entorno de A y A es denso
        
        >>> X={'a','b','c','d','e','f'};T=[set([]),X];d={};Espacio_Topologico(X,T,d).es_un_entorno_denso('a',X)
        True
        
        """
        if not A.issubset(self.X):
            return False
        
        for abierto in self.ABIERTOS:
            if a in abierto and abierto.issubset(A):
                if self.es_denso(A):
                    return True
            
        return False
    #    
    def d_es_una_aplicacion_X_x_X_en_R(self):
        """ 
        d: X x X -> R+
        
        """
        for a in self.X:
            for b in self.X:
                valor=self.d.get((a,b))
                
                if valor==None:
                    return False
                
                if not( type(valor)==int or type(valor)==float):
                    return False
                
                if valor<0:
                    return False
                                
        return True        
    #
    def d_es_regular(self):
        """ 
        d(x,x)=0
        """
        for a in self.X:
            if self.d.get((a,a))!=0:
                return False
        return True            
    #
    def d_es_no_degenerada(self):
        """ 
        (No degeneracion) 
        Si d(x, y) = 0 entonces x = y.
        """
        for par in self.d.items():
            if par[1]==0:
                x=par[0][0]
                y=par[0][1]
                if not x==y:
                    return False
                
        return True                    
    #
    def d_cumple_desigualdad_triangular(self):
        """ 
        d ( x , z ) ≤ d ( x , y ) + d ( y , z ) (desigualdad triangular) 
        """
        for a in self.X:
            for b in self.X:
                for c in self.X:
                    if not self.d.get((a,c))<=self.d.get((a,b))+self.d.get((b,c)):                    
                        return False
        return True                    
    #
    def d_es_simetrica(self):
        """ 
        d ( x , y ) = d ( y , x )  (simetría)
        """
        for a in self.X:
            for b in self.X:
                if self.d.get((a,b))!=self.d.get((a,b)):                    
                    return False
        return True        
    #
    def es_una_pseudometrica(self):    
        """ 
        d: X x X -> R+
        
        d(x,x)=0.
        d ( x , y ) = d ( y , x )  (simetría)
        d ( x , z ) ≤ d ( x , y ) + d ( y , z ) (desigualdad triangular)        
        """
        #           
        if not self.d_es_una_aplicacion_X_x_X_en_R():
            return False                
        #  
        if not self.d_es_regular():
            return False       
        #            
        if not self.d_es_simetrica():
            return False    
        #        
        if not self.d_cumple_desigualdad_triangular():
            return False
    
        return True            
    #    
    def es_una_metrica(self):
        """ 
        d: X x X -> R+
        
        d(x,y)=0 sii x=y
        d ( x , y ) = d ( y , x )  (simetría)
        d ( x , z ) ≤ d ( x , y ) + d ( y , z ) (desigualdad triangular)        
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};Espacio_Topologico(X,T,d).es_una_metrica()
        True
        
        >>> X={1,2,3};T=[set(),{1,2},{1,3},{2,3},X];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};Espacio_Topologico(X,T,d).es_una_metrica()
        True
        
        """
        #
        if not self.d_es_una_aplicacion_X_x_X_en_R():
            return False                
        #     
        if not self.d_es_regular():
            return False   
        #     
        if not self.d_es_no_degenerada():
            return False           
        #  
        if not self.d_es_simetrica():
            return False          
        #
        if not self.d_cumple_desigualdad_triangular():
            return False        
        
        return True                                                
    #
    def distancia_punto_Conjunto(self,a,A):
        """ 
        a: elemento de X
        A:set
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};A={2,3};Espacio_Topologico(X,T,d).distancia_punto_Conjunto(1,A)        
        1
        """
        
        if not self.es_un_espacio_topologico():
            return None
        
        if not a in self.X:
            return None
        
        if not A.issubset(self.X):
            return None
        
        if not self.es_un_espacio_metrico():
            return None
        
        if a in A:
            return 0
        else:            
            distancias=[]
            for b in A:
                distancia=self.d.get((a,b))
                if distancia!=None:                    
                    distancias.append(distancia)
            
            distancias.sort()
            
            return distancias[0]                                            
    #
    def distancia_conjuntos(self,A,B):
        """
        A:set
        B:set
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};A={3};B={1};Espacio_Topologico(X,T,d).distancia_conjuntos(A,B)                
        1
        """
        if not A.issubset(self.X):
                return None
            
        if not B.issubset(self.X):
                return None
        
        distancias=[]
        for a in A:
            for b in B:
                distancia=self.d.get((a,b))        
                distancias.append(distancia)
                
        distancias.sort()
        
        return distancias[0]            
    #
    def distancia(self,a,b):
        """ 
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};Espacio_Topologico(X,T,d).distancia(1,1)
        0
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};Espacio_Topologico(X,T,d).distancia(1,2)
        1
        """
        return self.d.get((a,b))
    #
    def diametro(self,A):
        """ 
        A:set
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};A={2,3};Espacio_Topologico(X,T,d).diametro(A)        
        3

        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};A={1,3};Espacio_Topologico(X,T,d).diametro(A)        
        3
        
        """ 
        if self.es_un_espacio_topologico():
            if self.es_un_espacio_metrico():
                resultado=-1
                for x in A:
                    for y in A:
                        if self.d.get(x,y)>resultado:
                            resultado=self.d.get(x,y)
                return resultado
            
        return None                                
    #
    def es_generado_por_base(self,abierto,base_candidata):
        """ 
        abierto:set
        base_candidata:[set1,set2,...]
        
        >>> X={'a','b','c','d','e','f'};T=[set(),X,{'a'},{'c','d'},{'a','c','d'},{'b','c','d','e','f'}];d={};Espacio_Topologico(X,T,d).es_generado_por_base({'c','d'},[{'a'},{'c','d'},{'b','c','d','e','f'}])                
        True

        """
        
        for i in range(1,2**len(base_candidata)):
            resultado=str(abierto)+"="
            aux=Conjunto().decimal_base_dos(i)
            aux=[0]*(len(base_candidata)-len(aux))+aux
            
            elemento_generado=set([])
            for k in range(len(aux)):                
                if aux[k]==1:                    
                    if elemento_generado==set([]):
                        resultado+=str(base_candidata[k])
                    else:    
                        resultado+=" U "+str(base_candidata[k])
                    
                    elemento_generado=elemento_generado.union(base_candidata[k])
                    
                    
                    if  elemento_generado==abierto:
                           
                        return True     
                     
        return False                                           
    #
    def es_una_base(self,base_candidata):
        """ 
        base_candidata:[set1,set2,...]
        
        >>> X={'a','b','c','d','e','f'};T=[set(),{'a'},X];d={};Espacio_Topologico(X,T,d).es_una_base([{'a'},{'b','c','d','e'}])
        False

        >>> X={'a','b','c','d','e','f'};T=[set(),X,{'a'},{'c','d'},{'a','c','d'},{'b','c','d','e','f'}];d={};Espacio_Topologico(X,T,d).es_una_base([{'a'},{'c','d'},{'b','c','d','e','f'}])                
        True
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_una_base([{1},{2},{3}])                
        True
        
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_una_base([{1,2},{1,3},{2,3}])                
        True
        
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_una_base([X])                
        True
        
        >>> X={1,2,3};T=[set(),{1},{1,2},X];d={};Espacio_Topologico(X,T,d).es_una_base([{1},{1,2}])              
        False
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2},{1,3}];d={};Espacio_Topologico(X,T,d).es_una_base([{1},{1,2},{1,3}])       
        True
        """   
        # Todo elemento de X  tiene que estar en algún elemento de la Base     
        
        for x in self.X:
            elemento_base_encontrado=False
            for elemento_base in base_candidata:
                if x in elemento_base:
                    elemento_base_encontrado=True
            
            if not elemento_base_encontrado:
                
                return False        
            
        # Todo elemento de la Base tiene que ser un Abierto     
        for a in base_candidata:
            if not a in self.ABIERTOS:
                
                return False
            
        # La union de todos los elemento de la Base debe ser igual a X    
        resultado=set()    
        for a in base_candidata:            
            resultado=resultado.union(a)
            
        if not resultado==self.X:
            print(resultado,self.X,base_candidata)
            
            return False
        
        # Todo abierto debe ser generado por elementos de la Base
        Abiertos_No_Vacios=self.ABIERTOS
        Abiertos_No_Vacios.remove(set())
        for abierto in Abiertos_No_Vacios:
            if not self.es_generado_por_base(abierto,base_candidata):
                
                return False
                         
        return True
    #
    def generar_una_distancia(self):
        """ 
        """
        distancia={}
        for a in self.X:
            for b in self.X:
                if distancia.get((a,b))==None:
                    if distancia.get((b,a))==None:                        
                        if a==b :
                            distancia[(a,b)]=0
                            distancia[(b,a)]=0          
                        else:    
                            distancia[(a,b)]=1
                    else:        
                        distancia[(a,b)]=distancia.get((b,a))                        
                            
                
                
        return distancia
    #
    def generar_topologia_inclusion(self,A):
        """ 
        A:set
        
        (X,T) espacio topologico 
        
        T'={0,X} u {B incluido en X / B incluido en A}
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d={};A=X;Espacio_Topologico(X,T,d).generar_topologia_inclusion(A)
        [{1, 2, 3}, set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}]
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d={};A=set();Espacio_Topologico(X,T,d).generar_topologia_inclusion(A)
        [{1, 2, 3}, set()]
        """
        potencia_X=Conjunto().potencia(self.X)
        resultado=[self.X]
        for B in potencia_X:
            if B.issubset(A):
                if not B in resultado:
                    resultado.append(B)
                
        return resultado
    #            
    def generar_todas_las_topologias(self):
        """
        
        n=1 n_topologias=1
        n=2 n_topologias=4
        n=3 n_topologias=29
        n=4 n_topologias=355
        n=5 n_topologias=6942
        
        >>> X={1};T=[];d={};Espacio_Topologico(X,T,d).generar_todas_las_topologias()
        [[set(), {1}]]
        >>> X={1,2};T=[];d={};Espacio_Topologico(X,T,d).generar_todas_las_topologias()
        [[set(), {1, 2}], [set(), {2}, {1, 2}], [set(), {1}, {1, 2}], [set(), {1}, {2}, {1, 2}]]
        """
        
        resultado=[]
        aux=Conjunto().potencia(self.X)
        
        for i in range(2**len(aux)):
            
            self.ABIERTOS=[]     
            
            elementos_elegidos=Conjunto().decimal_base_dos(i)
            elementos_elegidos=[0]*(len(aux)-len(elementos_elegidos))+elementos_elegidos
            
            for j in range(len(aux)):
                if elementos_elegidos[j]==1:     
                    if not set(aux[j]) in self.ABIERTOS:                                    
                        self.ABIERTOS.append(set(aux[j]))

            
            if self.es_un_espacio_topologico():   
                if not self.ABIERTOS in resultado:              
                    resultado.append(self.ABIERTOS)
                    
        return resultado
    #
    def topologia_generada_por(self,familia):
        """
        familia:[set1,set2,...]
        
        
        >>> X={1,2,3,4,5};T=[];d={};Espacio_Topologico(X,T,d).topologia_generada_por([{1,2,3},{3,4},{4,5}])
        [set(), {3}, {1, 2, 3}, {4}, {3, 4}, {1, 2, 3, 4}, {4, 5}, {3, 4, 5}, {1, 2, 3, 4, 5}]
        """
        intersecciones_posibles_en_familia=[]
        for i in range(2**len(familia)):
            elementos_elegidos=Conjunto().decimal_base_dos(i)
            elementos_elegidos=[0]*(len(familia)-len(elementos_elegidos))+elementos_elegidos            
            
            aux=set()
            for j in range(len(elementos_elegidos)):
                    if elementos_elegidos[j]==1:     
                        if aux==set():
                            aux=familia[j]                                    
                        else:
                            aux=aux.intersection(familia[j])
                            
            if not aux in intersecciones_posibles_en_familia:                
                intersecciones_posibles_en_familia.append(aux)    
                   
            
        resultado=[]    
        for i in range(2**len(intersecciones_posibles_en_familia)):  
            elementos_elegidos=Conjunto().decimal_base_dos(i)
            elementos_elegidos=[0]*(len(intersecciones_posibles_en_familia)-len(elementos_elegidos))+elementos_elegidos            
            
            aux=set()
            for j in range(len(elementos_elegidos)):
                    if elementos_elegidos[j]==1:     
                        if aux==set():
                            aux=intersecciones_posibles_en_familia[j]                                    
                        else:
                            aux=aux.union(intersecciones_posibles_en_familia[j]) 
                                                                    
            if not aux in resultado:                
                resultado.append(aux)    
                             
        return resultado            
    #
    def generar_sistema_entornos_punto(self,a):
        """
        
        >>> X={1,2,3};T=[set(),{1},{1,2},{1,3},X];d={};Espacio_Topologico(X,T,d).generar_sistema_entornos_punto(1) 
        [{1}, {1, 2}, {1, 3}, {1, 2, 3}]
        """
        
        resultado=[]
        if self.es_un_espacio_topologico():               
            subconjuntos=Conjunto().potencia(self.X)
            posibles_entornos=[subconjunto for subconjunto in subconjuntos if   a in subconjunto]
            for subconjunto in posibles_entornos:                                                     
                    for abierto in self.ABIERTOS:
                        if a in abierto:
                            if abierto.issubset(subconjunto):
                                aux1=set(subconjunto)
                                if not aux1 in resultado:
                                    resultado.append(aux1)
                             
                
        return resultado
    #
    def generar_sistema_entornos_cerrados_punto(self,a):
        """
        
        >>> X={1,2,3};T=[set(),{1},{1,2},{1,3},X];d={};Espacio_Topologico(X,T,d).generar_sistema_entornos_cerrados_punto(1) 
        [{1, 2, 3}]
        """
        
        resultado=[]
        if self.es_un_espacio_topologico():               
            subconjuntos=Conjunto().potencia(self.X)
            posibles_entornos=[subconjunto for subconjunto in subconjuntos if   a in subconjunto and self.es_cerrado(subconjunto)] 
            for subconjunto in posibles_entornos:                                                     
                    for abierto in self.ABIERTOS:
                        if a in abierto:
                            if abierto.issubset(subconjunto):
                                aux1=set(subconjunto)
                                if not aux1 in resultado:
                                    resultado.append(aux1)
                             
                
        return resultado            
    #
    def generar_sistema_entornos_densos_punto(self,a):    
        """        
        >>> X={1,2,3,4};T=[set(),{1},{1,2},{1,3},X];d={};Espacio_Topologico(X,T,d).generar_sistema_entornos_densos_punto(1) 
        []
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).generar_sistema_entornos_densos_punto(1) 
        []
        """
        
        resultado=[]
        if self.es_un_espacio_topologico():               
            subconjuntos=Conjunto().potencia(self.X)
            posibles_entornos=[subconjunto for subconjunto in subconjuntos if   a in subconjunto and self.es_denso(subconjunto)] 
            for subconjunto in posibles_entornos:                                                     
                    for abierto in self.ABIERTOS:
                        if a in abierto:
                            if abierto.issubset(subconjunto):
                                aux1=set(subconjunto)
                                if not aux1 in resultado:
                                    resultado.append(aux1)
                             
                
        return resultado                    
    #
    def son_puntos_indistinguibles(self,a,b):
        """
                        
        >>> X={1,2,3};T=[set([]),{3},X];d={};Espacio_Topologico(X,T,d).son_puntos_indistinguibles(1,2)                
        True
                
        """
        entornos_a=self.generar_sistema_entornos_punto(a)
        entornos_b=self.generar_sistema_entornos_punto(b)
        
        return entornos_a==entornos_b
    #
    def es_un_espacio_pseudometrico(self):
        """ 
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 0, (3, 3): 0};Espacio_Topologico(X,T,d).es_un_espacio_pseudometrico()
        True
        
        """
        if self.es_un_espacio_topologico():
            if self.es_una_pseudometrica():
                return True
            
        return  False
    #
    def es_un_espacio_metrico(self):
        """ 
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d = {(1, 1): 0, (1, 2): 1, (1, 3): 1,(2, 1): 1, (2, 2): 0, (2, 3): 1,(3, 1): 1, (3, 2): 1, (3, 3): 0};Espacio_Topologico(X,T,d).es_un_espacio_metrico()
        True
        
        """
        if self.es_un_espacio_topologico():
            if self.es_una_metrica():
                return True
            
        return  False
    #    
    def es_un_espacio_separable(self):
        """ 
        Definition 5.5 
         A topological space X is said to be separable if it contains a countable dense subsets.
        """    
        for abierto in self.abiertos_cerrados:
            if self.es_denso(abierto):
                return True
            
        return False    
    # 
    def es_un_espacio_T0(self):
        """
        
        También llamado Espacio de Kolmogorov
        
        T0 si cuando x, y son dos puntos distintos en X, existe un abierto que contiene        
        sólo a uno de ellos.
        
        Topologia.Carlos Ivorra. Pag 139.
        
        >>> X={1,2,3};T=[set(),{1},{2,3},X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T0()
        False

        >>> X={1,2,3};T=[set(),{1},{2,}{1,2},X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T0()
        True

        
        >>> X={1,2,3};T=[set(),X,{1}, {2}, {3}, {1,2}, {1,3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T0()
        True
        
        >>> X={1,2,3};T=[set(),X,{2}, {3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T0()
        True
        
        >>> X={1,2,3};T=[set(),X,{1,2}, {1,3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T0()
        False
        """
        if not self.es_un_espacio_topologico():
            return False

        for a in self.X:
            for b in self.X:      
                if not a==b :                                                          
                    encontrado_abierto=False
                    for abierto in self.ABIERTOS:
                        if abierto!=set():                            
                            if ( a in abierto and not b in abierto ) or ( not a in abierto and  b in abierto ):
                                encontrado_abierto=True
                                break
                            
                    if not encontrado_abierto:                        
                        return False    
                
        return True        
    #
    def es_un_espacio_de_Kolmogorov(self):
        return self.es_un_espacio_T0()
    #
    def es_un_espacio_T1(self):
        """
        Espacio de Frechet
        
                
        Pruebas :
        

        >>> X={1,2};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_T1()
        True
                
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_T1()
        True
            
        >>> X={1,2,3};T=[set(),X,{2}, {3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T1()
        False
        

        >>> X={1,2,3,4};T=[set(),X,{2,3,4},{1,3,4},{1,2,4},{1,2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T1()
        False

        >>> X={1,2,3,4,5};T=[set(),X,{1}, {2}, {3, 4, 5}, {1, 2}, {1, 3, 4, 5}, {2, 3, 4, 5}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T1()
        False
        
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T1()
        False

        
        """
        #
        def criterio1():
            """
            T1 si para todos x, y ∈ X con x ̸= y, existen U, V entornos abiertos de x e y 
            respectivamente tal que x ∈ V e y ̸∈ V e y x ̸∈ U e y ∈ U
            
            T1 si cuando x, y son dos puntos distintos en X, existe un abierto U tal que
            x pertenece U e  y no pertenece U.
            
            Topologia.Carlos Ivorra. Pag. 139
            """
            for x in self.X:
                for y in self.X:
                    if not x==y:
                        encontrados_abiertos=False
                        for U in self.ABIERTOS:
                            for V in self.ABIERTOS:
                                if not U==set() and not V==set():
                                    if x in U and not y in U  and not x in V and y in V:
                                         encontrados_abiertos=True
                        if not encontrados_abiertos:                            
                            return False
            return True                             
        #    
        def criterio2():
            """ 
            T1 sii todo punto es un conjunto cerrado
            """
        
            
            cerrados=self.cerrados()
            
            for x in self.X:
                if not set([x]) in cerrados:                                            
                    return False
                
            return True    
        #        
        if not self.es_un_espacio_topologico():                      
            return False

                    
        return criterio2()
    #
    def es_un_espacio_fuertemente_T1(self): 
        """ 

        Definicion 2.1. Un espacio topologico (X, T) se dice fuertemente T1, o,
        abreviadamente, F-T1, si satisface que, para todos x, y ∈ X, con x != y,
        existen U, V ∈ T tales que
        U ∩ {x, y} = {x}, V ∩ {x, y} = {y}, U ∪ {y} /∈ T, V ∪ {x} /∈ T.        
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_fuertemente_T1()        
        
        >>> X={1,2,3,4};T=[set(),X, {1}, {2}, {3, 4}, {1, 2}, {1, 3, 4}, {2, 3, 4}];d={};Espacio_Topologico(X,T,d).es_un_espacio_fuertemente_T1()
        
        >>> X={1,2,3,4};T=[set(),X,  {3}, {4}, {1, 2}, {3, 4}, {1, 2, 3}, {1, 2, 4}];d={};Espacio_Topologico(X,T,d).es_un_espacio_fuertemente_T1()
        """

        if not self.es_un_espacio_T1():            
            return False
        
        for x in self.X:
            for y in self.X:
                if not x==y:
                    encontrados_abiertos=False
                    for U in self.ABIERTOS:
                        for V in self.ABIERTOS:
                            if U.intersection(set([x,y]))==set([x]):
                                if V.intersection(set([x,y]))==set([y]):
                                    if not U.intersection(set([y])) in self.ABIERTOS:
                                        if not V.intersection(set([x])) in self.ABIERTOS:
                                            encontrados_abiertos=True
                    
                    if not encontrados_abiertos:
                        return False                        
                                    
        return True
    #
    def es_un_espacio_T2(self):
        """
        
         Tambien llamado espacio T2
         
         Un espacio topológico (X,T) es de Hausdorff o T2 si para cada par x,y de puntos distintos 
         existen dos abiertos A,B ∈ T disjuntos tales que x∈A e y∈B.
         
        T2 si cuando u, v pertenecen X, son dos puntos distintos, existen abiertos disjuntos U,
        V en X tales que u pertenece U, v pertenece V .         
        
        Topologia. Carlos Ivorra. Pag 139.
         
         >>> X={1,2};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         True

         
         >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         True

         >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         True

         >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False

         >>> X={1,2,3,4};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False
         
         >>> X={1,2,3};T=[set(),X,  {2}, {3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False
         
         >>> X={1,2,3};T=[set(),X,  {1}, {3}, {1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False
         
         >>> X={1,2,3};T=[set(),X,  {1}, {2}, {1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False

         >>> X={1,2,3};T=[set(),X,  {1},  {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False

         >>> X={1,2,3};T=[set(),X,   {3}, {1, 2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False

         >>> X={1,2,3,4};T=[set(),X, {1}, {2}, {3, 4}, {1, 2}, {1, 3, 4}, {2, 3, 4},];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False

         >>> X={1,2,3,4};T=[set(),X, {1, 2}, {3, 4},];d={};Espacio_Topologico(X,T,d).es_un_espacio_T2()
         False
        """
        if not self.es_un_espacio_topologico():                      
            return False

        if not self.es_un_espacio_T1 ():                      
            return False
        
        for x in self.X:
            for y in self.X:
                if not  x==y:
                    encontrados_abiertos=False
                    for A in self.ABIERTOS:
                        for B in self.ABIERTOS:
                            if not (A==set() or B==set()):
                                if A.intersection(B)==set([]):
                                    if (x in A and y in B) or (y in A and x in B):
                                        encontrados_abiertos=True
                                        break
                                
                    if not encontrados_abiertos:                        
                        return False                
                                
        return True
    #
    def es_un_espacio_de_Haussdorf(self):
        """
        """
        return self.es_un_espacio_T2()
    #    
    def es_un_espacio_T2_1_2(self):
        """ 
        Urysohn space, or T2½ space, is a topological space in which any 
        two distinct points can be separated by closed neighborhoods.
        """
        pass
    #
    def es_un_espacio_de_Urysohn(self):
        return self.es_un_espacio_T2_1_2()
    #    
    def es_un_espacio_T3(self):
        """ 
        T3 si es T1 y cuando C subconjunto de X es cerrado y p pertenece X - C, existen abiertos disjuntos
        U y V tales que p pertenece U, C subconjunto de V .
        
        Topologia. Carlos Ivorra.Pag 139.
        
        T3 si es un espacio regular y T1.
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T3()
        True
                
        >>> X={1,2,3}; T=[set(),X,{2},{3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T3()
        False
                
        >>> X={1,2,3};  T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T3()
        False
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T3()
        False
        
        >>> X={1,2,3};   T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T3()
        True
        """
        if not self.es_un_espacio_T1():            
            return False
                    
        return self.es_un_espacio_regular()
    #
    def es_un_espacio_de_Tychonoff(self):
        """                
        
        T3 1 2 o Tychonoff si es un espacio completamente regular y T1.        
        
        >>> X={1,2,3}; T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Tychonoff()
        True

        >>> X={1,2,3}; T=[set(),X,{2},{3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Tychonoff()
        False
        
        """
        if self.es_un_espacio_T1():
            if self.es_un_espacio_completamente_regular():
                return True
            
        return False    
    #
    def es_un_espacio_T3_1_2(self):
        """
        """
        return self.es_un_espacio_de_Tychonoff()
    #
    def es_un_espacio_T4(self):
        """
        Definición 5.10 Se dice que un espacio topológico X es normal, o que cumple
        el axioma T4, si es T1 y cuando C1, C2 incluido en X son cerrados disjuntos, existen
        abiertos disjuntos U1 y U2 tales que C1 incluido en U1 and C2 incluido en U2.        
        
        Teorema 5.11 Un espacio X que cumpla el axioma T1 es normal si y sólo
        si cuando C subconjunto de U son un cerrado y un abierto, respectivamente, existe otro
        abierto V tal que C subconjunto de V subconjunto de U.
        
        Topologia. Carlos Ivorra.Pag 143.
        
        T4 si es un espacio normal y T1.
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T4()
        False
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T4()
        True
        
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T4()
        False
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T4()
        True
        
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T4()
        False

        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T4()
        False
        
        
        
        if self.es_un_espacio_T1():
                cerrados=self.cerrados()
                for C1 in cerrados:
                    for C2 in cerrados:
                        if C1.intersection(C2) == set():
                            encontrados_abiertos=False
                            for U1 in self.ABIERTOS:
                                for U2 in self.ABIERTOS:
                                    if U1.intersection(U2)==set():
                                        if C1.issubset(U1) and C2.issubset(U2):
                                            encontrados_abiertos=True
                            
                            if not encontrados_abiertos:
                                return False                
                                            
                                        
                return True
        """    
        if self.es_un_espacio_T1():
            if self.es_un_espacio_normal():
                return True
            
        return False
    #
    def es_un_espacio_T4_1_2(self):
        """ 
        T4 1/2 si es un espacio completamente normal y T1.
        """
        if self.es_un_espacio_T1():
            if self.es_un_espacio_completamente_normal ():
                return True
        
        return False    
    #
    def es_un_espacio_perfectamente_T4(self):
        """
        T es T4
        Every closed set in T can be written as a countable intersection of open sets of T.
        """
        if  self.es_un_espacio_T4():
            cerrados=self.cerrados()
            for cerrado in cerrados:
                for i in range(2**len(cerrados)):
                    elementos_elegidos=Conjunto().decimal_base_dos(i)
                    elementos_elegidos=[0]*(len(cerrados)-len(elementos_elegidos))+elementos_elegidos            
                
                    encontrada_union=False
                    aux=set()
                    for j in range(len(elementos_elegidos)):
                        if elementos_elegidos[j]==1:     
                            if aux==set():
                                aux=cerrados[j]                                    
                            else:
                                aux=aux.union(cerrados[j]) 
                                                
                    if cerrado==aux:
                        encontrada_union=True
                        break
                if not encontrada_union:
                    return False        
        
        return True
    #    
    def es_un_espacio_T5(self):
        """ 
        Def 1:
        
        Es T1 (los puntos son cerrados).
        Es T4 (normal: los cerrados disjuntos pueden separarse con abiertos disjuntos).
        
        Para cualquier par de conjuntos A,B⊆X donde A y B son cerrados y disjuntos, los abiertos 
        U y V que separan A y B pueden elegirse de forma que contengan exactamente a A y B, respectivamente. 
        Esto asegura una separación completa entre cerrados disjuntos.

        Def 2:
        
        Es T5, si es T1 y, cuando dos subconjuntos A, B incluidos en  X  cumplen interseccion(clausura(A),B)  = interseccion(A, clausura(B)) = 0, entonces 
        existen abiertos disjuntos U y V en X tales que A incluido en  U, B incluido en  V .
        
        Topologia. Carlos Ivorra. Pag 145.
                
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_T5()
        False
        
        
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T5()
        True
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{2,3},{1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T5()
        False
        
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_T5()
        False
        
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_T5()
        True
        
        """
        if self.es_un_espacio_topologico():
            return False
        
        if self.es_un_espacio_T1():
            return False
        
        if self.es_un_espacio_T4():
            return False
        
        cerrados=self.cerrados()
        for A in cerrados:
            for B in cerrados:
                if A.intersection(B)==set():
                    encontrado_abierto=False
                    for U in self.ABIERTOS:
                        for V in self.ABIERTOS:
                            if A.issubset(U) and B.issubset(V):
                                encontrado_abierto=True
                    
                    if not encontrado_abierto:
                        return False  
                              

        return True            
    #
    def es_un_espacio_normal(self):
        """ 
                
        The space X is said to be normal if for each pair A, B of disjoint closed sets of X, there exist disjoint open sets
        containing A and B, respectively.
        
        Let (X,ℑ) be a topological space. Then Let (X,ℑ) is said to be “normal space” if for every pair of disjoint closed sets F1, F2 ⊂ X. This implies 
        there exist ℑ-open sets G and H such that F1 ⊂ G, F2 ⊂ H G ∩ H = φ    
        
        Normal si para cualesquiera A y B subconjuntos cerrados disjuntos de X, existen U, V abiertos
        disjuntos con A ⊂ U y B ⊂ V .            
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_normal()
        True
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_normal()
        True
                        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{1,2},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_normal()
        True

        >>> X={1,2,3}; T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_normal()
        True
        
        
    
        """
        if not self.es_un_espacio_topologico():
            return False
        
        cerrados=self.cerrados()
        for  C1 in cerrados:      
            for  C2 in cerrados:
                if C1.isdisjoint(C2):
                    encontrados_abiertos=False
                    for U1 in self.ABIERTOS:
                        for U2 in self.ABIERTOS:
                            if U1.isdisjoint(U2):
                                if C1.issubset(U1) and C2.issubset(U2):
                                    encontrados_abiertos=True
                    if not encontrados_abiertos:
                        return False                
        return True
    #
    def es_un_espacio_completamente_normal(self):
        """
        Es T1 (los puntos son cerrados).
        Es T4 (normal: los conjuntos cerrados disjuntos pueden separarse con abiertos disjuntos).
        
        Para cualquier par de conjuntos A,B⊆XA,B⊆X, donde A y B son cerrados y disjuntos, los 
        abiertos U y V que separan A y B pueden elegirse de forma que contengan exactamente A y B, respectivamente.
        
        Completamente regular si para todo cerrado A de X y para todo x ̸∈ A existe una aplicaci´on
        continua f : X → [0, 1] tal que f(x) = 0 y f(A) = 1.        
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_normal()
        True
        
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_normal()
        True
        
        
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_normal()
        True
        
        
        """
        if not self.es_un_espacio_topologico():
            return False
        
        if self.es_un_espacio_T1():
            return False
        
        if self.es_un_espacio_T4():
            return False
        
        cerrados=self.cerrados()
        for A in cerrados:
            for B in cerrados:
                if A.intersection(B)==set():
                    encontrados_abiertos=False
                    for  U in self.ABIERTOS:
                        for  V in self.ABIERTOS:
                            if A.issubset(U):
                                if B.issubset(V):
                                    encontrados_abiertos=True
                                    break
                    if not encontrados_abiertos:
                        return False            
        return True
    #
    def es_un_espacio_perfecto(self):
        """
        Definición 6.16 Un espacio topológico es perfecto si no tiene puntos aislados.
        
        Topologia. Carlos Ivorra. Pag 185
        """
        
        if not self.es_un_espacio_topologico():
            return False
        
        return self.aislados(self.X)==set()
    #
    def es_un_espacio_conexo(self):
        """
        
        (X,T) es conexo si no existen dos abiertos U, V disjuntos no vacios 
        tales que X = U ∪ V
        
        Definición 3.1 Un espacio topológico X es disconexo si existen subconjuntos
        abiertos U y V en X tales que X = U ∪ V , U - V = set() y U != set() != V . En caso
        contrario se dice que X es conexo.
        
        >>> X={1,2,3}; T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_conexo()
        True

        >>> X={1,2,3}; T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_conexo()
        True
        
        >>> X={1,2,3}; T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_conexo()
        True
        
        >>> X={1,2,3}; T=[set(),X,{1,2},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_conexo()
        True
        
        >>> X={1,2,3}; T=[set(),X,{1},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_conexo()
        False
        
        """
        for u in self.ABIERTOS:
            for v in self.ABIERTOS:
                if not u ==set([]) and not v ==set([]):
                    if u.intersection(v)==set([]):
                        if u.union(v)==self.X:                            
                            return False
                        
        return True                            
    #        
    def es_un_espacio_hiperconectado(self):
        """
        
        Un espacio está hiperconectado si cualesquiera dos conjuntos abiertos no vacíos 
        son no disjuntos.
        
                

                
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_hiperconectado()
        True
        
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_hiperconectado()
        True

        
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_hiperconectado()
        True
        
        >>> X={1,2,3};T=[set(),X,{1,2},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_hiperconectado()
        True
        
        
        """
        Vacio=set([])
        
        for A in self.ABIERTOS:
            for B in self.ABIERTOS:
                if not A==Vacio and not B==Vacio:
                    if A.intersection(B)==Vacio:
                        return False
                
        return True
    #
    def es_un_espacio_semiregular(self):    
        """ 
        (S,τ) is a Hausdorff (T2) space
        The regular open sets of T form a basis for T.
        """
        if not self.es_un_espacio_T2():
            return False
        
        abiertos_regulares=[]
        for abierto in self.ABIERTOS:
            if self.es_un_abierto_regular(abierto):
                abiertos_regulares.append(abierto)
                                                                    
        return self.es_una_base(abiertos_regulares)
    #
    def es_un_espacio_regular(self):
        """ 

        Regular si para todo cerrado A de X y para todo x ̸∈ A, existen dos 
        abiertos disjuntos  U, V con x ∈ U y A ⊂ V .

        Let (X,ℑ) be a topological space. Then Let (X,ℑ) is said to be “regular space” if given an element x ∈ X and 
        closed set F ⊂ X such that x ∉ F There exist disjoint open sets G, H ⊂ X such that
        x ∈ G, F ⊂ H.        
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_regular()
        True
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{1,2},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_regular()
        True
        
        >>> X={1,2,3};T=[set(),X,{2},{3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_regular()
        True
        
        >>> X={1,2,3};T=[set(),X,{1},{3},{1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_regular()
        True
                
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_regular()
        True
                
        """
        cerrados=self.cerrados()
        for A in cerrados:
            complemento_A=self.X.difference(A)
            for x in complemento_A:
                encontrados_abiertos=False
                for U in self.ABIERTOS:                            
                    for V in self.ABIERTOS:
                        if U.isdisjoint(V):
                            if x in U:
                                if A.issubset(V):
                                    encontrados_abiertos=True
                if not encontrados_abiertos:
                    return False                    
        return True
    #    
    def es_un_espacio_localmente_conexo(self):
        """
        Definición 3.8 Un espacio topológico es localmente conexo si todo punto tiene
        una base de entornos conexos.
        
        Teorema 3.9 Un espacio topológico es localmente conexo si y sólo si las componentes
        conexas de sus abiertos son abiertas (luego también cerradas).
        
        Todo espacio topologico finito es localmente conexo
        """
        if self.es_un_espacio_topologico():
            return True
        
        return False
    #    
    def es_un_espacio_localmente_conexo_por_caminos(self):
        """ 
            Todo espacio topologico finito es localmente conexo por caminos.
        """ 
        if self.es_un_espacio_topologico():
            return True
        
        return False        
    #
    def es_un_espacio_de_Baire(self):
        """
        
        Un espacio de Baire es un espacio topológico en el que la unión numerable de subconjuntos cerrados 
        y de interior vacío tiene interior vacío.
        
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Baire()
        True

        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Baire()
        False
            
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Baire()
        False
    
        >>> X={1,2,3};T=[set(),X,{1,2},{1,3},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Baire()
        False        
        
        >>> X={1,2,3};T=[set(),X,{1,2},{2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Baire()
        False
        
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Baire()
        True
        
        >>> X={1,2,3,4};T=[set(),X,{1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_de_Baire()
        False
                
        """
        #
        def criterio1():
            """ 
            Un espacio topologico (X, T ) se dice espacio de Baire si toda interseccion numerable 
            de abiertos densos de X es densa.

            """
            abiertos_densos=[]
            for abierto in self.ABIERTOS:
                if self.es_denso(abierto):
                    abiertos_densos.append(abierto)
            
            for i in range(2**len(abiertos_densos)):
                elementos_elegidos=Conjunto().decimal_base_dos(i)
                elementos_elegidos=[0]*(len(abiertos_densos)-len(elementos_elegidos))+elementos_elegidos            
            
                aux=set()
                for j in range(len(elementos_elegidos)):
                    if elementos_elegidos[j]==1:     
                        if aux==set():
                            aux=abiertos_densos[j]                                    
                        else:
                            aux=aux.union(abiertos_densos[j]) 
                                               
                if not self.es_denso(aux):
                    return False
            
            return True            
        #
        if not self.es_un_espacio_topologico():
            return False
                        
        return criterio1()
        #
        def es_un_espacio_extremadamente_disconexo(self):
            """ 
        Es extremadamente disconexo si el cierre de cualquier conjunto abierto es también abierto.
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{2,3},{1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_extremadamente_disconexo()
        True
        
        >>> X={1,2,3}; T=[set(),X, {2}, {3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_extremadamente_disconexo()
        True
        
        >>> X={1,2,3}; T=[set(),X, {1}, {3}, {1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_extremadamente_disconexo()
        True

        >>> X={1,2,3}; T=[set(),X,{1}, {2}, {1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_extremadamente_disconexo()
        True
        
        >>> X={1,2,3}; T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_extremadamente_disconexo()
        True
        
        """
        if self.es_un_espacio_de_Haussdorf():
            for abierto in self.ABIERTOS:
                if not self.clausura(abierto) in self.ABIERTOS:
                    return False
        
        return True 
    #    
    def es_un_espacio_completamente_de_Hausdorff(self):
        """ Pendiente
        
        
        """
        #
        def criterio1():
            """ 
            Es completamente de Hausdorff si cuando p, q  X son puntos distintos,
            están completamente separados.                
            """
            for x in self.X:
                for y in self.X:
                    if not x==y:
                        if not self.estan_completamente_separados():
                            return False
            return True            
            
        #
        def criterio2():
            """ 
            En espacios finitos, ser completamente de Hausdorff es equivalente a ser T1
            """
            return self.es_un_espacio_T1()
        #
        if not self.es_un_espacio_topologico():
            return False
        
        return criterio1()
    #
    def es_un_espacio_completamente_regular(self):
        """ 
        (X,T ) es completamente regular sii es T1 y es Normal    
        
        Es completamente regular si cuando C < X es un cerrado y p en  X - C,
        entonces p y C están completamente separados.
        
        Topología discreta:

        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_regular()
        True
                
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_regular()
        True
        
        Topología del punto excluido en 1:
        
        >>> X={1,2,3,4};T = [set(),X, {2}, {3}, {2,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_regular()
        False
        
        Topología del punto excluido en 2:
        
        >>> X={1,2,3};T = [set(),X, {1}, {3}, {1,3}];d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_regular()
        
        Topología del punto excluido en 3:
        
        >>> X={1,2,3};T = [set(),X, {1}, {2}, {1,2}];d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_regular()
        
        
        """
        #
        if not self.es_un_espacio_T1():
            return False
        
        return self.es_un_espacio_normal()
    #
    def es_un_espacio_completamente_normal(self):
        """ 
        En espacios finitos, ser completamente normal es equivalente a ser T1    
        Es completamente normal si cuando C1, C2 < X son cerrados disjuntos en X, están completamente separados.
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_normal()  
        True

        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).es_un_espacio_completamente_normal()  
        True
        
        """ 
        cerrados=self.cerrados()
        
        for C1 in cerrados:            
            for C2 in cerrados:
                if C1.intersection(C2)==set():
                    if not self.estan_completamente_separados(C1,C2):
                        return False
        return True
    #
    def es_un_espacio_perfectamente_normal(self):
        """ 
    
        Es T1 y todo par de cerrados disjuntos en X están perfectamente separados.
        
        >>> X={1};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_perfectamente_normal() 
        True
               
        >>> X={1,2};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_perfectamente_normal()        
        True
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_perfectamente_normal()  
        True
              
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_perfectamente_normal() 
        True
        

        Cualquier espacio topológico finito con la topología discreta:
        X = {x1, x2, ..., xn}
        T = P(X) (conjunto potencia de X)
        
        """ 
        if self.es_un_espacio_T1():
            cerrados=self.cerrados()
            for C in cerrados:
                for D in cerrados:
                    if C.intersection(D)==set():
                        if not self.estan_completamente_separados(C,D):
                            return False
            return True            
    #
    def es_un_espacio_uniformizable(self):
        """ 
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_uniformizable() 
        True
        
        """
        if self.es_un_espacio_T0():
            if self.es_un_espacio_completamente_regular():
                return True
            
        return False        
    #
    def es_un_espacio_fuertemente_cerodimensional(self):
        """ 
        Cualquier espacio topológico finito con la topología discreta:
        X = {x1, x2, ..., xn}
        T = P(X) (conjunto potencia de X)        
        
        
        Un espacio topológico X es fuertemente cerodimensional si es
        completamente regular, no vacío y, cuando A, B < X son disjuntos y están
        completamente separados, existe un abierto cerrado C en X de manera que
        A < C, B < X - C.        
        
        >>> X={1};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_fuertemente_cerodimensional()        
        True
        
        >>> X={1,2};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_fuertemente_cerodimensional()        
        True
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_fuertemente_cerodimensional()        
        True
        
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_fuertemente_cerodimensional()          
        True
        """        
        if self.X==set():
            return False
        
        if not self.es_un_espacio_completamente_regular():
            return False
                                            
        abiertos_cerrados=self.abiertos_cerrados()
        potencia=Conjunto().potencia(self.X)
        for A in potencia:
            for B in potencia:
                if A.intersection(B)==set():
                    if self.estan_completamente_separados(A,B):
                        encontrado_abierto_cerrado=False
                        for a_c in abiertos_cerrados:
                            if a_c.issubset(A):
                                if a_c.issubset(B):
                                    encontrado_abierto_cerrado=True
                                    break
                        if not encontrado_abierto_cerrado:
                            return False
                        
        return True                                
    #
    def es_un_espacio_polaco(self):
        """
        Un espacio polaco es un espacio topológico completamente metrizable
        con una base numerable 
        
        Cualquier conjunto finito X = {x1, x2, ..., xn} con la topología discreta:
        T = P(X) (conjunto potencia de X)        
        
        >>> X={1};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_polaco()   
        True
             
        >>> X={1,2};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_polaco()        
        True
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_polaco()        
        True
        
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_un_espacio_polaco()          
        True
        
        """
        if self.es_un_espacio_topologico():
            if self.es_un_espacio_completamente_metrizable():
                return True
            
        return False    
    #    
    def es_un_espacio_completamente_metrizable(self):
        """ 
        En espacios topologicos finitos ser T1 equivale a ser completamente metrizable
        """
        return self.es_un_espacio_T1()
    #
    def es_un_espacio_compacto(self):
        """
        Todo espacio topologico finito es compacto
        """
        if self.es_un_espacio_topologico():
            return True
        
        return False        
    #
    def es_un_espacio_localmente_compacto(self):
        """
        Todo espacio topologico finito es localmente compacto
        """
        if self.es_un_espacio_topologico():
            return True
        
        return False        
    #
    def es_un_espacio_irreducible(self):
        """ 
        (X,T) es irreducible sii todo conjunto abierto no vacıo en X es denso en X
        """
        abiertos_no_vacios=[abierto for abierto in self.ABIERTOS if not abierto==set()]
        for abierto in abiertos_no_vacios:
            if not self.es_denso(abierto):
                return False
            
        return False                
    #
    def es_una_topologia_de_Sierpinski(self):
        """
        >>> X={1,2};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_una_topologia_de_Sierpinski()        
        False
        >>> X={1,2};T=[set(),X,{1}];d={};Espacio_Topologico(X,T,d).es_una_topologia_de_Sierpinski() 
        True
        """
        
        if not len(self.X)==2:
            return False

        if not len(self.ABIERTOS)==3:
            return False
                
        if not self.es_un_espacio_topologico():
            return False
                
        return True   
    #
    def es_un_espacio_de_Alexandrov(self):
        """ 
        Definicion 2.1. Un espacio topologico (X,T) se dice de Alexandrov (o A-espacio)
        si T es cerrado respecto a las intersecciones arbitrarias.
        """
        for A in self.ABIERTOS:
            for B in self.ABIERTOS:                        
                if not A.intersection(B) in self.ABIERTOS:                        
                    return False
                
        return True
    #
    def generar_subespacios(self):
        """ 
        >>> X={1,2,3};T=[set([]),X,{1}, {3}, {1,3}];d={};Espacio_Topologico(X,T,d).generar_subespacios()  
        [(set(), [set()]), ({1}, [set(), {1}]), ({2}, [set(), {2}]), ({1, 2}, [set(), {1, 2}, {1}]), ({3}, [set(), {3}]), ({1, 3}, [set(), {1, 3}, {1}, {3}]), ({2, 3}, [set(), {2, 3}, {3}]), ({1, 2, 3}, [set(), {1, 2, 3}, {1}, {3}, {1, 3}])]
        """
        if not self.es_un_espacio_topologico():
            return []
        
        subconjuntos_de_X=Conjunto().potencia(self.X)
        resultado=[]
        for subconjunto in subconjuntos_de_X:
            topologia_asociada=[]
            for abierto in self.ABIERTOS:
                nuevo_abierto=abierto.intersection(subconjunto)
                if not nuevo_abierto in topologia_asociada:
                    topologia_asociada.append(nuevo_abierto)
            resultado.append((subconjunto,topologia_asociada))    
        return resultado
    #
    def generar_espacios_T0(self):
        """ 
        >>> X={1,2};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T0()
        [[set(), {2}, {1, 2}], [set(), {1}, {1, 2}], [set(), {1}, {2}, {1, 2}]]
        """ 
        topologias=self.generar_todas_las_topologias()
        
        resultado=[]
        for topologia in topologias:
            self.ABIERTOS=topologia
            if self.es_un_espacio_T0():
                resultado.append(topologia)
        return resultado
    #
    def generar_espacios_T1(self):
        """ 
        >>> X={1,2};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T1()
        [[set(), {1}, {2}, {1, 2}]]
        
        >>> X={1,2,3};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T1()
        [[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]]
        
        """ 
        topologias=self.generar_todas_las_topologias()
        
        resultado=[]
        for topologia in topologias:
            self.ABIERTOS=topologia
            if self.es_un_espacio_T1():
                resultado.append(topologia)
        return resultado
    #
    def generar_espacios_T2(self):
        """ 
        >>> X={1,2};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T2()
        [[set(), {1}, {2}, {1, 2}]]
        
        >>> X={1,2,3};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T2()
        [[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]]
        
        """ 
        topologias=self.generar_todas_las_topologias()
        
        resultado=[]
        for topologia in topologias:
            self.ABIERTOS=topologia
            if self.es_un_espacio_T2():
                resultado.append(topologia)
        return resultado
    #
    def generar_espacios_T3(self):
        """ 
        >>> X={1,2};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T3()
        [[set(), {1}, {2}, {1, 2}]]
        
        >>> X={1,2,3};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T3()
        [[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]]
        """ 
        topologias=self.generar_todas_las_topologias()
        
        resultado=[]
        for topologia in topologias:
            self.ABIERTOS=topologia
            if self.es_un_espacio_T3():
                resultado.append(topologia)
        return resultado
    #
    def generar_espacios_T4(self):
        """ 
        >>> X={1,2};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T4()   
        [[set(), {1, 2}], [set(), {2}, {1, 2}], [set(), {1}, {1, 2}], [set(), {1}, {2}, {1, 2}]]
        """ 
        topologias=self.generar_todas_las_topologias()
        
        resultado=[]
        for topologia in topologias:
            if self.es_un_espacio_T4():
                resultado.append(topologia)
        return resultado
    #
    def generar_espacios_T5(self):
        """ 
        >>> X={1,2};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T5() 
        []
        >>> X={1,2,3,4};T=[];d={};Espacio_Topologico(X,T,d).generar_espacios_T5()  
        []
        
        """ 
        topologias=self.generar_todas_las_topologias()
        
        resultado=[]
        for topologia in topologias:
            if self.es_un_espacio_T5():
                resultado.append(topologia)
        return resultado
    #    
    def es_un_punto_de_acumulacion_de(self,x,S):
        """
        S:set
        
            Def 1:
            
            Sea ( X , τ ) un espacio topológico y S un subconjunto de X. 
            Diremos que x es un punto de acumulación de S si y solamente si 
            para cualquier subconjunto abierto U del espacio X que contenga al 
            punto x, se tiene que S ∩ ( U - { x } ) ≠ ∅ 
            
            Def 2:
            
            Un punto x  de  X es un punto de acumulación de A si todo entorno U de x cumple U ∩ (A - { x} ) ≠ ∅ .            
            
            Topologia.Carlos Ivorra.Pag 19
            
            Proposicion 2.20 Todo punto de acumulacion es un punto de adherencia
            
        >>> X={1,2,3};T=[set(),X];d={};A={1,2,3};Espacio_Topologico(X,T,d).es_un_punto_de_acumulacion_de(1,A)
        True
        
        >>> X={1,2,3,4,5};T=[set(),X,{1}, {1,2}, {1,2,3}, {1,2,3,4}];d={};A={2,3,4,5};Espacio_Topologico(X,T,d).es_un_punto_de_acumulacion_de(1,A)            
        False
        
        >>> X={1,2,3,4,5};T=[set(),X,{1}, {1,2}, {1,2,3}, {1,2,3,4}];d={};A={3,4,5};Espacio_Topologico(X,T,d).es_un_punto_de_acumulacion_de(1,A)            
        False
        
        >>> X={1,2,3,4,5};T=[set(),X,{1}, {1,2}, {1,2,3}, {1,2,3,4}];d={};A={3,4,5};Espacio_Topologico(X,T,d).es_un_punto_de_acumulacion_de(2,A)
        False
        
        >>> X={1,2,3,4,5};T=[set(),X,{1}, {2,3,4,5}];d={};A={2,3,4};Espacio_Topologico(X,T,d).es_un_punto_de_acumulacion_de(5,A)        
        True
        
        >>> X={1,2,3,4,5};T=[set(),X,{1}, {2,3,4,5}];d={};A={1,2,3};Espacio_Topologico(X,T,d).es_un_punto_de_acumulacion_de(4,A)        
        True

        >>> X={1,2,3,4,5};T=[set(),X,{1}, {2,3,4,5}];d={};A={1,2,3};Espacio_Topologico(X,T,d).es_un_punto_de_acumulacion_de(5,A)        
        True
        
        """
        for U in self.ABIERTOS:
            if x in U:                
                if S.intersection(U.difference({x}))==set([]):
                    #print(U)
                    return False
                
        return True                        
    #
    def es_un_punto_aislado(self,x,S):
        """
        S:set
        
        Def 1:
        
        Un punto x ∈ S ⊂ X es un punto aislado de S en (X, T) si existe 
        un entorno U de x tal que U ∩ S = {x}.
        
        Def 2:
        
        Un punto x de un espacio topológico X es aislado si {x} es abierto.
        
        Topologia. Carlos Ivorra. Pag 4
        
        
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};A={1,2};Espacio_Topologico(X,T,d).es_un_punto_aislado(1,A)
        True
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};A={1,2};Espacio_Topologico(X,T,d).es_un_punto_aislado(2,A)
        True
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{1,2}];d={};A={1,2};Espacio_Topologico(X,T,d).es_un_punto_aislado(1,A)        
        True
        
        >>> X={1,2,3,4,5};T=[set(),X,{1}, {1,2}, {1,2,3}, {1,2,3,4}];d={};A={1,4,5};Espacio_Topologico(X,T,d).es_un_punto_aislado(1,A)        
        True
        
        >>> X={1,2,3,4,5};T=[set(),X,{1}, {1,2}, {1,2,3}, {1,2,3,4}];d={};A={2,5};Espacio_Topologico(X,T,d).es_un_punto_aislado(2,A)        
        True
        """
        entornos_x=self.generar_sistema_entornos_punto(x)
        for entorno in entornos_x:
            if entorno.intersection(S)==set([x]):
                return True
            
        return False    
    #
    def puntos_aislados(self,S):
        """
        S:set
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d={};A={1,2};Espacio_Topologico(X,T,d).puntos_aislados(A)
        {1, 2}
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d={};A={1,2};Espacio_Topologico(X,T,d).puntos_aislados(A)
        {1, 2}
        >>> X={1,2,3};T=[set(),X,{1},{2},{1,2}];d={};A={1,2};Espacio_Topologico(X,T,d).puntos_aislados(A)        
        {1, 2}
        
        """
        resultado=set([])
        for x in S:
            if self.es_un_punto_aislado(x,S):
                resultado.add(x)
                
        return resultado                        
    #
    def es_un_punto_adherente(self,a,A):
        """ 
        A:set
        
        """ 
        entornos=self.generar_sistema_entornos_punto(a)
        for entorno in entornos:
            if entorno.intersection(A)==set():
                return False
        
        return True    
    #
    def es_un_punto_limite(self,a,A):
        """ 
        A:set
        
        """
        return  self.es_un_punto_adherente(a,A)
    #    
    def es_perfecto(self,A):
        """
            A:set
        
            >>> X={1,2,3};T=Conjunto().potencia(X);d={};A=set();Espacio_Topologico(X,T,d).es_perfecto(A) 
            True

            >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};A=set();Espacio_Topologico(X,T,d).es_perfecto(A) 
            True
                    
            >>> X={1,2,3};T=[set(),X];d={};A=set();Espacio_Topologico(X,T,d).es_perfecto(A) 
            True

            >>> X={1,2,3};T=[set(),X];d={};A={1,2};Espacio_Topologico(X,T,d).es_perfecto(A) 
            False
            
            >>> X={1,2,3,4};T=[set(),X,{1},{1,2},{1,3},{1,4},{1,2,3},{1,2,4},{1,3,4}];d={};A={2,3,4};Espacio_Topologico(X,T,d).es_perfecto(A) 
            False

            >>> X={1,2,3,4};T=[set(),X,{1},{1,2}];d={};A={2,3,4};Espacio_Topologico(X,T,d).es_perfecto(A) 
            False
            
            >>> X={1,2,3,4};T=[set(),X,{1},{1,2}];d={};A={2,3,4};Espacio_Topologico(X,T,d).es_perfecto(A) 
            False
            
            >>> X={1,2,3};T=[set(),X,{1},{1,2},{1,2,3}];d={};A={2,3};Espacio_Topologico(X,T,d).es_perfecto(A) 
            False
            
        """
        def criterio1(A):
            """
            un conjunto perfecto es un conjunto que coincide con su conjunto derivado
            """     
        
            return A==self.derivado(A)
        
        def criterio2(A):
            """
            Un conjunto perfecto es un conjunto cerrado sin puntos aislados
            """     
            if self.es_cerrado(A):
                if self.puntos_aislados(A)==set():
                    return True
                
            return False    

        def criterio3(A):
            """
            A es cerrado y A es la cerradura de su interior
            """     
            if self.es_cerrado(A):
                if A==self.clausura(self.interior(A)):
                    return True
                
            return False    
        
            
        return criterio1(A)
    #
    def aislados(self,A):
        """
        A:set
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};A={1,2,3};Espacio_Topologico(X,T,d).aislados(A)
        {1, 2, 3}

        >>> X={1,2,3};T=Conjunto().potencia(X);d={};A={2,3};Espacio_Topologico(X,T,d).aislados(A)
        {2, 3}
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d={};A={1,2};Espacio_Topologico(X,T,d).aislados(A)
        {1, 2}
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{1,2}];d={};A={1,2};Espacio_Topologico(X,T,d).puntos_aislados(A)        
        {1, 2}
        
        """
        
        
        resultado=set()
        for a in A:
            if self.es_un_punto_aislado(a,A):
                resultado.add(a)
        
        return resultado
    #
    def cerrados(self):
        """
        """ 
        resultado=[]
        for abierto in self.ABIERTOS:
            resultado.append(self.X.difference(abierto))
        
        return resultado
    #
    def abiertos_cerrados(self):
        """ 
        """
        cerrados=self.cerrados()
        resultado=[]
        for abierto in self.ABIERTOS:
            if abierto in cerrados:
                resultado.append(abierto)
                
        return resultado        
    #
    def derivado(self,A):
        """
        A:set
        
        El conjunto de todos los puntos de acumulación de A se llama conjunto derivado de A
        
        >>> X={1,2,3};T=[set(),X];d={};A={1,2,3};Espacio_Topologico(X,T,d).derivado(A)
        {1, 2, 3}
        
        >>> X={1,2,3,4};T=[set(),X,{1},{1,2},{1,2,3}];d={};A={1,2,3};Espacio_Topologico(X,T,d).derivado(A)
        {2, 3, 4}
        
        >>> X={1,2,3,4,5};T=[set(),X,{1},{1,2},{1,3,4}];d={};A={3,5};Espacio_Topologico(X,T,d).derivado(A)
        {4, 5}
        
        >>> X={1,2,3,4,5};T=[set(),X,{1},{1,2},{1,3,4}];d={};A={2};Espacio_Topologico(X,T,d).derivado(A)
        {5}
        
        >>> X={1,2,3,4};T=[set(),X,{1},{1,2},{1,2,3}];d={};A={1,2,3};Espacio_Topologico(X,T,d).derivado(A) 
        {2, 3, 4}
        
        """
        resultado=set()
        for a in self.X:
            if self.es_un_punto_de_acumulacion_de(a,A):
                resultado.add(a)
                
        return resultado                    
    #
    def frontera(self,A):
        """ 
        A:set
        
        Si X es un espacio topológico y A incluido en  X, se define la frontera de A como el conjunto
        
        Frontera(A) = clausura(A) interseccion clausura(X - A)        
        
        Topologia. Carlos Ivorra. Pag 18
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).frontera({1})
        {2, 3}
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).frontera({2})
        {2, 3}

        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).frontera({3})
        {3}

        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).frontera({1,2})
        {3}
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).frontera({2,3})
        {2, 3}
        
        Fr(A)=X-(Interior(A) u Exterior(A))
        """
        complemento_A=self.X.difference(A)
        
        return self.clausura(A).intersection(self.clausura(complemento_A))
    #
    def borde(self,A):
        """ 
        A:set
                
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).borde({2,3})  
        {2, 3}
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).borde({2,3})                
        set()
        
        >>> X={1,2,3};T=[set(),X];d={};Espacio_Topologico(X,T,d).borde({1,2})           
        {1, 2, 3}
        
        >>> X={1,2,3};T=[set(),X, {3}, {1, 2}];d={};Espacio_Topologico(X,T,d).borde({1,2})
        set()

        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).borde({1,2})
        {3}
        
        """
        def criterio1(A):
            """ 
             El borde de A es el conjunto de todos los puntos frontera de A
            """
            return self.frontera(A)
        
        def criterio2(A):
            """ 
             El borde de un conjunto A es la diferencia entre su clausura y su interior             
            """
            return self.clausura(A).difference(self.interior(A))
        

        def criterio3(A):
            """ 
             El borde de A es el conjunto de puntos x tales que x pertenece a la adherencia de A y 
             x pertenece a la adherencia del complemento de A           
            """
            return self.adherencia(A).intersection(self.adherencia(self.X.difference(A)))
        

        
        return criterio1(A)
    #
    def clausura(self,A):
        """
        A:set
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).clausura({1})
        {1, 2, 3}
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).clausura({2})
        {2, 3}
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).clausura({3})
        {3}
        
        
        """     
        resultado=set([])   
        for x in self.X:
            entornos_x=self.generar_sistema_entornos_punto(x)
            es_punto_de_clausura=True
            for entorno in entornos_x:
                if A.intersection(entorno)==set([]):
                    es_punto_de_clausura=False
                    break
                
            if es_punto_de_clausura:
                resultado.add(x)
                                                                    
        return resultado    
    #
    def clausura2(self,A):
        """ 
        A:set
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).clausura2({1})
        {1, 2, 3}
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).clausura2({2})
        {2, 3}
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).clausura2({3})
        {3}
        
        """        
        cerrados=self.cerrados()
        
        resultado=set()
        for cerrado in cerrados:
            if A.issubset(cerrado):
                if resultado==set():
                    resultado=cerrado
                else:    
                    resultado=resultado.intersection(cerrado)
                
        return resultado        
    # 
    def adherencia(self,A):
        """ 
        A:set
        
        """
        return self.interior(A).union(self.frontera(A))    
    #
    def exterior(self,A):
        """
        A:set
        
        """
        return self.interior(self.X.difference(A))
    #
    def interior(self,A):  
        """
        A:set
        
        
        Interior de A es la unión de todos los abiertos contenidos en A
        
        >>> X={1,2,3,4,5};T=[set([]),{1},{3,4},{1,3,4},{2,3,4,5}];d={};A={2,3,4};Espacio_Topologico(X,T,d).interior(A)
        {3, 4}
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).interior({1})
        {1}
        
        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).interior({2})
        set()

        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};Espacio_Topologico(X,T,d).interior({1,2})
        {1, 2}
        
        """  
        
        resultado=set([])
        for abierto in self.ABIERTOS:
            if abierto.issubset(A):                
                resultado=resultado.union(abierto)
                        
        return resultado
    #
    def es_interior(self,a,A):
        """        
        A:set
        
        >>> X={1,2,3,4,5};T=[set([]),{1},{3,4},{1,3,4},{2,3,4,5}];d={};A={2,3,4};Espacio_Topologico(X,T,d).es_interior(3,A)
        True

        >>> X={1,2,3,4,5};T=[set([]),{1},{3,4},{1,3,4},{2,3,4,5}];d={};A={2,3,4};Espacio_Topologico(X,T,d).es_interior(4,A)
        True
        
        """
        
        for abierto in self.ABIERTOS:
            if abierto.issubset(A):
                if a in abierto: 
                    return True 
            
        return False 
    #
    def es_conexo(self,M):
        """ 
        M es conexo si no existen dos abiertos U, V disjuntos no vacios 
        tales que M = U ∪ V
        
        >>> X = {1, 2, 3};T=[set(), {1}, {1,2}, {1,2,3}];d={};M={2,3};Espacio_Topologico(X,T,d).es_conexo(M)
        True
        
        """
        for U in self.ABIERTOS:
            for V in self.ABIERTOS:
                if not U ==set([]) and not V ==set([]):
                    if U.intersection(V)==set([]):
                        if U.union(V)==M:                            
                            return False
                        
        return True                            
    #
    def es_denso(self,A):
        """
        A:set
        
        Un subconjunto D de un espacio topológico X es denso en X si clausura(D) = X.
        Topologia. Carlos Ivorra. Pag 16
        
        >>> X={1,2,3};T=[set(),{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}];d={}; D={1,2,3};Espacio_Topologico(X,T,d).es_denso(D)
        True
                        
        >>> X={1,2,3};T=[set(),{1,2},{1,3},{2,3},{1,2,3}];d={}; D={1};Espacio_Topologico(X,T,d).es_denso(D)
        True
                        
        >>> X={1,2,3};T=[set(),X];d={}; D={1};Espacio_Topologico(X,T,d).es_denso(D)
        True
        
        >>> X={1,2,3};T=[set(),X,{1},{2},{1,2}];d={}; D={1};Espacio_Topologico(X,T,d).es_denso(D)
        False
        
        >>> X={1,2,3};T=[set(),X,{1,2},{2,3}];d={}; D={2};Espacio_Topologico(X,T,d).es_denso(D)
        True
        
        """
        return self.adherencia(A)==self.X
    #
    def es_continua(self,f,X1,T1,X2,T2):
        """ Pendiente
        f: X1 -> X2
        (X1,T1) espacio topologico
        (X2,T2) espacio topologico
        
        
        Caso 1:
        
            X={2,3} con la topología τX​={∅,{2},{2,3}} y 
            Y={1,2} con τY​={∅,{1},{1,2}}.

            Definimos una función f:X→Y como:
            
            f(2)=1
            f(3)=2.
                        
            f es continua
        """
        pass
    #
    def bola_abierta(self,a,r):
        """
        """
        resultado=[a]
        
        for x in  self.X:
            if self.d.get((a,x))<r:
                resultado.append(x)
            
        return resultado
    #
    def bola_cerrada(self,a,r):
        """
        """
        resultado=[a]
        
        for x in  self.X:
            if self.d.get((a,x))<=r:
                resultado.append(x)
            
        return resultado
    #
    def es_un_recubrimiento(self,Familia,X):
        """ 
        Familia:[set1, set2 , ...]
        X:set
        
        >>> F=[{1, 2, 3}, {1, 4}, {2, 3}, {1, 5}];X={1, 2, 3, 4, 5};Espacio_Topologico([],[],{}).es_un_recubrimiento(F,X)
        True
        
        >>> F=[{1, 3}, {1, 4}, {2, 3}, {1, 5}];X={1,  3, 4, 5};Espacio_Topologico([],[],{}).es_un_recubrimiento(F,X)
        True
        
        >>> F=[{1, 3}, {1, 4}, {2, 3}, {1, 5}];X={1,  3, 4, 6};Espacio_Topologico([],[],{}).es_un_recubrimiento(F,X)
        False
        """
        resultado=set()
        for C in Familia:
            resultado=resultado.union(C)
            
        return X.issubset(resultado)    
    #    
    def es_un_filtro(self,Familia,X):
        """ 
        Familia:[set1, set2 , ...]
        X:set
        
         Si A, B ∈ Familia , entonces A ∩ B ∈ Familia .
         Si A ∈ Familia y A ⊆ B, entonces B ∈ Familia
         
          >>> F=[{1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 5}, {1, 2, 3, 4, 5}];X={1, 2, 3, 4, 5};Espacio_Topologico([],[],{}).es_un_filtro(F,X)
          True
        """
        #
        for A in Familia:
            if not A.issubset(X):
                return False
        #    
        for A in Familia:
            for B in Familia:    
                if not A.intersection(B) in Familia:
                    return False
        #        
        partes_X=Conjunto().potencia(X)
        for A in Familia:
            for B in partes_X:        
                if A.issubset(B):
                    if not B in Familia:
                        return False
        #
        return True                            
    #
    def es_un_ultrafiltro(self,Familia,X):
        """ 
        Familia:[set1, set2 , ...]
        X:set
                
        Es un filtro y si un conjunto A no está en F, entonces su complemento X \ A sí está en F
        
        >>> F=[{1}, {1, 2}, {1, 3}, {1, 2, 3}];X={1, 2, 3};Espacio_Topologico([],[],{}).es_un_ultrafiltro(F,X)
        True

        """
        partes_X=Conjunto().potencia(X)
        
                    
        if self.es_un_filtro(Familia,X):
            for parte in partes_X:
                if not parte in Familia:
                    
                    if not  X.difference(parte) in Familia:
                        return False
                                    
        return True        
    #
    def generar_separaciones(self):
        """ 
        X= A u B 
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).generar_separaciones()
        [[{1}, {2, 3}], [{2}, {1, 3}], [{1, 2}, {3}]]
         
        >>> X={1,2,3};T=[set(),X,{2}, {3}, {2,3}];d={};Espacio_Topologico(X,T,d).generar_separaciones()
        []
        """
        
        if not self.es_un_espacio_topologico():
            return []
        
        separaciones=[]
        for A in self.ABIERTOS:
            for B in self.ABIERTOS:
                if not A==set() and not B==set():
                    if A.intersection(B)==set():
                        if self.X==A.union(B):
                            if not [A,B] in separaciones and not [B,A] in separaciones:
                                separaciones.append([A,B])
        return separaciones                    
    #
    def es_una_componente_conexa(self,C):
        """ 
        C:set
        
        Proposicion 3.3.12. Las componentes conexas de un espacio topologico finito son abiertas.        
        
        >>> X={1,2,3,4};T=[set(),X];d={};C=X;Espacio_Topologico(X,T,d).es_una_componente_conexa(C)        
        True
        
        >>> X={1,2,3,4};T=[set(),X,{2,3,4}];d={};C=X;Espacio_Topologico(X,T,d).es_una_componente_conexa(C)        
        True

        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};C={1};Espacio_Topologico(X,T,d).es_una_componente_conexa(C)        
        True
        
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};C={2};Espacio_Topologico(X,T,d).es_una_componente_conexa(C)        
        True

        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};C={3};Espacio_Topologico(X,T,d).es_una_componente_conexa(C)        
        True
                
        """
        #
        def criterio1(C):
            """ 
            """ 
            if self.es_conexo(C):                
                if C in self.ABIERTOS:                    
                    cerrados=self.cerrados()
                    if C in cerrados:                        
                        return True  
                              
            return False
        #
        def criterio2(C):
            """ 
            """ 
            
            partes_de_X=Conjunto().potencia(self.X)
            
            partes_conexas=[]
            for parte in partes_de_X:
                if self.es_conexo(parte):                
                    partes_conexas.append(parte)
                    
            resultado=[]        
            for parte_conexa1 in partes_conexas:                
                encontrado_super=False
                for parte_conexa2 in partes_conexas:
                    if not parte_conexa1==parte_conexa2:                        
                        if parte_conexa1.issubset(parte_conexa2):
                            encontrado_super=True
                            
                if not encontrado_super:
                    resultado.append(parte_conexa1)                

            return C in resultado
        
        
        if not self.es_un_espacio_topologico():
            
            return False
        
                
        return criterio1(C)       
    #
    def es_una_componente_conexa_de(self,x):
        """ 
        Se llama componente conexa de x la union de todos los subconjuntos conexos de X que contienen a x.
        """
        subconjuntos_X=Conjunto().potencia(self.X)
        subconjuntos_X_que_tienen_a_x=[A for A in subconjuntos_X if x in A]
        resultado=[]
        for A in subconjuntos_X_que_tienen_a_x:
            if self.es_denso(A):
                resultado.append(A)
        
        return resultado
    #
    def estan_separados(self,A,B):
        """ 
        A:set
        B:set
        
        Dos conjuntos A y B en un espacio topológico (X,τ) se llaman separados 
        si no tienen puntos de adherencia en común
        
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={}; A={1};B={2,3};Espacio_Topologico(X,T,d).estan_separados(A,B)        
        True
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={}; A={2};B={1,3};Espacio_Topologico(X,T,d).estan_separados(A,B)                
        True
        
        >>> X={1,2,3}; T=[set(),X,{2}, {3}, {2,3}];d={}; A={2};B={3};Espacio_Topologico(X,T,d).estan_separados(A,B)                        
        True
        
        """
        return self.adherencia(A).intersection(B)==set() and self.adherencia(B).intersection(A)==set() 
    #
    def estan_completamente_separados(self,A,B):
        """     
        A:set
        B:set
           
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={}; A={1};B={2};Espacio_Topologico(X,T,d).estan_separados(A,B)        
        True
        
        >>> X={1,2,3}; T=[set(),X,{1},{2},{3},{1,2},{1,3},{2,3}];d={}; A={1};B={3};Espacio_Topologico(X,T,d).estan_separados(A,B)        
        True
        

        """
        #
        def criterio1():
            
            """ 
            En espacios finitos los conjuntos completamente separados son aquellos que son tanto abiertos 
            como cerrados (clopen) y disjuntos entre sí            
            """
            cerrados=self.cerrados()
            
            if A in self.ABIERTOS and A in cerrados:
                if B in self.ABIERTOS and B in cerrados:
                    if A.intersection(B)==set():
                        return True
                    
            return False
        # 
        if not self.es_un_espacio_topologico():
            return False
        
        return criterio1()

    def es_diseminado(self,M):
        """ 
        M:set
        
        
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};M=set();Espacio_Topologico(X,T,d).es_diseminado(M) 
        True
        
        >>> X={1,2,3};T=Conjunto().potencia(X);d={};M={1,2};Espacio_Topologico(X,T,d).es_diseminado(M) 
        False
        
        >>> X={1,2,3};T=[set(),X,{1}, {1,2}, {1,2,3}];d={};M={4};Espacio_Topologico(X,T,d).es_diseminado(M)         
        True
        
        
        >>> X={1,2,3,4};T=[set(),X, {1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}];d={};M={1,2};Espacio_Topologico(X,T,d).es_diseminado(M) 
        False
        
        >>> X={1,2,3};T=[set(),X];d={};M={1,3};Espacio_Topologico(X,T,d).es_diseminado(M)
        False
        
        >>> X={1,2,3};T=[set(),X,{1}, {1,2}];d={};M={3,4};Espacio_Topologico(X,T,d).es_diseminado(M) 
        True

        >>> X={1,2,3,4};T=[set(),X,{1},{1,2},{1,3},{1,4},{1,2,3},{1,2,4},{1,3,4}];d={};M={2};Espacio_Topologico(X,T,d).es_diseminado(M) 
        True

        >>> X={1,2,3,4};T=[set(),X,{1},{1,2},{1,3},{1,4},{1,2,3},{1,2,4},{1,3,4}];d={};M={3};Espacio_Topologico(X,T,d).es_diseminado(M) 
        True

        >>> X={1,2,3};T=[set(),X,{1},{1,2}];d={};M={2};Espacio_Topologico(X,T,d).es_diseminado(M) 
        True

        >>> X={1,2,3,4};T=[set(),X,{1},{1,2}];d={};M={2,3};Espacio_Topologico(X,T,d).es_diseminado(M) 
        True
        
        """
        #
        def criterio1(M):
            """ 
            Un subconjunto A de un espacio topológico X se dice diseminado en X si el interior 
            de su clausura es vacío
            
            Topologia Carlos Ivorra Pag 37 Definición 1.61
            """
            return self.interior(self.clausura(M))==set()    
        
        def criterio2(M):
            """ 
                Un conjunto es diseminado si su complemento es denso en el espacio topológico
            """
            return self.es_denso(self.X.difference(M))
        
        def criterio3(M):
            """ 
                Un conjunto es diseminado si su interior es vacío
            """            
            return self.interior(M)==set()
        
        def criterio4(M):
            """ 
                Un conjunto es diseminado si no contiene ningún conjunto abierto no vacío de la topología dada
            """
            for abierto in self.ABIERTOS:
                if not abierto==set():
                    if abierto.issubset(M):
                        return False                    
            return True
        
        def criterio5(M):
            """ 
                Un conjunto es diseminado si su complemento es denso en el espacio topológico
            """
            return  self.es_denso(self.X.difference(M))
        # 
        if not self.es_un_espacio_topologico():
            return False
        
        return criterio1(M)
    #
    def diseminados(self):
        """ 
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).diseminados()
        [set()]
        >>> X={1,2,3};T=[set(),X,{1}, {1,2}, {1,2,3}];d={};Espacio_Topologico(X,T,d).diseminados() 
        [set(), {2}, {3}, {2, 3}]
        """
        p_x=Conjunto().potencia(self.X)
        resultado=[]
        for p in p_x:
            if self.es_diseminado(p):
                resultado.append(p)
                
        return resultado
    #    
    def es_denso_en_ninguna_parte(self,M):
        """ 
        M:set
        
                
        """
        return self.es_diseminado(M)
    #
    def es_nunca_denso(self,M):
        """ 
        M:set
        """
        return self.es_denso_en_ninguna_parte(M)
    #
    def es_de_primera_categoria(self,M):        
        """ 
        M:set
        
        Un subconjunto M de un espacio topologico (X, T ) como de primera categoria en (X, T ) si es 
        union numerable de conjuntos diseminados.
        
        >>> X={1,2,3,4};T=[set(),X,{1}, {1,2}, {1,2,3}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({1})
        (False, False, False, False, False)
        
        >>> X={1,2,3};T=[set(),X,{1}, {1,2}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({2})
        True
        
        Nuevos casos 
        
        >>> X={1,2,3,4};T=[set(),X,{1},{2,3,4}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria(set())
        (True, True, True, True, True)
        >>> X={1,2,3,4};T=[set(),X,{1},{2,3,4}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({1})
        (False, False, False, False, False)
        >>> X={1,2,3,4};T=[set(),X,{2,3,4},{1,4},{4}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({1})
        
        >>> X={1,2,3,4};T=[set(),X,{1}, {1,2}, {1,2,3}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({4})
        
        >>> X={1,2,3,4};T=[set(),X,{1,2}, {3,4}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({1,3})
        
        >>> X={1,2,3,4};T=[set(),X,{1}, {2}, {1,2}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({3,4})
        
        >>> X={1,2,3,4};T=[set(),X,{1}, {2,3,4}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({2,3})
        
        >>> X={1,2,3,4};T=[set(),X,{1,2,3}, {4}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({4})
        (False, False, False, False, False)
        >>> X={1,2,3,4};T=Conjunto().potencia(X);d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({1})
        (False, False, False, False, False)
        >>> X={1,2,3,4};T=[set(),X,{1}, {1,2}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({2,3,4})
        
        >>> X={1,2,3,4};T=[set(),X,{1,2}, {3,4}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({1,3})
        
        >>> X={1,2,3,4};T=[set(),X,{1}, {1,2,3}];d={};Espacio_Topologico(X,T,d).es_de_primera_categoria({2,4})
        """
        def criterio1(M):
            """ 
            Un subconjunto M de un espacio topologico (X, T ) como de primera categoria en (X, T ) si es 
            union numerable de conjuntos diseminados.

            """ 
            candidatos=Conjunto().potencia(self.X)
            diseminados=[]        
            for candidato in candidatos:
                if self.es_diseminado(candidato):
                    diseminados.append(candidato)
                    
            for i in range(2**len(diseminados)):
                elementos_elegidos=Conjunto().decimal_base_dos(i)
                elementos_elegidos=[0]*(len(diseminados)-len(elementos_elegidos))+elementos_elegidos            
                aux=set()
                for j in elementos_elegidos:
                    if  elementos_elegidos[j]==1:
                        aux=aux.union(diseminados[j])
                        
                if aux==M:
                    return True        
                
                return False
        #            
        def criterio2(M):
            """ 
            Un conjunto M es de primera categoría si su complemento es denso en el espacio topológico.
            """
            return self.es_denso(self.X.difference(M))
        #
        def criterio3(M):
            if self.es_cerrado(M):
                return self.interior(M)==set()
            
            return False
        #
        def criterio4(M):
            """ 
            Un conjunto M es de primera categoría si su clausura tiene interior vacío.
            """
            
            return self.interior(self.clausura(M))==set()
        #
        def criterio5(M):            
            """ 
            M no contiene ningún conjunto abierto no vacío,
            """
            for abierto in self.ABIERTOS:
                if not abierto==set():
                    if abierto.issubset(M):
                        return False
            return True        
        #        
        if not self.es_un_espacio_topologico():
            print("no es_un_espacio_topologico")
            return False
        

                    
        return criterio1(M),criterio2(M),criterio3(M),criterio4(M),criterio5(M)
    #
    def es_magro(self,M):
        """
        M:set
        """
        return self.es_de_primera_categoria(M)
    #
    def es_de_segunda_categoria(self,M):
        """
        M:set
        """
        
        return not self.es_de_primera_categoria(M)
    #
    def es_residual(self,M):
        """
        M:set
        """
        
        return self.es_de_primera_categoria(self.X.difference(M))
    #
    def es_un_abierto_regular(self,M):
        return M==self.interior(self.clausura(M))
    #

"""            
" ".startswith
X={1,2,3,4};T=[set(),X,{1}, {1,2}, {1,2,3}];d={};et=Espacio_Topologico(X,T,d)
l=dir(et)
metodos=[x for x in l if  not x.startswith("_")]
for m in metodos:
    print(m)

""" 
if __name__ == "__main__":
    for i in range(5):
        print("\n")

    print("--------------------------------------------")

    resultados_pruebas=doctest.testmod()
        
    if resultados_pruebas.failed==0 :        
        print("No se han encontrado errores en las %d pruebas " % (resultados_pruebas.attempted))

    print("--------------------------------------------")    
