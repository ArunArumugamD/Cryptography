import random


class DHKeyExchange:
	p=None
	g=None
	def __init__(self,secret):
		self.key=None
		self._secret=secret
	
	@staticmethod
	def is_prime(num):
		for i in range(2,num):
			if num%i==0:
				return False
		return True


	@classmethod
	def get_prime(cls):
		while(not cls.p):
			choice = random.randrange(1000,10000)
			if cls.is_prime(choice):
				cls.p=choice

		return cls.p
	
	@classmethod
	def is_generator(cls,g):
		for i in range(1,cls.p-1):
			if (g**i)%cls.p==1:
				return False
		return True
	@classmethod
	def get_generator(cls):
		for g in range(2,cls.p):
			if cls.is_generator(g):
				cls.g=g
				break
		
	def gen_key(self):
		self.key= (DHKeyExchange.g**self._secret) % DHKeyExchange.p
	
	def get_key(self,shared):
		return (shared**self._secret)%DHKeyExchange.p
		
	
DHKeyExchange.get_prime()
print('PRIME :',DHKeyExchange.p)
DHKeyExchange.get_generator()
print('GENERATOR :',DHKeyExchange.g)


alice =DHKeyExchange(10)
a_k=alice.gen_key()


bob=DHKeyExchange(5)
b_k=bob.gen_key()


print(f'alice : {alice.key}  bob:{bob.key}')

print("alice's derived key :",alice.get_key(bob.key))
print("bob's derived key :",bob.get_key(alice.key))


