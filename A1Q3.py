# Question 3 

yearlyseconds = 60 * 60 * 24 * 365
twoyearlyseconds = yearlyseconds * 2
threeyearlyseconds = yearlyseconds * 3
fouryearlyseconds = yearlyseconds * 4
fiveyearlyseconds = yearlyseconds * 5


pop0 = 312032486

yearlybirths = yearlyseconds // 7
yearlydeaths = yearlyseconds // 13
yearlyimmigrants = yearlyseconds // 45

twoyearlybirths = twoyearlyseconds // 7
twoyearlydeaths = twoyearlyseconds // 13
twoyearlyimmigrants = twoyearlyseconds // 45

threeyearlybirths = threeyearlyseconds // 7
threeyearlydeaths = threeyearlyseconds // 13
threeyearlyimmigrants = threeyearlyseconds // 45


fouryearlybirths = fouryearlyseconds // 7
fouryearlydeaths = fouryearlyseconds // 13
fouryearlyimmigrants = fouryearlyseconds // 45

fiveyearlybirths = fiveyearlyseconds // 7
fiveyearlydeaths = fiveyearlyseconds // 13
fiveyearlyimmigrants = fiveyearlyseconds // 45

pop1 = pop0 + yearlybirths - yearlydeaths + yearlyimmigrants
pop2 = pop0 + twoyearlybirths - twoyearlydeaths + twoyearlyimmigrants
pop3 = pop0 + threeyearlybirths - threeyearlydeaths + threeyearlyimmigrants
pop4 = pop0 + fouryearlybirths - fouryearlydeaths + fouryearlyimmigrants
pop5 = pop0 + fiveyearlybirths - fiveyearlydeaths + fiveyearlyimmigrants


print ("population after one year", pop1)
print ("population after two years", pop2) 
print ("population after three years", pop3) 
print ("population after four years", pop4)
print ("population after five years", pop5) 
