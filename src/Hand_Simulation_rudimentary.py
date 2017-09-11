####Alter the parameters in the following block for various test cases
inter_arrival_time=6
service_completion_time=10
retransmission_time=5
simulation_time=200
queue_size=2
#Assigning the first arrival time as 2
cla=2
#######################################################################
wait_queue=list()
orbiting_dev=[]
clr=0
cls=0
mc=0
output_file = open("./IOT_Hand_Simulation.tsv","w")
def generate_next_arrival():
    global cla,clr,cls,mc,inter_arrival_time,wait_queue,orbiting_dev,retransmission_time,queue_size
    cla=cla+inter_arrival_time
    if(len(wait_queue)==0):
        if(cls==0):
            cls=cls+mc+10
            wait_queue.append(mc)
        else:
            cls=cls+10
            wait_queue.append(mc)
    elif(len(wait_queue)<queue_size ):
        wait_queue.append(mc)
    elif(len(wait_queue)>=queue_size):
        orbiting_dev.append(mc+retransmission_time)
def do_on_service_completion():
    global cla,clr,cls,mc,inter_arrival_time,wait_queue,orbiting_dev,retransmission_time,queue_size
    cls=mc+service_completion_time
    if(len(wait_queue)>0):
        wait_queue.pop(0)
def perform_retransmission():
    global cla,clr,cls,mc,inter_arrival_time,wait_queue,orbiting_dev,retransmission_time,queue_size
    orbiting_dev.pop(0)
    if(len(wait_queue)<queue_size):
        wait_queue.append(mc)
    else:
        orbiting_dev.append(mc+retransmission_time)
def run_simulation():
    global cla,clr,cls,mc,inter_arrival_time,wait_queue,orbiting_dev,retransmission_time,queue_size,clr,cls
    print(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev))
    output_file.write(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev)+"\n")
    mc=cla
    generate_next_arrival()
    print(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev))
    output_file.write(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev)+"\n")
    while(mc<=simulation_time):
        if(len(orbiting_dev)==0):
            clr=0
        else:
            clr=orbiting_dev[0]
        if(clr==0 and cls !=0):
            mc=min(cla,cls)
        else:
            mc=min(cla,clr,cls)
        if(mc==clr):
            perform_retransmission()
            print(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev))
            output_file.write(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev)+"\n")
            continue
        elif(mc==cla):
            generate_next_arrival()
            print(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev))
            output_file.write(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev)+"\n")
            continue
        elif(mc==cls):
            do_on_service_completion()
            print(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev))
            output_file.write(repr(mc)+"\t"+repr(cla)+"\t"+repr(cls)+"\t"+repr(len(wait_queue))+"\t"+repr(orbiting_dev)+"\n")
            continue

run_simulation()
output_file.close()
