
ttl_class=int(input("Number of total classes: "))
attnd_class=int(input("Number of class you attend: "))
attnd_prctg=(attnd_class/ttl_class)*100

print("Percetage of attendance:",attnd_prctg)

if attnd_prctg>=75:
    print("Student can sit in the exam")
else:
    print("Student failed to sit in the exam")