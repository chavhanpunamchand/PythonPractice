# MAKE INSTALLATIONS- ->
# TRY OUT --> THESE THINGS-->

#PROGRAM -->    ELEMENTS -->


#variable --> variable=value
#function --> at module  def name():-->
#class --> class classname
#methods --> class in which function
#innerfunction --> either inside function or inside method-->
#indent --> ideally 4 spaces-->


class CollegeInfo:
    pass


class StudentInfo:
    pass


# constant --> variable --> whose value will be changed --> all capital + seperate it by underscore

PI_VALUE = 3.14 # ALL CAPS + SEPERATE IT BY UNDERSCORE
class ProductInfo:      # classname --> start with capital + camelcase
    productName = "Mobile"     #variablename --> start with small + camelcase
    productPrice = 1292.34         #variablename --> start with small + camelcase
    productQty = 12        #variablename --> start with small + camelcase
    def display_product_information(self):  # method --> all small letters + seperated by underscores
        pass

#CORE READIBILITY --> MAINTAINANCE EASY -- UNIVERSALLY

#all small -->  new word --> underscore
def calculation():
    pass

def smart_calculate():
    pass

def new_calculation():
    pass


#class=10

class Emp:
    x = 10      # variable
    def m1(self):   # method
        print('inside m1')
    y = 20              # variable

    def m2(self):   #method
        print('inside m2')

    def m3(self):   #method
        print('inside m3')

        def x():    # 1 --> inside method-->
            print('inside x')

    def xx(self):   #methods
        def yy():   # inner function
            def zz():   #inner function
                pass

firstName = "Yogesh"    # this one is correct   # whenver new word comes up--> first letter capital
firstname = "Yogesh"    #not accepted ==> --> IT industry

collegeName = "AAA"


name ="ABC"
age = 20
ONE = 20
def one():  #function               --> method/function --> function --> inner function
    print('inside one')


#indentifiers --> to whome to identify --> class/variable/functions/innerfunctins/methods -->

#python --> indefiers rules--> name ??  --> grammer--> python -->   --> not allowed
        # make sure every idenfieriers =-->   A-Z,a-z,0-9,_       --> only allowed
        # shud not start with digit
        # case sensitive
        # special keywords cannot be used --> reserved words
    #recommandations -->
            #variable --> name -->  start with small letter + camelcase
            #methods/function/innerfunction-->  name -> start with small + seperate it by underscore
            #class ---> always start with capital letter + camelcase




'''


f1(){

				as
	33
					233
}


indent --> 1 indent --> 4 spaces

def f1:
	dsd
	12		
	33
	12		34
44	--> functionbodyends here
	22878

Software
	open source	-->  software + softwarecode--> freely available --> so that in case u want--> code modify as per ur requirement
	freeware	--> only software is freely available --> but not code--> u cannot modify--> we can only use the software
	copyright	--> first u need to accept terms and condition--> we can bt as per condition specified by owner/dev
	licensed	--> software or code ->not available freely -- we need pay first then we can 
					avail only software bt not code.
	trailversion --> free for few days-- maybe for week/month/quarter/year--> 
	
	
	
	

python is  --> dynamically type	-- type and memory--
			   open source --> freely available --> we can custmize as per requirements
			   
			   
datatypes --> basics
		number --> 		number --> int		float		complex
		string			''		""			'''	'''			"""		"""	
		boolean			True/False
		Absence			None
		
Variable--> specific memory in programming context--> on which our value is stored-->
			what type of data/value is nothing but--> datatype..
			
			
			
			
			
python --> Case sensitive lang-->
			
variables --> momory location
datatype --> type of data or values
methods/functions --> multiple lines code/instruction--> reuse	--> def keyword
class 	--> class keyword
files
modules
	
	
	dt  variable assignemnt value
	int num = 10
	dt variable assignemnt value
	byte num = 20
	String name = "ABC"
	
	---------->
	int num = 10
	<-----------
	
	= right to left--> num

	python in a dynamically type in --> type context + memory context
										type-- value infer
										memory  --> value vrn
				open source lang --> any can download -- freely available
	
	
	
	statically typed ->					dynamic- ->
	
statically typed-->			based on datatype --> we can store the value--> in future we are allowed to change the type
			int num = 10;
			num ------------> memory location --> this memory location reserved only for int
			num = "A" --> error--> 
			
			
		dynamically type --> first u place the value on memory --> based on value--> type of the variable
																	will be inferred
			based on value --> type will be inferred 
			num = 10	--> initially --> int
			num = "A"	--> string
			num = 102.34 --> float
			
			
			
											c++				java 
			int num  = 10		--> int-->  2 bytes			4 bytes
											16 bit			32 bit
									sb	64	32	16	8	4	2	1
						1 byte ---> 0	0	0	0	0	0	0	0
									
							
						num = 15	0	0	0	0	1	1	1	1
						num = 20	0	0	0	1	0	1	0	0
									0	1	1	1	1	1	1	1 --> 127 --> 127
									1	1	1	1	1	1	1	1 --> 128
					
						-ve -->+1
														range
						1 byte --> 8 bit ---> 		-2^7 to (2^7)-1	  ->		-128 to 127
						2 byte --> 16 bit-->		-2^15 to (2^15)-1 ->			
						4 byte --> 32 bit-->		-2^31 to (2^31)-1
								-128	to	+127
							
					
									msb --> most sign bit--> sign bit
									0 ---> +ve
									1 ---> -ve
			
			num = 101283981832137182738217312813871872183218	-> any number-->
			int num = 129389128392138219389213892183918391389231 --> will be failed inside -- statically typed
			4 byte --> -2^31 to (2^31)-1
	
	
We need these softwares for developement purpose-
	--> Python Interpretter	--> whatever source code  -->	Interpretter --->	machine code/binary
	--> Pycharm --> IDE		--> to write python code--> which provides--> intelligent enough-->
								automcomplete--> methods/functions--->
									--> faster developement
	--> Notepad ++			--> whatever u copy/notes-> notepad++ --> developement handy..
	
	
steps -->
		step1 --> download and install -->	https://www.python.org/downloads/
				3.8.6 -->  3 - major version ==> in case new functionality added inside software which was not there prev. major change/impact on application
						   8 -- minor version==> in case functionlity,want extend the given/existing functionality
						   6 --> code patch ==> in case defect/issue resolution--
						   
		once we install this software --> installation would be inside-->
		
		actual path on my machine --> C:\Users\Yogesh\AppData\Local\Programs\Python\Python37-32
		
		
			C:\Users\urname\AppData\Local\Programs\Python\Python38-32
	
Open Control Panel - top right corner -> env -->
											Account 
											System --> click -->Enviroment variables
																new --> bottom side la
	edit path variable -- in which we need add two more variable--> mentioned below..
	
		--> %PYTHON_HOME%		  ---> C:\Users\Yogesh\AppData\Local\Programs\Python\Python37-32
			%PYTHON_HOME%\Scripts --> C:\Users\Yogesh\AppData\Local\Programs\Python\Python37-32\Scripts
			
			
	--> open fresh cmd prompt- ->

			
			
--> python --version
--> pip --version

---> it means that python interpretter properly configured on ur machine-->

PIP --> PYTHON INSTALLS PACKAGE--> TO INSTALL REQUIRED LIBS/PACKAGES-->


---> WE NEED TO DOWNLOAD ONE MORE--> PYCHARM --> COMMUNITY
		https://www.jetbrains.com/pycharm/download/#section=windows
		
	download --> install it as we install other softwares--> 
	c:prog files -->
	
--> python interpretter -->https://www.python.org/downloads/ --> cmd  line la --> python --version -- pip --version-->
--> pycharm community edition -->	https://www.jetbrains.com/pycharm/download/#section=windows
--> notepad ++		--> https://notepad-plus-plus.org/downloads/


-------------------------------------------------------------------------------------->

		Windows --> env variables		--> command prompt -->
		Pycharm -- Existing interpretter --> pycharm code-->
		
variables --> its memory location 
	
	datatype -> type of data --> which type of data is present on that location->
	
		generics -->				 	python					java
					generic	
						Number	-->	int float complex		byte short int long float long
						Chars	--> str						String
						Boolean ---> True/False				true/false
						NoValue --> None					Null
						
Major Datatypes-->
		Number	-->
						+ve/-ve --> its integral
						num = 0			num = 10		---> int
						num = -1203						--> int
						
Major Types--> type	
	Number
		int
		float
		complex
	String							multiline
			''		""			'''	'''		"""	"""
	boolean 
			 val = True				val = False
	
	absence -->		value = None
	
	
	
						
						
						
		Python  is 
					--> dynamically typed--			
	


		
		
		
		


		
		A extends Thread
		
		
						//2 thread
		A a1 = new A();	//run  -- instance method	--> single
		A a2 = new A(); //run` --> instance method --> single
		
		
		
		impl
		
		
		A a = new A()		// single thread --> 		multiple
		Thread t1 = new Thread(a)
		Thread t2 = new Thread(a)
		
		


class A:

	sync m1 
	
	sync m2
		
		m3



t1 -- ob1
t2 -- ob2
										*									*
m1 m2 m3 --> type of method -->		instance methods 				== static method--> 		combi





Account --> bank stmt		--

											Account
													with
													draw


-->Thread class methods -->
-->Object class methods -->- 5 methods
--> approaches--> extends Thread -- implements Runnable/callable
--> static sync vs instance sync -- methods level
--> critical section -- block level -->	static method / instance -method-->
--> Thread lifecycle-->
==> producer / consumer -->
			
			
			8.30pm --> 

	
	thread created --- new / in born
	
			class A extends Thread
				A a1 = new A()	---> stage1-- new/inborn
				a.start()	-- runnable	--> run method--No
			
			class A implements Runnable
				A a1 = new A()
				Thread t1 =new Thread(a1)	// stage1 -->new /inborn
				
				t1.start()		--> runnable
				
				
				
				a.start -- not going to start task ->
							when os picks that thread from thread scheduler- cpu assign
							algo -->
							 actually -- task -- run method execution -->  running
							 
				10 thread --> quad -- 4 -->
												timed waiting
												i/o waiting
									waiting
										
	new/inborn	--> runnable	--> running			-- completed
					start()			cpu assign				task completed
				
				
		--> final class vs all methods final --> Open Point


	1-100	-->
					1 sec		--> n threads--> computer can executed--> only that much of thread 
									at the same time --> cores
		t1
		t2
		t3
		
		
		
		t100
								no of cores			practically			multithreading
		p4-->	 				1					one thread			yes	-- time slicing
		dual core				2					2					yes
		quad core				4					4					yes
		hexa					6					6					yes
		octa					8					8					yes
		
		
		t1 		t2 		t3 		t4 		t5 		--> 		t2
		1min	5min	2min	4mins	3min				
		
			30sec	--> 
			context switching-->
			operating system
				fcfs -- round robin --> timeslicing --> prioritybased--> lru -->		-->os
						t1 t2 t3 t4
						
						
						
			
		



singlethreaded		--> mainthread..



--single threded
--multithreaded --> fast


1-100--> numbers
1 sec --> 
		100 sec
		
	
					independently -- task --> 
							25 sec
	w1 --> 1-25
	w2 -->26-50
	w3 -->51-75
	w4--> 76-100
	
	
	req  --> sequentially -->
	w1			--> 100 sec						-->
			--> 	-------------> 100 sec
	
	!sync
	w1-w4	--> 25 sec	--> failed--> data consistent nasel--> 100--> 
		w1
		w2
		w3
		w4
	
	sync										--> unnecessary overhead--> 
		w1--> 25
				w2
					w3
						w4
						
	w1-w4	--> more than 100 secs
	



Threading -->
		
		Single Threaded
		Multithreaded


Multi -->	
		Tasking
		Threading
		
		Programming		--> program
		Processing		--> 1/m


processes --> 
		task - unit of work-->
		
		
		firefox	--> launch		tasks
				w1 --> p1 --> 	t1,t2		-->  upload/download
				w2 --> p2 -->	t1,t2,t3		-->  torrent -- download1/download2/download3
				w3 --> p3 -->	t1,t2,t3,t4,t5,t6,t7,t8		--> surfing--online music/down1,2,3/upload1,2,3

	program -- run -- process/es --> task -->
									same processes --> multiple processes
																	subprocesses
																			process--> will handle-- task seperatly
	programming lang-->
				program --> 
						runtime instance
								process/es
									--> lightweight processes -- to handle task seperatly
											lightweight processes-- threads--> 
													threads-- under processes
														thread/subprocess--> task -work --

1program -- processes --> subprocesses/	--> tasks
		lang	
			program		
				process	
					thread --> worker 
					task  --> work



				
--> programming lang-->

			java ->  programs-->
					1 program	--> run --> program at runtime --> process
					n programs	--> run --> programs at runtime--> process
					
		1 program --> with 1/n -- processes
		1 program --> 1 or many
		n program  --> 1 or many processes		--> javaw.exe
		
	with the help of programming--> lang -> program -- runtime instance process/es
	
		


'''