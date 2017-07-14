import time,random

starttime= time.time()


turn=['X','O']
playerturn,compturn=turn

print '\n'
print '''........WELCOME TO TIC-TAC-TOE GAME.......
         
         CHOOSE UR MOVE FROM THESE OPTIONS ONLY

         'top-L'  'top-M' 'top-R'  
         'mid-L'  'mid-M' 'mid-R' 
         'low-L'  'low-M' 'low-R'   

'''
print 'TO EXIT THE GAME press CTRL-C'
print '\n'

choice=raw_input("PLEASE ENTER YOUR CHOICE : X or O \n ")


if choice=='O':
	turn=['O','X']

theBoard={
          'top-L':' ','top-M':' ','top-R':' ',
          'mid-L':' ','mid-M':' ','mid-R':' ',
          'low-L':' ','low-M':' ','low-R':' ',
          }
def printboard(theBoard):
 	print '         ' + theBoard['top-L'] +' | '+theBoard['top-M'] +' | '+theBoard['top-R']
 	print '         '+'--+---+--'
 	print '         '+theBoard['mid-L'] +' | '+theBoard['mid-M'] +' | '+theBoard['mid-R']
 	print '         '+'--+---+--'
 	print '         '+theBoard['low-L'] +' | '+theBoard['low-M'] +' | '+theBoard['low-R']
 	print '         '+'\n'


def check(theBoard,yturn):
		if(theBoard['top-L']==theBoard['top-M']==theBoard['top-R']==yturn):
			return True
		elif(theBoard['mid-L']==theBoard['mid-M']==theBoard['mid-R']==yturn):
			return True
		elif(theBoard['low-L']==theBoard['low-M'] ==theBoard['low-R']==yturn):
			return True
		elif(theBoard['top-L']==theBoard['mid-L'] ==theBoard['low-L'] ==yturn):
			return True
		elif(theBoard['top-M']==theBoard['mid-M'] ==theBoard['low-M'] ==yturn):
			return True
		elif(theBoard['top-R']==theBoard['mid-R'] ==theBoard['low-R'] ==yturn):
			return True
		elif(theBoard['top-L']==theBoard['mid-M']==theBoard['low-R'] ==yturn):
			return True
		elif(theBoard['top-R']==theBoard['mid-M']==theBoard['low-L'] ==yturn):
			return True

def whichmove(theBoard,compturn,playerturn):
	dupli={}
	move1=[]
	dupli=theBoard.copy()
	
	
	for keys in dupli:
		if dupli[keys]==' ':
			move1.append(keys)
	
	
    
	for x in move1:
        
		
		dupli[x]=compturn
		

		if check(dupli,compturn):
			return x
		dupli[x]=' '
		

	for x in move1:
        
		


		dupli[x]=playerturn
		
		if check(dupli,playerturn):
			return x

		dupli[x]=' '
		
	x1=['top-L' , 'top-R ', 'low-R' , 'low-L']
	x2=['top-M' , 'mid-L' , 'mid-R' , 'low-M']

	for r in x1:
		if r in move1:
			return r 
	if 'mid-M'  in move1:
		return 'mid-M'
	for r in x2:
		if r in move1:
			return r 
			
i=0
print '\n'
print "PLAYER = %s"%turn[0]
print "COMPUTER = %s"%turn[1]
print '\n'

def game(theBoard,turn,playerturn,compturn):

	j=random.randint(0,1)
	if(j==0):
		print "....PLAYER GOES FIRST...."
	else:
		print "....COMPUTER GOES FIRST...."
	for i in xrange(9):
		
		
		printboard(theBoard)
		print 'TURN FOR '+turn[j]+'\n' ' MOVE ON WHICH SPACE?'
		if j==0:
			move=raw_input()
			print '\n'
		elif j==1:
			move=whichmove(theBoard,turn[1],turn[0])
			print '\n'

		while move not in theBoard:
			print '''....NOT A VALID INPUT
			PLEASE ENTER A VALID POSITION.....
			      '''
			move=raw_input()
			print '\n'

		while theBoard[move]!=(' ') :
			print '''....POSITION ALREADY OCCUPIED
			KINDLY CHOOSE ANOTHER POSITION .....
			            
			      '''
			move=raw_input()
			print '\n'
			if move not in theBoard:
				print '''....NOT A VALID INPUT
				PLEASE ENTER A VALID POSITION.....
				      '''
				move=raw_input()
				print '\n'

				
			
		theBoard[move]=turn[j]

		if check(theBoard,turn[j]):
			if turn[j]==choice:
				print '   '+"HURRAY!!! YOU WIN...."
				break
			else:
				print '   '+"...COMPUTER WINS..."
				break


			

		if j==1:
			j=0
		else :
			j=1

	

game(theBoard,turn,playerturn,compturn)

printboard(theBoard)
endtime= time.time()
if (' ') not in theBoard.values():
	print "THE MATCH IS A DRAW"

print '\n\n\n'
print 'THE GAME FINISHED IN ',endtime-starttime,'SECONDS '






    
	

	



	
				
				


				
				
    




	
	









	

	
	

