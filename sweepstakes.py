import random


class Sweepstakes:
    def __init__(self):
        self.contestants = []

    def add_contestant(self, first_name, last_name, license_num):
        contestant = {
            "firstName": first_name,
            "lastName": last_name,
            "fullName": f'{first_name} {last_name}',
            "driversLicenseNumber": license_num
        }
        self.contestants.append(contestant)

    def random_winner(self):
        cont_pool = []
        for person in self.contestants:
            cont_pool.append(person["driversLicenseNumber"])
            x = random.randint(0, len(cont_pool) - 1)
        winning_num = cont_pool[x]
        for person in self.contestants:
            if person["driversLicenseNumber"] == winning_num:
                print(person["fullName"] + " has won!")
                break
