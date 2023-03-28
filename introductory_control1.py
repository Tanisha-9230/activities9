'''Problem Statement- I
Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.

Steps to Follow: 
Understand how net run rate getting calculated (Cite the reference in submission comment)
Follow the computational thinking process.
Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
Design Controls -  Compound Statements and Suites
Provide Feedback to the User (Console level Feedback)
Test (Paper Calculation)
Validate (Paper Calculation = Code  Result)'''

#inputs for calculating net run rate.
team1=input("enter 1 st team name: ")   #input team name
team2=input("enter 1 st team name: ")
team1_runs =int(input("team 1 scores: "))   #input run scored by two teams.
team2_runs =int(input("team 2 scores: "))
team1_overs=int(input("team 1 overfaced: "))  #input run faced by two teams.
team2_overs=int(input("team 2 overfaced: "))
team1_runs_conceded=int(input("team 1 runs conceded: "))   #runs conceded refer to the total number of runs that a bowling team has allowed the opposition team to score during their innings. 
team2_runs_conceded =int(input("team 2 runs conceded: "))
team1_overs_bowled = int(input("team 1 overs bowled: ")) #overs bowled" refers to the number of completed overs that a team has bowled during the opposition team's innings.
team2_overs_bowled =int(input("team 2 overs bowled: "))

team1_nrr = (team1_runs/ team1_overs) - (team1_runs_conceded / team1_overs_bowled) # team 1 and 2 net run rate. Reference: https://www.sportskeeda.com/cricket/what-net-run-rate-cricket 
team2_nrr = (team2_runs/ team2_overs) - (team2_runs_conceded / team2_overs_bowled)

print("Net Run Rate of", team1, round(team1_nrr, 2)) 
print("Net Run Rate of", team2, round(team2_nrr, 2))

# Check which team tops the points table
if team1_nrr > team2_nrr:                                  
    print(team1, "tops the points table")
elif team2_nrr > team1_nrr:
    print(team2, "tops the points table")
#tie breaker condition
else:
    print("Both teams have the same NRR. The teams are tied.")
