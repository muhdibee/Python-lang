class Attendee:
    'Common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def display_attendee(self):
        print('Name: {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))


# Create Attendee instances.
attendee_1 = Attendee('B. Giles', 2)
attendee_2 = Attendee('J. Ortega', 1)

# Access Attendee methods
attendee_1.display_attendee()
attendee_2.display_attendee()
attendee_2.addTicket()
attendee_2.addTicket()
