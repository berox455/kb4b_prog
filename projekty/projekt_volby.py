import random
import copy

class Vote_simulator:
    def __init__(self):
        self.parties = ["ANO", "Spolu", "STAN", "SPD", "Pirati", "Stacilo!", "Motoriste", "Prisaha"]
        self.preference = [32.6, 21.1, 11.2, 10.1, 8.7, 7.7, 5.4, 2.1]
        self.noise_preference = []
        self.voters = 8838567 #podle https://zpravy.kurzy.cz/811680-vekove-slozeni-obyvatelstva-2024/ lidi 18 plus
        self.voting_voters = None
        self.partic_range = [60, 75] #min max range of participation
        self.results = {
            "ANO":0,
            "Spolu":0,
            "STAN":0,
            "SPD":0, 
            "Pirati":0, 
            "Stacilo!":0, 
            "Motoriste":0, 
            "Prisaha":0
        }


    def add_noise(self):
        beta_noise_preference = []

        for num in self.preference:
            beta_noise_preference.append(round(num+random.randrange(-2, 2), 2))

        self.noise_preference = beta_noise_preference

    
    def gen_participation(self):
        min = self.partic_range[0]
        max = self.partic_range[1]
        participation = random.randrange(min,max)
        return participation / 100 #pro procenta

    
    def gen_vv(self): #voting voters
        vv = self.gen_participation() * self.voters
        self.voting_voters = int(round(vv, 0)) 


    def simulation(self):
        br = copy.copy(self.results) #beta results
        for voter in range(self.voting_voters):
            vote = random.choices(self.parties, self.noise_preference)[0]
            br.update({vote: br[vote]+1})

        self.results = br


    def print_party_stats(self):
        for party in self.results:
            votes = self.results[party]
            print("Strana:", party, "Pocet_hlasu:", votes, votes/self.voting_voters+"%")


    def gen_voter_chart(self):
        return chart 

    
    def mandate_counter(self):
        return count


    def play(self):
        self.add_noise()
        self.simulation()
        print_party_stats()

        return None
    


sim = Vote_simulator()

sim.play()