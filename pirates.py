class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew


    def Is_worth_it(self):

        if (self.draft + self.crew*1.5) - (self.crew)> 20:
            return True
        return False

