print(''' _   _  ___    _   _  _____  ___    _   _  ___    ___      
( ) ( )|  _`\ ( ) ( )(  _  )(  _`\ ( ) ( )(  _`\ (  _`\    
| | | || (_) )| |_| || (_) || ( (_)| |/'/'| (_(_)| | ) |   
| | | || ,  / |  _  ||  _  || |  _ | , <  |  _)_ | | | )   
| (_) || |\ \ | | | || | | || (_( )| |\`\ | (_( )| |_) |   
(_____)(_) (_)(_) (_)(_) (_)(____/'(_) (_)(____/'(____/'   
                                                           ''')
with open("website.log.txt","r") as f:
                             lines=f.readlines()
                             with open("output.txt",'wt') as nf:
                                                             for line in lines:
                                                                              line=line.split(" ")
                                                                              nf.write("IP \t Date time \t Time Zone \t Request Type \t Path \t HTTP Protocol \t Status Code \t Packet size \t User Info \n")
                                            #   print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(line[0],line[3],line[5],line[6],line[7],line[8],line[9],line[11]))    
                                                                              nf.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(str(line[0]).replace('"',' '),line[3],line[5],line[6],line[7],line[8],line[9],(str(line[11]).replace('"',' '))) )
                                            #   to relace extra quotations with blank   
                                                                                                                   